# Forge Classic 简体中文汉化

[English](README.md) | 中文

适用于 `sd-webui-forge-classic` / Forge 风格 WebUI 的简体中文汉化扩展。插件使用 WebUI 标准本地化机制，不通过脚本强制遍历或替换网页文本。

## 功能

- 提供 `localizations/zh_CN.json`。
- 覆盖 txt2img、img2img、Extras、PNG Info、Checkpoint Merger、Settings、Extensions 等常见界面文本。
- 覆盖内置脚本：Prompt Matrix、Prompts from file、Loopback、SD upscale、X/Y/Z Plot 等。
- 覆盖常见 Forge/扩展界面文案：ControlNet、LoRA、Extra Networks、Compile、Never OOM、MultiDiffusion、IPAdapter、Spectrum、Radial Attention、Soft Inpainting 等。
- 不翻译模型名、采样器名、文件名、LoRA 名或提示词文本。

## 安装

1. 将整个 `sd-webui-forge-classic-zh-cn` 文件夹复制到 WebUI 的 `extensions` 目录。
2. 重启 WebUI，或使用 Reload UI。
3. 打开 **设置 > 用户界面 > 本地化**。
4. 选择 `zh_CN`，应用设置并重载界面。

## 维护

如果上游 Forge 新增英文文案，可继续在以下文件中补充精确翻译：

```text
localizations/zh_CN.json
```

## 说明

- 这是汉化插件，不额外加入语言切换。
- 插件不修改 Forge 原生文件。
- 它刻意使用 WebUI 的本地化机制，而不是用 JavaScript 扫描并替换页面文本。
