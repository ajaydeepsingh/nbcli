from setuptools import setup

setup(
    name='nbcli',
    version='0.1',
    description='Command-line interface for accessing NetBox records',
    author='Ajaydeep Singh, Dave Noonan',
    py_modules=['nbcli'],
    install_requires=[
        'Click', 'pynetbox'
    ],
    entry_points='''
        [console_scripts]
        nbcli=nbcli:cli
    ''',
)
