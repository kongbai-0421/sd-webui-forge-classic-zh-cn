from __future__ import annotations

import json
import re
from pathlib import Path

import gradio as gr

from modules import localization as localization_module
from modules import script_callbacks, scripts, shared


EXTENSION_ROOT = Path(scripts.basedir())
LOCALIZATION_FILE = EXTENSION_ROOT / "localizations" / "zh_CN.json"
API_INFO_RE = re.compile(rb"<script>window\.gradio_api_info = .*?</script>", re.DOTALL)


def load_zh_cn() -> dict:
    try:
        with LOCALIZATION_FILE.open("r", encoding="utf8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def patch_localization_loader():
    original_localization_js = localization_module.localization_js

    def external_zh_cn_localization_js(current_localization_name: str) -> str:
        if current_localization_name != "zh_CN":
            return original_localization_js(current_localization_name)

        # Keep the HTML head small: load the zh_CN dictionary as a cacheable
        # external JSON request instead of embedding it directly into the page.
        return """
window.localization = {};
try {
    const request = new XMLHttpRequest();
    request.open("GET", "/sd-webui-forge-classic-zh-cn/localization", false);
    request.send(null);
    if (request.status >= 200 && request.status < 300) {
        window.localization = JSON.parse(request.responseText || "{}");
    }
} catch (error) {
    console.error("Failed to load zh_CN localization", error);
}
"""

    localization_module.localization_js = external_zh_cn_localization_js


def patch_gradio_api_info_inline():
    if getattr(shared, "forge_classic_zh_cn_api_info_patch", False):
        return

    if not hasattr(shared, "GradioTemplateResponseOriginal"):
        shared.GradioTemplateResponseOriginal = gr.routes.templates.TemplateResponse

    previous_template_response = gr.routes.templates.TemplateResponse

    def compact_api_info_template_response(*args, **kwargs):
        response = previous_template_response(*args, **kwargs)
        response.body = API_INFO_RE.sub(b"<script>window.gradio_api_info = {};</script>", response.body)
        response.init_headers()
        return response

    gr.routes.templates.TemplateResponse = compact_api_info_template_response
    shared.forge_classic_zh_cn_api_info_patch = True


def patch_controlnet_batch_dir_sync():
    if getattr(shared, "forge_classic_zh_cn_controlnet_batch_dir_patch", False):
        return

    try:
        from lib_controlnet.controlnet_ui.controlnet_ui_group import ControlNetUiGroup
    except Exception:
        return

    def register_sync_batch_dir(cls):
        batch_dirs = [
            cls.global_batch_input_dir,
            cls.a1111_context.img2img_batch_input_dir,
        ]
        batch_dirs = [comp for comp in batch_dirs if comp is not None]

        if not batch_dirs:
            return

        def determine_batch_dir(*dirs: str) -> None:
            batch_dir = dirs[0] if len(dirs) > 0 else ""
            fallback_dir = dirs[1] if len(dirs) > 1 else ""
            cls.GLOBAL_CONTROLNET_BATCH_DIR = batch_dir if batch_dir else fallback_dir

        for comp in batch_dirs:
            comp.blur(
                fn=determine_batch_dir,
                inputs=batch_dirs,
                queue=False,
            )

    ControlNetUiGroup.register_sync_batch_dir = classmethod(register_sync_batch_dir)
    shared.forge_classic_zh_cn_controlnet_batch_dir_patch = True


def register_options():
    shared.options_templates.update(
        shared.options_section(
            ("forge_classic_zh_cn", "Forge Classic 中文汉化", "ui"),
            {
                "forge_classic_zh_cn_notice": shared.OptionHTML(
                    """
                    <b>Forge Classic zh-CN Localization</b><br>
                    This extension provides the standard WebUI localization file
                    <code>localizations/zh_CN.json</code>. Select <code>zh_CN</code>
                    in <b>Settings &gt; User Interface &gt; Localization</b>, then reload the UI.
                    It does not force-replace page text with scripts.<br><br>
                    <b>中文说明</b><br>
                    本插件仅提供 WebUI 标准本地化文件 <code>localizations/zh_CN.json</code>。
                    请在“设置 &gt; 用户界面 &gt; 本地化”中选择 <code>zh_CN</code>，然后重载界面。
                    插件不会用脚本强制替换网页文本。
                    """
                ),
            },
        )
    )


def register_api(_demo, app):
    @app.get("/sd-webui-forge-classic-zh-cn/localization")
    async def localization():
        return load_zh_cn()


register_options()
patch_localization_loader()
patch_gradio_api_info_inline()
script_callbacks.on_before_ui(patch_controlnet_batch_dir_sync)
script_callbacks.on_app_started(register_api)
