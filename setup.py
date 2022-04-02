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
    description="WordTrie: a simple trie (prefix tree) for word and phrase matching",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Indexing",
        "Topic :: Text Processing :: Linguistic"
    ],
    provides=["wordtrie"],
    packages=find_packages(),
    python_requires=">=3"
)
