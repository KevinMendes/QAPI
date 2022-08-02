import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QAPI",
    version="0.0.1_alpha",
    author="Kevin Mendes",
    author_email="kevin.mendes35@gmail.com",
    description="This package is made to automated Rest API test, and give you the possibility to keep a traceability of these",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/KevinMendes/QAPI",
    packages=setuptools.find_packages(),
    install_requires  = ['Click','requests',...], # List all your dependencies inside the list
    license = 'Mozilla Public License Version 2.0'
)