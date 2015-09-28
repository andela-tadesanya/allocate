try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description': 'takes a list of employees and allocates them randomly to office rooms and living spaces',
    'author': 'Tosin Adesanya',
    'url': 'https://github.com/andela-tadesanya/allocate',
    'download_url': 'https://github.com/andela-tadesanya/allocate',
    'author_email': 'oluwatosin.adesanya@andela.com',
    'version': '0.1',
    'install_requires': [],
    'packages': [],
    'name': 'allocate',
]

setup(**config)
