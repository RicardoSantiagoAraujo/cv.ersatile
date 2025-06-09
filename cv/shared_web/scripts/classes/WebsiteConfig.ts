
export class WebsiteConfig {
    lang: string;
    version: string;
    title: string;
    infoInInHeader: string[];
    sectionsToInclude: string[];

    constructor(
      { lang, version, title, infoInInHeader, sectionsToInclude }: 
      { lang: string; version: string, title: string, infoInInHeader: string[], sectionsToInclude: string[] }) {
      this.lang = lang;
      this.version = version;
      this.title = title;
      this.infoInInHeader = infoInInHeader;
      this.sectionsToInclude = sectionsToInclude;
    }
  }