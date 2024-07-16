# Pygal


[![Build Status](https://travis-ci.org/Kozea/pygal.svg?branch=master)](https://travis-ci.org/Kozea/pygal)
[![Coverage Status](https://coveralls.io/repos/Kozea/pygal/badge.svg?branch=master&service=github)](https://coveralls.io/github/Kozea/pygal?branch=master)
[![Documentation Status](https://readthedocs.org/projects/pygal/badge/?version=latest)](https://readthedocs.org/projects/pygal/?badge=latest)


- [Pygal](#pygal)
    - [Description](#description)
    - [Installation](#installation)
    - [Test](#test)
    - [Contribute](#contribute)
    - [License](#license)

## Description

**pygal** is a dynamic SVG charting library written in python.
All the documentation is on [www.pygal.org](http://www.pygal.org)

## Instructions for building and installing the Pygal in local by compiling new changes each time

1. Clone the repository
2. Go to the project directory
```bash
cd path/to/pygal
```
3. Ensure you have setuptools and wheel installed:
```bash
pip install setuptools wheel
```
4. Create the distribution package
```bash
python setup.py sdist bdist_wheel
```

NOTE: If you run into any issues regarding missing packages, please install the missing libraries as specified.
This command will generate the distribution files (.whl file) in the dist directory.

## Installation

You can install the library using the `.whl` file:

1. Navigate to the `dist` directory.
```bash
cd dist
```

2. Install the `.whl` file using `pip`:

```sh
pip install pygal-3.0.4-py3-none-any.whl
```

## Test if the installation works fine

You can find sample.ipynb file in the project, restart the kernel and run this file to check if the bar chart is rendered without any issues and your changes are reflected.

## Installation in general

As simple as:

```
    $ pip install pygal
```



## Test

Pygal is tested with py.test:


```
    $ pip install pytest
    $ py.test
```


## Contribute

You are welcomed to fork the project and make pull requests.
Be sure to create a branch for each feature, write tests if needed and run the current tests !


You can also support the project:

[![Flattr](http://api.flattr.com/button/flattr-badge-large.png)](https://flattr.com/submit/auto?user_id=paradoxxx_zero&url=https://github.com/Kozea/pygal&title=Pygal&tags=github&category=software)
[![gittip](http://i.imgur.com/IKcQB2P.png)](https://www.gittip.com/paradoxxxzero/)



## License

Copyright © 2012-2016 Kozea
LGPLv3:

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
