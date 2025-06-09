import { WebsiteConfig } from "../classes/WebsiteConfig";

/**
 * Function to add a section to the html document.
 * @param section_name Name of the section to be added
 * @param config Website configuration object
 */
export function addSection(section_name: string, config: WebsiteConfig) {
  var secEl: HTMLElement = document.createElement("section");
  let secClass: string = "section-" + section_name;
  secEl.classList.add(secClass);
  // Create a new element (e.g., a div or span)
  let secTitle = document.createElement("h1");
  // Optionally, add a class or other attributes
  secTitle.classList.add("section__title");
  // Set the inner HTML
  secTitle.innerHTML = `${section_name}`;
  // Append the new element to the header
  secEl.appendChild(secTitle);
  document.body!.appendChild(secEl);

  fetch(
    `./sections/${section_name}/${section_name}_contents_${config.version}_${config.lang}.html`
  )
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch HTML file");
      }
      return response.text(); // Get the HTML as text
    })
    .then((htmlContent) => {
      // Do something with the HTML content
      // Wrap it into a div element
      let content_container = document.createElement("div");
      content_container.innerHTML = htmlContent;
      content_container.classList.add("section__content");
      document.querySelector("section." + secClass)!.append(content_container); // Insert HTML into a DOM element

      secTitle.addEventListener("click", function () {
        console.log(`Section ${section_name} clicked!`);
        secEl.classList.toggle("section--hidden"); // Toggle visibility of the section contents
      });
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

/**
 * Function to loop through desired sections and add them to the html document. 
 * @param config Website configuration object
 */
export function addMultipleSections(config: WebsiteConfig)
  {
    for (let section_name of config.sectionsToInclude) {
      addSection(section_name, config);
    }
}

/**
 * Function to add a header to the html document.
 * @param const_general user general data object
 * @param config Website configuration object
 */
export function addHeader(const_general, config: WebsiteConfig): void {
  var secEl: HTMLElement = document.createElement("header");
  let header_class: string = "header";
  secEl.classList.add(header_class);
  secEl.innerHTML = ``;
  document.body!.appendChild(secEl);
  fetch(`./sections/header/header.html`)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch HTML file");
      }
      return response.text(); // Get the HTML as text
    })
    .then((htmlContent) => {
      // Do something with the HTML content
      document.querySelector("header." + header_class)!.innerHTML +=
        htmlContent; // Insert HTML into a DOM element
      var subjectName = document.querySelector("header .subject-name");
      var subjectTitle = document.querySelector("header .subject-title");
      var headerList = document.querySelector("header .header__list");
      var headerPicture = document.querySelector("header .header__right img");
      subjectName!.textContent = `${const_general.name} ${const_general.surname}`;
      if (const_general.title) {
        subjectTitle!.textContent = `, ${const_general.title}`;
      }
      if (const_general.picture) {
        headerPicture!.setAttribute(
          "src",
          "../assets/" + const_general.picture
        );
      }
      for (let key of config.infoInInHeader) {
        if (!const_general[key]) {
          continue; // Skip keys not chosen to be included in the header
        }
        // Create a new element (e.g., a div or span)
        let el = document.createElement("ki");
        // Set the data-general attribute
        el.setAttribute("data-general", key);
        // Optionally, add a class or other attributes
        el.classList.add("header__list__item");
        // Set the inner HTML
        el.innerHTML = const_general[key];
        // Append the new element to the header
        headerList?.appendChild(el);
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
    meta = document.createElement("meta");
    meta.name = name;
    document.head.appendChild(meta);
  }
  meta.content = content;
}

/**
 *  Function change title of the document in the title tag.
 * @param config Website configuration object
 */
export function updateTitle(config: WebsiteConfig): void {
  console.log("Updating title to: ", config.title);
  let titleTag = document.querySelector("title") as HTMLTitleElement;
  console.log(titleTag);
  titleTag.textContent = config.title;
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
