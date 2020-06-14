"""Setup script for package_name wich contains module_name"""
import os.path
from setuptools import setup
# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))
# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()
# This call to setup() does all the work
setup(
    name="module_name",
    version="1.0.0",
    description="Does THINGS",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zell0ss/logparser.git",
    author="zelloss",
    author_email="zelloss@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    # refers to the folder where the package actually is
    packages=["module_name"],
    include_package_data=True,
    install_requires=[
        "re"
    ],
    entry_points={"console_scripts": ["parseit=logparser.__main__:main"]}, 
 #the entrypoint bit will be the name of the entrypoint
)