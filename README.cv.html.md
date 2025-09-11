# CV.ersatile Generated Website

This feature is a web version of the CV generated from the python scripts, and is an additional feature of the cv.ersatile, which is otherwise built around the tex output.

### Use

First, ensure you are at the **profiles/{profile_name}/webpage/** directory.

1. Run the typescript transpiler in one of a number of ways:

```
tsc --watch
tsc
tsc --project <path/to/tsconfig.json>
```

2. Run a SCSS transpiler in one of a number of ways:

```
sass --watch styles/main.scss:styles/main.css
sass --no-source-map --update .:.
```

3. Configure webpage in **websiteConfig.json**

There are default styles being imported from a shared folder, but feel free to overwrite them in your **styles/folder**.
