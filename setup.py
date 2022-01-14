from setuptools import setup, find_packages

setup(
    name='navier_stoked',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Derives the Navier Stokes equations in different coordinate systems',
    #long_description=open('README.txt').read(),
    long_description='TBA',
    install_requires=['sympy'],
    url='https://github.com/bolverk/navier_stoked',
    author='Almog Yalinewich',
    author_email='almog.yalin@gmail.com'
)
