import { const_general } from "./constants/general.js";

console.log(const_general)
function addSection(section_name: string){
    var sec_el: HTMLElement = document.createElement('section');
    let sec_class: string = "section-" + section_name;
    sec_el.classList.add(sec_class);
    sec_el.innerHTML=
    `
    <h1>${section_name}</h1>
    `;
    document.body!.appendChild(sec_el);

    fetch(`./sections/${section_name}/${section_name}_contents_en.html`)
    .then((response) => {
        if (!response.ok) {
          throw new Error('Failed to fetch HTML file');
        }
        return response.text(); // Get the HTML as text
      })
      .then((htmlContent) => {
        // Do something with the HTML content
        document.querySelector("section."+sec_class)!.innerHTML += htmlContent; // Insert HTML into a DOM element
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
        console.log(key + " : " + value);
        console.log(`header.${header_class} .const_${key}`)
        let el = document.querySelector(`header.${header_class} .const_${key}`);
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
addSection("experience")
addSection("education")
addSection("popScience")
addSection("research")
addSection("teaching")
