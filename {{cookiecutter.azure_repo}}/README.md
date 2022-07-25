# {{ cookiecutter.project|title }}

## Goal

TODO: Briefly describe the goal of the project here...

## Installation

To install this project on the workbench, first create a new Anaconda environment:

```shell
conda create --file environment.yml
```

Activate the environment to start working with it:

```shell
conda activate {{ cookiecutter.azure_repo }}
```

Then create a folder for the project and clone the repository from Azure DevOps:

```shell
git clone {{ cookiecutter.azure_url }}
```

## Project Structure

The project has the following folder structure:

|Folder|Contents|
|---|---|
|dashboard|Folder containing PowerBI dashboard(s).|
|models|Folder containing trained models / model artefacts.|
|notebooks|Folder containing Jupyter Notebooks and Python code.|
|output|Folder for storing output images, graphs, et cetera.|
|sql|Folder containing (explorative) SQL scripts.|

TODO: Feel free to remove any folders your project does not require.

## Usage

TODO: Describe how to use your project...

## Contributing

If you want to contribute to this project, feel free to clone the code, make
improvements and open a pull request!

If you have suggestions or remarks not directly related to the project's code or
documentation, feel free to e-mail the authors.

## Maintainers

This project is maintained by:

1. {{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})
