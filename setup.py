from setuptools import setup, find_packages

LONG_DESCRIPTION = """
Overview
--------------

+ date_range: help you generate date between 2 date

"""

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
]

setup(
    name='date-cli',
    version=open('VERSION').read().strip(),
    author='Hsueh-Hung Cheng',
    author_email='jhengsh.email@gmail.com',
    url='https://github.com/Jhengsh/tidyframe',
    description='Data Command for shell',
    scripts=['date_cli/bin/date_range'],
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    keywords=['pandas', 'tidy'],
    packages=find_packages(),
    license='MIT',
    platforms='any',
)
