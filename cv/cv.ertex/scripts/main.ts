import { config } from "../config.js";
import * as utils from "./utils.js";

console.log("Creating PDF and HTML links..."); 
utils.createPdfLinks(config);
utils.createHtmlLinks(config);
