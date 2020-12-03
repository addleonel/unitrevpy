import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uconvert",
    version="0.0.2",
    license="MIT",
    author="A. D. Leonel",
    author_email="adleonel@gmail.com",
    description="This contains common unit conversions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/addleonel/unit-converter",
    packages=setuptools.find_packages(),
    install_requires=['numpy'],
    keywords=['unit', 'convert', 'conversion'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)