# Exploration Cookiecutter

## Goal

This cookiecutter is used to set up exploratory data science projects. It creates a
folder structure on your  harddrive, creates standard configuration files, and sets up
git and Anaconda.

## Installation

To use this cookiecutter, you should have the cookiecutter package available on your
system. To install cookiecutter into your current Python environment, type:

```shell
python -m pip install cookiecutter
```

Or if you prefer Anaconda:

```shell
conda install cookiecutter
```

After installing cookiecutter, you can use templates to kickstart your Python projects!

## Usage

Once you have cookiecutter installed, you can use the template to create a new project.
Go to the folder on your local drive where you want to create the new project and type:

```shell
cookiecutter https://github.com/LFKoning/cookiecutter_exploration
```

This will start cookicutter and ask you for the following inputs:

|Input|Description|Example|
|---|---|---|
|`author_name`|Your first and last name.|`Lukas Koning`|
|`author_email`|Your e-mail address.|`lfkoning@gmail.com`|
|`project`|Title for your project.|`Test Project`|
|`azure_user`|Your username in Azure DevOps.|`lukas_koning`|
|`azure_project`|Project name in Azure DevOps.|`TEST`|
|`azure_repo`|Name of the project's repository.|`test-project`|
|`azure_url`|URL to the project's repository|`https://lukas_koning@dev.azure.com/lukas_koning/TEST/_git/test_project`|
|`python_version`|The Python version you are using.|`3.9`|
|`create_git`|Create a new git repository? (y/n).|`y`|
|`create_conda`|Create a new Anaconda environment? (y/n)|`y`|
|`precommit`|Install pre-commit hooks? (y/n).|`y`|

If a default value is available, cookiecutter will display the default between square
brackets (`[..]`). Simply press `Enter` to accept the default value and continue.

*Tip: If you make an error filling in the values, you can either stop the process using
`CTRL + C` of continue and correct the mistake later on.*

After filling in all the fields, you should see a new folder with your package's name in
the current folder. If you navigate to the package folder, you will see a skeleton with
the default file layout to create a simple Python package.

Depending on the final three choices, cookiecutter will also:

1. Have initialized a local git repository.
2. Set the git remote to the correct Azure DevOps repository.
3. Created a new Anaconda environment with the name of your package.
4. Installed development packages; black, pylint, pre-commit.
5. Installed pre-commit hooks for black, pylint, et cetera.

So you should be all good to go; good luck!

If you chose to skip any of the above steps, you should perform them manually from a
(Anaconda) command prompt in the package folder:

1. Initialize a new git repository: `git init`
2. Set git remote: `git remote add origin <Azure Repository URL>`
3. Create Anaconda environment: `conda create -n <package name> python=<python version>`
4. Install development packages: `conda install black pylint pre-commit`
5. Install pre-commit hooks: `pre-commit install`

Performing these actions manually should have the same result as using the cookiecutter
template, but allows for a bit more control over the process.

*Tip: Using the standard development packages is highly recommended!*

## Contributing

If you want to contribute to this project, feel free to clone the code, make
improvements and open a pull request!

If you have suggestions or remarks not directly related to the project's code or
documentation, feel free to e-mail the authors.

## Maintainers

1. Lukas Koning (lukas.koning@afm.nl)
