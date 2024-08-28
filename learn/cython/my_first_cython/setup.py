from setuptools import setup
from Cython.Build import cythonize

#This tells compiler to compile the file mentioned
setup( ext_modules = cythonize("hello.pyx"))
setup( ext_modules = cythonize("fact.pyx"))

