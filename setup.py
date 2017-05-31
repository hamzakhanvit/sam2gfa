from setuptools import setup
import sys

if not sys.version_info[0] == 3:
    sys.exit("Sorry, only Python 3 is supported")

files = ["data/*"]

setup(name='sam2gfa',
      version='1.0',
      description='SAM to GFA Converter ',
      author='Hamza Khan',
      author_email='hamza.khan@alumni.ubc.ca',
      packages=['sam2gfa'],
      scripts=['run-sam2gfa.py'],
      install_requires=[
              'gfapy',
              'simplesam',
              'numpy',
              'biopython',
      ],
      package_data = {'sam2gfa' : files },
      zip_safe=False)
