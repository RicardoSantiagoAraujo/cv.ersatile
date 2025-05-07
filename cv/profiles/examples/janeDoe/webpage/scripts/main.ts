import { const_general } from "./constants/general.js";

const version: string="full";
const lang:string ="en";


function addSection(section_name: string){
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



function addHeader(){
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

addHeader()
addSection("description")
addSection("experience")
addSection("education")
addSection("popScience")
addSection("research")
addSection("teaching")
addSection("programming")
addSection("other")
addSection("awards")
addSection("certificates")
addSection("works")
addSection("publications")
