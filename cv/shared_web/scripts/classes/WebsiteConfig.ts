export class WebsiteConfig {
  lang: string;
  version: string;
  title: string;
  infoInInHeader: string[];
  sectionsToInclude: string[];
  backgroundTexture: string;
  pageTexture: string;

  constructor({
    lang,
    version,
    title,
    infoInInHeader,
    sectionsToInclude,
    backgroundTexture,
    pageTexture,
  }: {
    lang: string;
    version: string;
    title: string;
    infoInInHeader: string[];
    sectionsToInclude: string[];
    backgroundTexture: string;
    pageTexture: string;
  }) {
    this.lang = lang;
    this.version = version;
    this.title = title;
    this.infoInInHeader = infoInInHeader;
    this.sectionsToInclude = sectionsToInclude;
    this.backgroundTexture = backgroundTexture;
    this.pageTexture = pageTexture;
  }
}
