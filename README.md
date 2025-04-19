# C.V.ersatile
Repository to share a highly versatile and customizable curriculum vitae template.

### Introduction:

This template allows you to create more than one profile, meaning that you can store CV's for multiple people simultaneously while relying on the same tex code and functions.
Additionally, the template is build around "elements", premade sections of a CV that can be customized. Alternatively, you can yourself create your own element from scratch.
Finally, for a given profile, it is possible to hold multiple versions, which lets you store more than one CV in parallel: for example for you might be applying for jobs as software developer and as teacher, two jobs which very different demands but still with some overall. c.v.ersatile makes it easy to keep CVs ready for both. To do this, you use the scripts present in the .scripts/ folder.

### Generating contents:

While you may keep make all yours changes directly to the tex files in elements, I advice you to make use of the python integration that is built into c.v.ersatile. This way, you can neatly separate from content, easily switch between different section styles, and benefit from an HTML version of your CV as well, ready to be deployed as a personal website.


### Requirements
#### On Windows
##### Recommended Set-up with Visual Studio Code:
- Install the LaTeX distribution [Miktex](https://miktex.org/download)
- Install the Pearl distribution [Strawberry](https://strawberryperl.com/)
- Install the Latex Workshop extension
- Ideally, set the compilation output path in **settings.json** to

````
"latex-workshop.latex.outDir": "%DIR%/auxiliary_files"
````

and add "-outdir=%OUTDIR%" as an argument in "latex-workshop.latex.recipes".


> You may need to restart Visual Studio Code or your machine.




### Suggested Usage:

You can pull the contents of this repository to the root one of your as follows:

- First, you add this repository as a remote to your own:
````
git remote add {desired name of remote}  {address of remote}
git remote add cv.ersatile  https://github.com/RicardoSantiagoAraujo/cv.ersatile.git
````
- You can then simply pull from it by specifying the remote. Use the option flag if you get an unrelated histories error.
````
git pull {name of remote} {branch to pull from} [--allow-unrelated-histories]
git pull cv.ersatile main
````

Ideally, you wouldn't touch any of the existing files... instead, you should add new profiles as needed based on the available examples.



### Troubleshooting compilation
- Use lualatex to compile
- Ensure required fonts are installed on the computer (even if there is a fallback system in place)
- Some packages might need to be installed, so ensure you have an internet connection
