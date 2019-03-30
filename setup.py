"""
sphinx-graphml
Graphml charts embedding tool for Sphinx
"""

from setuptools import setup, find_packages
import os

PACKAGE = 'sphinx_graphml'

# credentials
AUTHOR = 'Thomas Khyn'
AUTHOR_EMAIL = 'thomas@ksytek.com'
URL = 'https://bitbucket.org/tkhyn/sphinx-graphml/'

# imports __version__ and __version_info__ variables
exec(open('sphinx_graphml/version.py').read())

dev_status = __version_info__[3]
if dev_status == 'alpha' and not __version_info__[4]:
    dev_status = 'pre'

DEV_STATUS = {'pre': '2 - Pre-Alpha',
              'alpha': '3 - Alpha',
              'beta': '4 - Beta',
              'rc': '4 - Beta',
              'final': '5 - Production/Stable'}

setup(
    name=PACKAGE,
    version=__version__,
    description='GraphML charts embedding extension for Sphinx',
    long_description=open(os.path.join('README.rst')).read(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    keywords=['sphinx', 'graphml', 'yEd', 'chart'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Development Status :: %s' % DEV_STATUS[dev_status],
        'License :: OSI Approved :: MIT License',
        'Environment :: Plugins',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'Topic :: Documentation :: Sphinx'
    ],
    packages=find_packages(),
    install_requires=(
        'sphinx>=2.0'
    ),
    # static files are not available from zipped directories, so we need to set this flag to False
    zip_safe=False
)
