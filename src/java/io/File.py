# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 01.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import os
from java.lang.Object import Object
from java.lang.UnsupportedOperationException \
     import UnsupportedOperationException
from builtins import str


class File(Object):
    '''
    classdocs
    '''

    separator: str = os.path.sep

    def __init__(self, *params):
        '''
        Constructor
        '''
        if 1 != len(params):
            # TODO: implement other java.io.File constructors with 2 params
            raise UnsupportedOperationException()
        if isinstance(params[0], str):
            self.path_as_string = params[0]
        else:
            raise UnsupportedOperationException()
            # TODO: implement other java.io.File constructor with URI

    def getCanonicalPath(self) -> str:
        return os.path.abspath(self.path_as_string)
