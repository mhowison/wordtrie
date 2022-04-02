from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

with open("wordtrie/VERSION") as f:
    version = f.read().strip()

setup(
    name="wordtrie",
    author="Mark Howison",
    author_email="mark@howison.org",
    version=version,
    url="https://github.com/mhowison/wordtrie",
    description="WordTrie: A simple trie (prefix tree) for word matching",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8"
    ],
    provides=["wordtrie"],
    packages=find_packages(),
    python_requires=">=3.8"
)
