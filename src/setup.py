# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VampireAPI", 
    version="0.0.3",
    author="Sͬeͥbͭaͭsͤtͬian",
    author_email="bastie@users.noreply.github.com",
    description="Just Another Vampire Api 4 Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bastie/PythonVampire",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Java Libraries"
    ],
    python_requires='>=3.6',
)
