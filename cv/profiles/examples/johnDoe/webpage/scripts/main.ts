function addSection(section_name: string){
    var sec_el: HTMLElement = document.createElement('section');
    let sec_class: string = "section-" + section_name;
    sec_el.classList.add(sec_class);
    sec_el.innerHTML=
    `
    <h1>${section_name}</h1>
    `;
    document.body!.appendChild(sec_el);

    fetch(`./${section_name}/${section_name}_contents_en.html`)
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
  let sec_class: string = "header";
  sec_el.classList.add(sec_class);
  sec_el.innerHTML=``;
  document.body!.appendChild(sec_el);
  fetch(`./general.html`)
  .then((response) => {
      if (!response.ok) {
        throw new Error('Failed to fetch HTML file');
      }
      return response.text(); // Get the HTML as text
    })
    .then((htmlContent) => {
      // Do something with the HTML content
      document.querySelector("header."+sec_class)!.innerHTML += htmlContent; // Insert HTML into a DOM element
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

addHeader()
addSection("experience")
addSection("education")
