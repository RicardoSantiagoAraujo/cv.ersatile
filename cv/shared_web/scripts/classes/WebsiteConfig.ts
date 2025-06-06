
export class WebsiteConfig {
    lang: string;
    version: string;
    title: string;

    constructor({ lang, version, title }: { lang: string; version: string, title: string }) {
      this.lang = lang;
      this.version = version;
      this.title = title;
    }
  }