import { const_general } from "./constants/general.js";
import * as  contents from "./helpers/change_contents.js";

///////////////////////////////////////////////////////////////////////
// Pick CV version and language
export const version: string="full";
export const lang:string ="en";


///////////////////////////////////////////////////////////////////////
// Chose CV section to be displayed
contents.updateMeta("author", `${const_general.name} ${const_general.surname}`);
contents.setDocumentLanguage(lang);
contents.addHeader()
contents.addSection("description")
contents.addSection("experience")
contents.addSection("education")
contents.addSection("popScience")
contents.addSection("research")
contents.addSection("teaching")
contents.addSection("programming")
contents.addSection("other")
contents.addSection("awards")
contents.addSection("certificates")
contents.addSection("works")
contents.addSection("publications")
