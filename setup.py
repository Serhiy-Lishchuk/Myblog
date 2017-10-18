from distutils.core import setup

setup(
    name='Myblog',
    version='1.04',
    packages=['', 'tests', 'Flaskblog', 'Flaskblog.db',
              'Flaskblog.views', 'Flaskblog.config', 'Flaskblog.models', 'Flaskblog.services'],
    url='https://github.com/Serhiy-Lishchuk/Myblog',
    license='Free',
    author='serhiy',
    description='Blog on Flask'
)
