import subprocess
from glob import glob
from os.path import splitext, basename

import setuptools


def get_version():
    try:
        git = subprocess.Popen(
            ["git", "describe", "--always", "--dirty"], stdout=subprocess.PIPE
        )
        stdout, stderr = git.communicate()
        gitlabel = stdout.decode().strip()
        with open("VERSION", "w") as fo:
            fo.write(gitlabel)
    except OSError:
        with open("VERSION", "r") as fo:
            gitlabel = fo.read()

    return gitlabel


with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flaskhost",
    version=get_version(),
    author="Terrel Shumway",
    author_email="ghdev@flaskhost.com",
    description="Command Line Interface for https://flaskhost.com/",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/flaskhost/flaskhost-cli",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=True,
    install_requires=["Click"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["flaskhost=flaskhost.cli:main"]},
)
