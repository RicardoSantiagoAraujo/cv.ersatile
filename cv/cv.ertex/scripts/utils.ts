export function createPdfLinks(config: any) {
   var list = document.querySelector("#section__pdf ul")

   config.pdfs.forEach((pdf: any) => { 
    var li = document.createElement("li")
    var a = document.createElement("a")
    a.href = `../profiles/${pdf.profile}/published_pdfs/${pdf.filename}`
    a.textContent = pdf.name
    li.appendChild(a)
    list?.appendChild(li)
   })
}

export function createHtmlLinks(config: any) {
    var list = document.querySelector("#section__pdf ul")
 
    config.pdfs.forEach((pdf: any) => { 
     var li = document.createElement("li")
     var a = document.createElement("a")
     a.href = `../profiles/${pdf.profile}/webpage/index.html`
     a.textContent = pdf.name
     li.appendChild(a)
     list?.appendChild(li)
    })
 }
