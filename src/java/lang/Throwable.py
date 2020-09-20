# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 07.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''

from java.lang.Object import Object


class Throwable(Object, Exception):
    '''
    see Javadoc
    '''

    def __init__(self, message="", cause: 'Throwable' = None):
        '''
        Constructor
        '''
        self.problemMessage = message
        self.problemCause = cause

    def getMessage(self) -> str:
        return self.problemMessage

    def getCause(self) -> 'Throwable':
        return self.problemCause
