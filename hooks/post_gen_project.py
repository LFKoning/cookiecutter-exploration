"""Module with pre-generation cookiecutter hooks."""
import os
import shutil


def is_yes(value):
    """Checks for a yes input."""
    if isinstance(value, str) and value.lower().startswith("y"):
        return True
    return False


print("\n\n")
print("Post-processing cookiecutter template.")

# Create git repo
if is_yes("{{ cookiecutter.create_git }}"):
    print("Setting up the git repository.")
    os.system("git init")

    print("Adding remote: {{ cookiecutter.azure_url }}.")
    os.system("git remote add origin {{ cookiecutter.azure_url }}")

# Create Anaconda environment
if is_yes("{{ cookiecutter.create_conda }}"):
    print("Creating Anaconda environment: {{ cookiecutter.azure_repo }}.")
    os.system("conda env create -f environment.yaml")

    # Pre-commit setup
    if is_yes("{{ cookiecutter.precommit }}"):
        # Note: Requires a git repository to be initialized!
        if is_yes("{{ cookiecutter.create_git }}"):
            print("Installing pre-commit hooks.")
            os.system(
                "conda activate {{ cookiecutter.azure_repo }} "
                + "& python -m pre-commit install"
            )
        else:
            print("Cannot install pre-commit hooks; no git repository!")
            print("Type `pre-commit install` in the package folder to install manually.")

    else:
        # Remove pre-commmit config
        os.remove(".pre-commit-config.yaml")

print("All done!")
