(function () {
    // Keep this extension compatible with WebUI's normal localization system.
    // Do not walk or rewrite the DOM here; forced translation can corrupt
    // Settings/JSON panels and third-party plugin UIs.
    onUiLoaded(function () {
        document.documentElement.lang = "zh-CN";
    });
})();
