from setuptools import setup, find_packages

setup(
    name='library_modeling_tools',
    version='0.1.0',
    author='Jane Smith',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
