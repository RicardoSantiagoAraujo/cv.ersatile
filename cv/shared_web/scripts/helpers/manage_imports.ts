export async function import_shared_files(configData: any) {
  // Shared functions
  let functions: any = await import("./change_contents.js");

  // Website Configuration class
  let WebsiteConfig: any = (await import("../classes/WebsiteConfig.js"))
    .WebsiteConfig;

  // Shares stylesheet
  const link = document.createElement("link");
  link.rel = "stylesheet";
  link.href = "./../../../../shared_web/styles/main_shared.css";
  document.head.appendChild(link);

  // Return an object containing the imported modules and the instantiated config
  return {
    functions: functions,
    websiteConfig: new WebsiteConfig(configData),
  };
}
