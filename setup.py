import os
from setuptools import setup, find_packages

__version__ = '1.0' # 版本号
requirements = open('requirements.txt').readlines() # 依赖文件

setup(
    name = "fish",
    version = __version__,
    description = "Touch fish everyday~",
    license = "MIT Licence",
    url = "https://github.com/josephuszhou",
    author = "JosephusZhou",
    author_email = "josephuszhou@qq.com",
    packages = find_packages(exclude=["tests"]),
    platforms = "any",
    install_requires = requirements,

    scripts = [],
    entry_points = {
        'console_scripts': [
            'fish = fish:fish'
        ]
    }
)