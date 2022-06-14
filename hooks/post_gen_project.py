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
    os.system(
        "conda create --yes --quiet --name {{ cookiecutter.azure_repo }} "
        + "python={{ cookiecutter.python_version }}"
    )

    print("Installing development packages.")
    os.system(
        "conda activate {{ cookiecutter.azure_repo }} "
        + "& conda install --yes --quiet black pylint"
    )

    # Pre-commit setup
    if is_yes("{{ cookiecutter.precommit }}"):
        # Install pre-commit and hooks
        print("Installing pre-commit and hooks.")
        os.system(
            "conda activate {{ cookiecutter.azure_repo }} "
            + "& python -m pip install pre-commit"
        )
        os.system("conda activate {{ cookiecutter.azure_repo }} & pre-commit install")

    else:
        # Remove pre-commmit config
        os.remove(".pre-commit-comfig.yaml")

print("All done!")
