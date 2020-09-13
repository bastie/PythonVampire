# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
@author: Sͬeͥbͭaͭsͤtͬian
'''
# pip3 install -U --requirement requirements.txt
# pip3 install -U --requirement requirements-devel.txt

import compileall

# if we are in src directory
#

# check py syntax
compileall.compile_dir(".")

# clear
# $ rm -Rf VampireAPI.egg-info dist build ../docs
#
# check license
# python3 -m reuse lint
#
# check code problems and format
# but ignore first line, because SPDX information are too long
# python3 -m flake8 | grep -v ":1:80: E501"
#
# build module
# python3 setup.py sdist bdist_wheel
# python3 -m twine check dist/*
# python3 -m twine upload dist/*
#
# build docs
# python3 -m pdoc --html --output-dir ../docs/_build/html java
#
# add all
#
# git add ../.
# git commit
# git push
#
