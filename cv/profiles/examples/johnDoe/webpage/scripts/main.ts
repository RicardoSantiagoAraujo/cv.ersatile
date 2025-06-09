import { const_general } from "./constants/general.js";

let contents: any;
let WebsiteConfig: any;

try {
  // ====== IMPORTS WHEN PROFILES ARE AT THE PROFILES ROOTFOLDER ======
  // @ts-ignore
  contents = await import("../../../../shared_web/scripts/helpers/change_contents.js");
  // @ts-ignore
  WebsiteConfig = (await import("../../../../shared_web/scripts/classes/WebsiteConfig.js")).WebsiteConfig;

} catch (e1) {
  try {
    // ====== IMPORTS WHEN PROFILES IN A SUBFOLDER LIKE "EXAMPLES" ======
    // @ts-ignore
    contents = await import("../../../../../shared_web/scripts/helpers/change_contents.js");
    // @ts-ignore
    WebsiteConfig = (await import("../../../../../shared_web/scripts/classes/WebsiteConfig.js")).WebsiteConfig;
  } catch (e2) {
    console.error("Failed to load files from both paths");
    throw e2; // or handle error gracefully
  }
}
import configData from './../websiteConfig.json';
const websiteConfig = new WebsiteConfig(configData);

///////////////////////////////////////////////////////////////////////
contents.updateMeta("author", `${const_general.name} ${const_general.surname}`);
contents.setDocumentLanguage(websiteConfig.lang);
contents.updateTitle(websiteConfig);
contents.addHeader(const_general, websiteConfig);
contents.addMultipleSections(websiteConfig); 
