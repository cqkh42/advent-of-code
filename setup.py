from setuptools import setup, find_packages

setup(
    name="aoc_cqkh42",
    version="0.1",
    description="cqkh42's solutions for https://adventofcode.com/ using aoc_cqkh42 Python",
    url="https://github.com/myusername/advent-of-code-myusername",
    author="cqkh42",
    author_email="jackcooper93@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Games/Entertainment :: Puzzle Games",
    ],
    install_requires=[
        "advent-of-code-data >= 0.8.0",
    ],
    packages=find_packages(),
    entry_points={
        "adventofcode.user": ["cqkh42 = aoc_cqkh42:answer"],
    },
)
