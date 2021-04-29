from __future__ import absolute_import, division, print_function
from setuptools import setup, find_packages

# Long description will go up on the pypi page
with open('README.md') as file:
    LONG_DESCRIPTION = file.read()

opts = dict(name='echopydantic',
            maintainer='Landung Setiawan',
            maintainer_email='landungs@uw.edu',
            description='Pydantic data models for SONAR-netCDF4 convention.',
            long_description=LONG_DESCRIPTION,
            long_description_content_type='text/markdown',
            url='https://github.com/lsetiawan/echopydantic',
            download_url='',
            license='Apache License, Version 2.0',
            classifiers=['Development Status :: 3 - Alpha',
                         'Environment :: Console',
                         'Intended Audience :: Science/Research',
                         'License :: OSI Approved :: Apache Software License',
                         'Operating System :: OS Independent',
                         'Programming Language :: Python',
                         'Topic :: Scientific/Engineering'],
            author='Landung Setiawan',
            author_email='landungs@uw.edu',
            platforms='OS Independent',
            packages=find_packages(),
            install_requires=['pydantic'],
            py_modules=["_echopydantic_version"],
            use_scm_version={
                "fallback_version": "unknown",
                "local_scheme": "node-and-date",
                "write_to": "_echopydantic_version.py",
                "write_to_template": 'version = "{version}"\n',
            },
            setup_requires=["setuptools>=30.3.0", "wheel", "setuptools_scm"],)


if __name__ == '__main__':
    setup(**opts)