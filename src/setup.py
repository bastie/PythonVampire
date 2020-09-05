import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="VampireAPI", # Replace with your own username
    version="0.0.1",
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