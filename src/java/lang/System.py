# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 01.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
from os.path import sys
from java.lang import Object


class System(Object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''

    @classmethod
    def exit(self, status: int):
        sys.exit(status)
