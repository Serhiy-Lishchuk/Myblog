from setuptools import setup, find_packages

setup(
    name='Myblog',
    version='1.04',
    packages=find_packages,
    install_requires=['Flask', 'Pillow'],
    url='https://github.com/Serhiy-Lishchuk/Myblog',
    license='Free',
    author='serhiy',
    description='Blog on Flask'
)
