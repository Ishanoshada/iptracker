from setuptools import setup, find_packages

setup(
    name='iptracker',
    version='1.0.3',
    packages=find_packages(),
    install_requires=['requests'],
    author='Ishan Oshada',
    author_email='ishan.kodithuwakku.official@email.com',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    description='A Python package for tracking IP addresses and their locations.',
    url='https://github.com/ishanoshada/iptracker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
