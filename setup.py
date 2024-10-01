from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="ubl-tr-py",
    version='0.1.0',
    packages=find_packages(),
    install_requires=required,

    entry_points=None,
    python_requires='>=3.7',
    include_package_data=True,
)
