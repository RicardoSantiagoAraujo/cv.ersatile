import { const_general } from "../constants/general.js";
import { version, lang } from "../main.js";


/**
 * Function to add a section to the html document.
 * @param section_name Name of the section to be added
 */
export function addSection(section_name: string){
    var sec_el: HTMLElement = document.createElement('section');
    let sec_class: string = "section-" + section_name;
    sec_el.classList.add(sec_class);
    sec_el.innerHTML=
    `
    <h1>${section_name}</h1>
    `;
    document.body!.appendChild(sec_el);

    fetch(`./sections/${section_name}/${section_name}_contents_${version}_${lang}.html`)
    .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch HTML file');
        }
        return response.text(); // Get the HTML as text
      })
      .then((htmlContent) => {
        // Do something with the HTML content
        // Wrap it into a div element
        let content_container = document.createElement('div');
        content_container.innerHTML = htmlContent;
        document.querySelector("section."+sec_class)!.append(content_container); // Insert HTML into a DOM element
      })
      .catch((error) => {
        console.error("Error:", error);
      });
}


/**
 * Function to add a header to the html document.
 */
export function addHeader(){
  var sec_el: HTMLElement = document.createElement('header');
  let header_class: string = "header";
  sec_el.classList.add(header_class);
  sec_el.innerHTML=``;
  document.body!.appendChild(sec_el);
  fetch(`./sections/header/header.html`)
  .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to fetch HTML file');
      }
      return response.text(); // Get the HTML as text
    })
    .then((htmlContent) => {
      // Do something with the HTML content
      document.querySelector("header."+header_class)!.innerHTML += htmlContent; // Insert HTML into a DOM element
      for (let key in const_general) {
        let value = const_general[key];
        let el = document.querySelector(`header.${header_class} [data-general=${key}]`);
        if (el){
          el.innerHTML = value;
        }
      }
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

/**
 *  Function to update or add a meta tag to the document head.
 * @param name meta tag name to be updated/created
 * @param content meta tag content to be set
 */
export function updateMeta(name: string, content: string): void {
  let meta = document.querySelector(`meta[name="${name}"]`) as HTMLMetaElement;

  if (!meta) {
    // Create the meta tag if it doesn't exist
    meta = document.createElement('meta');
    meta.name = name;
    document.head.appendChild(meta);
  }
  meta.content = content;
}


/**
 * Function to set the document language.
 * @param lang Language code to be set (e.g., "en", "fr", "de")
 */
export function setDocumentLanguage(lang: string): void {
  document.documentElement.lang = lang;
}

// Usage
setDocumentLanguage("fr"); // Changes to French