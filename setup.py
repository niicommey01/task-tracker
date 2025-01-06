from setuptools import setup

setup(
    name = "tasktracker",
    version = "1.0",
    py_modules = ["tasktracker"],
    install_requires = [],
    entry_points = {
        "console_scripts": [
            "tasktracker=tasktracker:main",
        ]
    },
    author = "Nii Commey",
    author_email = "jude.niicommey@outlook.com",
    description = "A simple task tracking CLI tool",
    long_description = open("README.md").read(),
    long_description_content_type= "text/markdown",
    url = "https://github.com/niicommey01/task-tracker",
    classifiers = [
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6",
)