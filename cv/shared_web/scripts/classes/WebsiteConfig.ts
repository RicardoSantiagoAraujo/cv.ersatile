
export class WebsiteConfig {
    lang: string;
    version: string;
    title: string;
    InfoInInHeader: string[];

    constructor(
      { lang, version, title, InfoInInHeader }: { lang: string; version: string, title: string, InfoInInHeader: string[] }) {
      this.lang = lang;
      this.version = version;
      this.title = title;
      this.InfoInInHeader = InfoInInHeader;
    }
  }