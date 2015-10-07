try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='allocate',
      version='1.0',
      description='takes a list of employees and allocates them randomly to office rooms and living spaces',
      author='Oluwatosin Adesanya',
      author_email='oluwatosin.adesanya@andela.com',
      url='https://github.com/andela-tadesanya/allocate',
      packages=['allocate'],
      )