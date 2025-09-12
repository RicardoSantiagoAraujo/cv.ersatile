import fetch from "node-fetch"; // install with: npm i node-fetch

async function checkHref(url: string) {
  try {
    const res = await fetch(url, { method: "HEAD" }); // HEAD is faster
    if (res.ok) {
      console.log(`✅ ${url} is reachable (${res.status})`);
    } else {
      console.log(`⚠️ ${url} responded with status ${res.status}`);
    }
  } catch (err) {
    console.error(`❌ ${url} could not be reached`, err);
  }
}



export function createPdfLinks(config: any) {
   var list = document.querySelector("#section__pdf ul")

   config.pdfs.forEach((pdf: any) => {
   console.log("Processing PDF:", pdf)
   let href = `../profiles/${pdf.profile}/published_pdfs/${pdf.filename}.pdf`
   if (checkHref(href)){// Check if the link is reachable
      var li = document.createElement("li")
      var a = document.createElement("a")
      a.href =  href
      a.textContent = pdf.name
      li.appendChild(a)
      list?.appendChild(li)
      console.log("Added link for", pdf.name)
   } 
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
