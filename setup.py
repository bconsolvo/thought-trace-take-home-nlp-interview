# Taken from example setup.py here: https://github.com/pypa/sampleproject/blob/master/setup.py
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
    
#The "# Required" paramters are necessary for uploading to pypi.
setup(
    name='ocr_bconsolvo', # Required
    version='1.0.0', # Required
    description='Solving challenges with pytesseract and building my own OCR functions', # Required
    #long_description='Here' # Optional
    url='https://github.com/bconsolvo/ocr_bconsolvo', # Optional
    author='Benjamin Consolvo', # Optional
    #author_email='email@email.com' # Optional
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software DEvelopment :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],
    #keywords='keywords' # Optional
    packages=find_packages(), # Required
    python_requires='>=3.5',
    #install_requires=['none'], # Optional
    #extras_require={} # Optional
    #package_data = {} # Optional
    #data_files=[] # Optional
    #entry_points={} # Optional
    #project_urls={}
)    
