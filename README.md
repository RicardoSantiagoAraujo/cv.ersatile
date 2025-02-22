# C.V.ersatile
Repository to share a highly versatile and customizable curriculum vitae template.

### Introduction:

This template allows you to create more than one profile, meaning that you can store CV's for multiple people simultaneously while relying on the same tex code and functions.
Additionally, the template is build around "elements", premade sections of a CV that can be customized. Alternatively, you can yourself create your own element from scratch.
Finally, for a given profile, it is possible to hold multiple versions, which lets you store more than one CV in parallel: for example for you might be applying for jobs as software developer and as teacher, two jobs which very different demands but still with some overall. c.v.ersatile makes it easy to keep CVs ready for both. To do this, you use the scripts present in the .scripts/ folder.

### Generating contents:

While you may keep make all yours changes directly to the tex files in elements, I advice you to make use of the python integration that is built into c.v.ersatile. This way, you can neatly separate from content, easily switch between different section styles, and benefit from an HTML version of your CV as well, ready to be deployed as a personal website.


###  Troubleshooting bibliography in LaTeX documents
#### Running Biber
Make sure to run it from directory where root tex file is located, qnd not to include file extension
```
biber path/to/output/files/without/extension
```

#### Clearing Biber cache:
https://tex.stackexchange.com/questions/140814/biblatex-biber-fails-with-a-strange-error-about-missing-recode-data-xml-file

If citations are coming out empty ([citation_code]), you might need to clear the biber cache: Biber creates binaries in a cache folder, and sometimes that can get corrupted. In order to solve the problem, you need to manually delete the cache folders.
You can find the location of the cache folder by looking at the .blg file, or by using the command.
```
biber --cache
```
On Linux and Mac, this can be combined to delete the offending folder in one command:
```
rm -rf `biber --cache`
```


### Converting from pdf to word:
```
pandoc <source_name.tex> -o <destination_name.docx>
```
