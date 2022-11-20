# research-template :microscope:

![version](https://img.shields.io/badge/version-1.0-blue) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)

This repository serves as a template for **scientific research projects** utilizing Python and R language.

| **NOTE.** The structure of this project developed during my academic research career. 

## Project Intro/Objective :mag:

The purpose of this project is _______.

### Remarks

* A definition of the structure can be obtained under `structure.txt`
* All data exploration steps, are performed in notebooks using scripts, classes and functions located in the `/src_*` folders.
* To install the **conda environment** `ml-1` run `conda env create -f environment.yml`
  * Best practice shows, that you should modify/extend the the environment name with your project name, e.g. `ml-1-recsys23`
* To update module version in environment.yml run `conda env update --name ml-1 --file environment.yml --prune`
* To run **Jupyter Notebooks** and import custom modules (under `/src_py`) in Visual Studio Code you need to change `.vscode/settings.json` property `jupyter.notebookFileRoot` to `${workspaceFolder`

To pull changes/updates from this template into your project folder run

```sh
git remote add template https://github.com/malill/research-template.git
git fetch --all
# ATTENTION: this might lead to merge conflicts
git merge template/main --allow-unrelated-histories
```

### Acknowledgment

Initial project structure was created by https://github.com/dssg/hitchhikers-guide.git
