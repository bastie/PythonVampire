# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 05.10.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
from java.lang.IllegalCallerException import IllegalCallerException
from java.lang.Throwable import Throwable


class IllegalInstantiationException(IllegalCallerException):
    '''
    This exception is raised if You call a private constructor
    and realized at runtime not instantiatable class
    '''

    def __init__(self,
                 message="private constructor call",
                 cause: Throwable = None):
        '''
        Constructor
        '''
        super().__init__(message, cause)
