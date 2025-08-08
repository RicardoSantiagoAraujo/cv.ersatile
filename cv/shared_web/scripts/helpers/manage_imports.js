export async function import_shared_files(configData, pathAdjust) {
    // Shared functions
    let functions = await import("./change_contents.js");
    // Website Configuration class
    let WebsiteConfig = (await import("../classes/WebsiteConfig.js"))
        .WebsiteConfig;
    // Shares stylesheet
    const link = document.createElement("link");
    link.rel = "stylesheet";
    link.href = pathAdjust + "../../../shared_web/styles/main_shared.css";
    document.head.appendChild(link);
    // Return an object containing the imported modules and the instantiated config
    return {
        functions: functions,
        websiteConfig: new WebsiteConfig(configData),
    };
}
//# sourceMappingURL=manage_imports.js.map