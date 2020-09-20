# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 01.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
from builtins import staticmethod, str
from java.nio.file.Path import Path
from java.lang.Object import Object
import codecs


class Files(Object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    @staticmethod
    def readString(path: Path) -> str:
        '''
        Java 11 like implementation
        see Javadoc 11 Files.html#readString(java.nio.nio.nio.file.Path)
        '''
        textFile = codecs.open(path.toString(), "r", "utf-8")
        text = textFile.read()
        textFile.close()
        return text
