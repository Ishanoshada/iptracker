from setuptools import setup, find_packages

setup(
    name='iptracker',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['requests'],
    author='Ishan Oshada',
    author_email='ishan.kodithuwakku.official@email.com',
    description='A Python package for tracking IP addresses and their locations.',
    url='https://github.com/ishanoshada/iptracker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
