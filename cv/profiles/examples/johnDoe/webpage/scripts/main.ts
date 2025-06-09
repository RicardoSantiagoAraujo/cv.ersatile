// *********** PROFILE SPECIFIC IMPORTS ***********
import { const_general } from "./constants/general.js";
import configData from "../websiteConfig.js";

// *********** SHARED IMPORTS ***********
let importManager: any;
try {
  // IMPORTS WHEN PROFILES ARE AT THE PROFILES ROOTFOLDER
  importManager = await import(
    // @ts-ignore
    "../../../../shared_web/scripts/helpers/manage_imports.js"
  );
} catch (e1) {
  try {
    // IMPORTS WHEN PROFILES IN A SUBFOLDER LIKE "EXAMPLES"
    importManager = await import(
      // @ts-ignore
      "../../../../../shared_web/scripts/helpers/manage_imports.js"
    );
  } catch (e2) {
    console.error("Failed to load files from both paths !");
    throw e2; // or handle error gracefully
  }
}

///////////////////////////////////////////////////////////////////////
const { functions, websiteConfig } = await importManager.import_shared_files(
  configData
);

functions.updateMeta(
  "author",
  `${const_general.name} ${const_general.surname}`
);
functions.setDocumentLanguage(websiteConfig.lang);
functions.updateTitle(websiteConfig);
functions.addHeader(const_general, websiteConfig);
functions.setTextures(websiteConfig.backgroundTexture, websiteConfig.pageTexture);
functions.addMultipleSections(websiteConfig);
