from setuptools import setup, find_packages

setup(
    name='my_awesome_library',
    version='0.1.0',
    author='John Doe',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
