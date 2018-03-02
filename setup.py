# Copyright (c) 2018 Patrick Pedersen <ctx.xda@gmail.com>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

long_description = "Bash button is a simple python server that can execute bash commands and bash scripts on the push of my modified/hacked Staples Easy Button. Which scripts to be executed on which event is configured trough a simple configuration file."

setup(
    name='bashbutton',
    version='0.1.0',
    description='Bootstrap bash scripts to your EasyButton!',
    long_description=long_description,
    url='https://github.com/UniQHW/EasyButton_BashButton',
    author='Patrick Pedersen',
    author_email='ctx.xda@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',

        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='pyserial arduino staples easybutton',

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
          'serial',
          'pyserial',
    ],

    entry_points={
        'console_scripts': [
            'bash-button=BashButton.__main__:main',
        ],
    },

    project_urls={
        'Project': 'https://github.com/UniQHW/EasyButton_Docs',
        'Bug Reports': 'https://github.com/UniQHW/EasyButton_BashButton/issues',
        'Source': 'https://github.com/UniQHW/EasyButton_BashButton',
    },
)
