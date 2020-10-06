import codecs
from setuptools import setup

with codecs.open('README.md', encoding='utf-8') as f:
    README = f.read()
    
setup(
    name='opencv-python',
    description='rebrand opencv-python-headless',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Robert Sachunsky',
    author_email='sachunsky@informatik.uni-leipzig.de',
    url='https://github.com/bertsky/wrap_opencv-python-headless',
    install_requires=['opencv-python-headless'],
    packages=[]
)
