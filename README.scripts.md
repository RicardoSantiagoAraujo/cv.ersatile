# cv.ersatile scripts

This projects includes a bunch of functionalities incapsulated in the scripts module. These range from practical QOL features to powerful tools. 
The scripts module is divided into submodules, which you can run from the project root directory. Documentation for the scripts module is found inside the scripts/documentation directory.


## GENERATE

Generate a file from a python object (individual/multiple CV section(s) or set(s) of constants)

### Usage:
```
python -m scripts.generate.section <profile> <section name> <version> <language> <output format>
```
```
python -m scripts.generate.constants <profile> <constants set name> <version> <language> <output format>
```
```
python -m scripts.generate.multiple <sections/constants>
```


