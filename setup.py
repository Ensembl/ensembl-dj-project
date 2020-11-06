# Learn more: https://github.com/Ensembl/ols-client
import os

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    readme = f.read()

with open(os.path.join(os.path.dirname(__file__), 'LICENSE')) as l:
    license_ct = l.read()

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as v:
    version = v.read()


def import_requirements():
    with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]
        return content


setup(
    name='ebi-ols-client',
    version=version,
    description='Ensembl {{ project_name }} Django app',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='',
    author_email='mchakiachvili@ebi.ac.uk',
    url='https://github.com/Ensembl/ols-client',
    license=license_ct,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=import_requirements(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    setup_requires=[
        'setuptools>=41.0.1',
        'wheel>=0.33.4'
    ]
)