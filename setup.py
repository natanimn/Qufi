from setuptools import setup
from qufi import __version__ 


setup(
    name="qufi-script",
    author="Natanim Negash",
    author_email="natanimn@yahoo.com",
    description="A python package that changes Afan Oromo language script's witten in latin latters to geez latters",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    keywords=["qufi", "qube fidel", "qube to fidel", "qube to geez", "qube script", "python", "alphabet", "amharic", "oromo", "afan oromo", "latters", "latters convertors"],
    classifiers=['Programming Language :: Python :: 3.8'],
    version=__version__,
    license="MIT"    
)