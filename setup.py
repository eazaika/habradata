from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='habradata',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    install_requires=[
        'pymongo==3.7.2',
        'Scrapy==1.5.1',
        'mongo==0.2.0'
    ]
)
