# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
@author: Sͬeͥbͭaͭsͤtͬian
'''


# pip3 install -U --requirement requirements.txt 
# pip3 install -U --requirement requirements-devel.txt 


# if we are in src directory
#
# clear 
# $ rm -Rf VampireAPI.egg-info dist build ../docs
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