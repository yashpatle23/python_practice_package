from setuptools import find_packages, setup

with open("python_practice_package/README.md", "r") as f:
    long_description = f.read()

setup(
    name="python_practice_package",
    version="0.0.10",
    description="i made this to try different things",
    package_dir={"": "python_practice_package"},
    packages=find_packages(where="python_practice_package"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ArjanCodes/2023-package",
    author="Yash Patle",
    author_email="person.23.yash@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["bson >= 0.5.10 "],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)