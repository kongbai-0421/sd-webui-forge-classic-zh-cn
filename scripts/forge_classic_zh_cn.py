from __future__ import annotations

import json
from pathlib import Path

from modules import script_callbacks, scripts, shared


EXTENSION_ROOT = Path(scripts.basedir())
LOCALIZATION_FILE = EXTENSION_ROOT / "localizations" / "zh_CN.json"


def load_zh_cn() -> dict:
    try:
        with LOCALIZATION_FILE.open("r", encoding="utf8") as file:
            data = json.load(file)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


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
script_callbacks.on_app_started(register_api)
