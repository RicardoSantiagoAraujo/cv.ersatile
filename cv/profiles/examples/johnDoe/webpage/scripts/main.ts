import { const_general } from "./constants/general.js";
import * as contents from "../../../../../shared_web/scripts/helpers/change_contents.js";
import { WebsiteConfig } from "../../../../../shared_web/scripts/classes/WebsiteConfig.js";

///////////////////////////////////////////////////////////////////////
// Pick CV version and language
// export const version: string="full";
// export const lang:string ="en";
const websiteConfig: WebsiteConfig = new WebsiteConfig({
  lang: "en",
  version: "full",
  title: "John Doe's CV",
});

///////////////////////////////////////////////////////////////////////
// Chose CV section to be displayed
contents.updateMeta("author", `${const_general.name} ${const_general.surname}`);
contents.setDocumentLanguage("en");
contents.updateTitle(websiteConfig);
contents.addHeader(const_general);
contents.addSection("description", websiteConfig);
contents.addSection("experience", websiteConfig);
contents.addSection("education", websiteConfig);
contents.addSection("popScience", websiteConfig);
contents.addSection("research", websiteConfig);
contents.addSection("teaching", websiteConfig);
contents.addSection("programming", websiteConfig);
contents.addSection("other", websiteConfig);
contents.addSection("awards", websiteConfig);
contents.addSection("certificates", websiteConfig);
contents.addSection("works", websiteConfig);
contents.addSection("publications", websiteConfig);
