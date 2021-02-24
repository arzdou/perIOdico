import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="perIOdico-ARZDOU"
    version="0.0.1",
    author="Arzdou",
    author_email="arzdou@gmail.com",
    description="Download the first page of a date",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jtl125/perIOdico",
    project_urls={
        "Bug Tracker": "https://github.com/jtl125/perIOdico/issues",
    }
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.8',
)
