async function checkHref(
  url: string
): Promise<{ url: string; status: number | null; ok: boolean; error?: any }> {
  try {
    const res = await fetch(url, { method: "HEAD" });
    return {
      url,
      status: res.status,
      ok: res.ok,
    };
  } catch (err) {
    return {
      url,
      status: null,
      ok: false,
      error: err,
    };
  }
}

function createLink(href: string, item: any, list: HTMLElement) {
  checkHref(href).then((result) => {
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = href;
    if (result.ok) {
      a.textContent = item.name;
    } else {
      a.textContent = `[${result.status}] ` + item.name;
      a.style.color = "red";
      a.style.opacity = "0.5";
      a.classList.add("broken-link");
    }
    li.appendChild(a);
    list?.appendChild(li);
    console.log("Added link for", item.name);
  });
}

export function createPdfLinks(config: any) {
  var list = document.querySelector("#section__pdf ul") as HTMLElement;

  config.pdfs.forEach((item: any) => {
    // console.log("Processing PDF:", pdf);
    let href = `../profiles/${item.profile}/published_pdfs/${item.filename}.pdf`;
    createLink(href, item, list);
  });
}

export function createHtmlLinks(config: any) {
  var list = document.querySelector("#section__html ul") as HTMLElement;

  config.htmls.forEach((item: any) => {
    // console.log("Processing HTML:", pdf);
    let href = `../profiles/${item.profile}/webpage/index.html`;
    createLink(href, item, list);
  });
}
