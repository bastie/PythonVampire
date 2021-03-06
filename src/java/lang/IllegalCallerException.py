# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 05.10.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''

from java.lang.RuntimeException import RuntimeException
from java.lang.Throwable import Throwable


class IllegalCallerException (RuntimeException):
    '''
    classdocs
    '''

    def __init__(self, message="", cause: Throwable = None):
        '''
        Constructor
        '''
        super().__init__(message, cause)
