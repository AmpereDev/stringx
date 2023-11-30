from setuptools import setup, find_packages
import stringx

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=stringx.__name__,
    version=stringx.__version__,
    author=stringx.__author__,
    author_email=stringx.__email__,
    description=stringx.__description__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=stringx.__repository__,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
