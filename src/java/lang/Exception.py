# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 07.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''

from java.lang.Throwable import Throwable


class JException(Throwable):
    '''
    Because Python knows base class Exception this class is called JException.
    see Javadoc
    '''

    def __init__(self, message="", cause: Throwable = None):
        '''
        Constructor
        '''
        super().__init__(message, cause)
