# Forge Classic zh-CN Localization

English | [中文](README_zh.md)

This extension provides Simplified Chinese localization files for `sd-webui-forge-classic` / Forge-style WebUI. It uses the standard WebUI localization system and avoids forced DOM text replacement.

## Features

- Provides `localizations/zh_CN.json`.
- Covers common txt2img, img2img, Extras, PNG Info, Checkpoint Merger, Settings, and Extensions UI text.
- Covers many built-in scripts such as Prompt Matrix, Prompts from file, Loopback, SD upscale, and X/Y/Z Plot.
- Covers common Forge/extension UI text such as ControlNet, LoRA, Extra Networks, Compile, Never OOM, MultiDiffusion, IPAdapter, Spectrum, Radial Attention, and Soft Inpainting.
- Does not translate model names, sampler names, filenames, LoRA names, or prompt text.

## Installation

1. Copy the whole `sd-webui-forge-classic-zh-cn` folder to the WebUI `extensions` directory.
2. Restart WebUI, or use Reload UI.
3. Open **Settings > User Interface > Localization**.
4. Select `zh_CN`, apply settings, and reload the UI.

## Maintenance

If upstream Forge adds new English UI text, add exact translations to:

```text
localizations/zh_CN.json
```

## Notes

- This is a localization extension, so no separate language toggle is added.
- The extension does not modify Forge core files.
- It intentionally uses WebUI's localization mechanism instead of scanning and replacing page text with JavaScript.
