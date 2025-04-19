
##  Bibliography
###  Troubleshooting bibliography in LaTeX documents

#### Running Biber
Make sure to run it from directory where root tex file is located, and not to include file extension
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
