"""
precisa compilar o código
Rodando no terminal:
python setup.py build_ext --inplace
"""


from distutils.core import setup

from Cython.Build import cythonize

setup(
    ext_modules=cythonize(['cumprimenta.pyx'])
)
