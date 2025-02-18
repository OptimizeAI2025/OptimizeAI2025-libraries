from setuptools import setup, find_packages

setup(
    name='library_data_utils',
    version='0.1.0',
    author='John Doe',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
