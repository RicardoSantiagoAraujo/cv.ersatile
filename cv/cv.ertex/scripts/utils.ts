export function createPdfLinks(config: any) {
   var list = document.querySelector("#section__pdf ul")

   config.pdfs.forEach((pdf: any) => {
   console.log("Processing PDF:", pdf)
    var li = document.createElement("li")
    var a = document.createElement("a")
    a.href = `../profiles/${pdf.profile}/published_pdfs/${pdf.filename}.pdf`
    a.textContent = pdf.name
    li.appendChild(a)
    list?.appendChild(li)
    console.log("Added link for", pdf.name)
   })
}

export function createHtmlLinks(config: any) {
    var list = document.querySelector("#section__html ul")
    config.htmls.forEach((html: any) => {
     var li = document.createElement("li")
     var a = document.createElement("a")
     a.href = `../profiles/${html.profile}/webpage/index.html`
     a.textContent = html.name
     li.appendChild(a)
     list?.appendChild(li)
     console.log("Added link for", html.name)
    })
 }
