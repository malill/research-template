<p float="left">
  <img src="./docs/.readme/Python_logo_and_wordmark.svg" height="75" />
  <img src="./docs/.readme/R_logo.svg" height="75" />
</p>

# research-template :microscope:

![version](https://img.shields.io/badge/version-1.1-blue) ![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg) ![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)

This repository serves as a template for **scientific research projects** utilizing Python and R language.

# Project Intro/Objective :mag:

The purpose of this project is _______.

# Remarks
* A definition of the structure can be obtained under `structure.txt`
* All data exploration steps are performed in notebooks using scripts, classes and functions located in the `/srcPy` and `/srcR` folders.
* To run **Jupyter Notebooks** and import custom modules (under `/srcPy`) in Visual Studio Code you need to change `.vscode/settings.json` property `jupyter.notebookFileRoot` to `${workspaceFolder`
  
# Environment Management (Python)

## Anaconda Environement

To install the **conda environment** `ml-1` run `conda env create -f environment.yml` . Best practice shows, that you should modify/extend the environment name with your project name, e.g. `ml-1-recsys23` . To update module version in environment.yml run `conda env update --name ml-1 --file environment.yml --prune`

## Virtual Environment (venv)

```cmd
# [Optional] If virtualenv is not installed run:
pip install virutalenv

python -m venv .venv
pip install -r requirements.txt
```

# Update Template in Project

To pull changes/updates from this template into your project folder run

```sh
git remote add template https://github.com/malill/research-template.git
git fetch --all
# ATTENTION: this might lead to merge conflicts
git merge template/main --allow-unrelated-histories
```

### Acknowledgment

Initial project structure was created by https://github.com/dssg/hitchhikers-guide.git
