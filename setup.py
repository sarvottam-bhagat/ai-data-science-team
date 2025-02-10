from setuptools import find_packages, setup
import os

def parse_requirements(filename):
    """Parse requirements from requirements.txt file"""
    filename = os.path.join(os.path.dirname(__file__), filename)
    with open(filename, "r") as f:
        return [line.strip() for line in f if line and not line.startswith("#")]

# Read long description from README if it exists
try:
    with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A text-to-SQL conversion tool using AI"

# Get version from version file
version = {}
with open("ai_data_science_team/_version.py", encoding="utf-8") as fp:
    exec(fp.read(), version)

setup(
    name="ai-data-science-team",
    version=version["__version__"],
    description="A text-to-SQL conversion tool using AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sarvottam Bhagat",
    author_email="sarvottambhagat38@gmail.com",
    url="https://github.com/sarvottam-bhagat/ai-data-science-team",
    packages=find_packages(exclude=["tests*"]),
    install_requires=parse_requirements("requirements.txt"),
    include_package_data=True,
    package_data={
        "": ["data/*"],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Database",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="text-to-sql, ai, nlp, database, sql",
) 