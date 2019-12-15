# from setuptools import setup

# setup(
#     name='exam_toolbox_02450',    # This is the name of your PyPI-package.
#     version='0.1',                          # Update the version number for new releases
#     scripts=['exam_toolbox']                  # The name of your scipt, and also the command you'll be using for calling it
# )


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="exam_toolbox_02450-pkg-s183920", # Replace with your own username
    version="0.0.1",
    author="Lukas Leindals",
    author_email="s183920@student.dtu.dk",
    description="Functions for exam in the course 02450 Introduction to machine learning and data mining at the Technical Univerity of Denmark",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/s183920/introML_02450_exam",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)