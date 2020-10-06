import codecs
from setuptools import setup
import subprocess

# from opencv-python in its pre-PEP518 state
# (needed to install opencv-python-headless at setup time
#  to mirror its version number, too):
def get_or_install(name, version=None):
    """ If a package is already installed, build against it. If not, install """
    # Do not import 3rd-party modules into the current process
    import json
    js_packages = json.loads(
        subprocess.check_output([sys.executable, "-m", "pip", "list", "--format", "json"]).decode('ascii'))  # valid names & versions are ASCII as per PEP 440
    try:
        [package] = (package for package in js_packages if package['name'] == name)
    except ValueError:
        install_packages("%s==%s" % (name, version) if version else name)
        return version
    return package['version']

def install_packages(*requirements):
    # No more convenient way until PEP 518 is implemented; setuptools only handles eggs
    subprocess.check_call([sys.executable, "-m", "pip", "install"] + list(requirements))

with codecs.open('README.md', encoding='utf-8') as f:
    README = f.read()

setup(
    name='opencv-python',
    description='rebrand opencv-python-headless',
    version=get_or_install('opencv-python-headless'),
    long_description=README,
    long_description_content_type='text/markdown',
    author='Robert Sachunsky',
    author_email='sachunsky@informatik.uni-leipzig.de',
    url='https://github.com/bertsky/wrap_opencv-python-headless',
    license='Apache License 2.0',
    install_requires=['opencv-python-headless'],
    packages=[]
)

