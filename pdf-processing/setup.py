from setuptools import setup, find_packages

setup(
    name='pdf_processing',
    version='0.1.0',
    author='Bemnet Alemayehu',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
