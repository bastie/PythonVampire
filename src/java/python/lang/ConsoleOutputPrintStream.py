# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 05.10.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import sys
import os
from java.io.PrintStream import PrintStream


class ConsoleOutputPrintStream (PrintStream):
    '''
    Wrapper using Python wrapper
    '''

    out = sys.stdout

    def __init__(self):
        '''
        Constructor
        '''

    def printJ(self, param):
        ConsoleOutputPrintStream.out.write(param)

    def println(self, param):
        self.printJ(param+os.linesep)
