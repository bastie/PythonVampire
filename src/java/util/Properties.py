# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 05.10.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
from java.lang.Object import Object


class Properties(Object):
    '''
    classdocs
    '''

    properties = {}

    def __init__(self):
        '''
        Constructor
        '''
        pass

    def getProperty(self, key: str) -> str:
        return self.properties.get(key, None)

    def setProperty(self, key: str, value: str) -> Object:
        oldValue = self.getProperty(key)
        self.properties[key] = value
        return oldValue

    def list(self, output):
        output.println("-- listing properties --")
        keys = self.properties.keys()
        for key in keys:
            value = self.properties.get(key, "")
            value = (value[:37]+'...') if len(value) > 40 else value
            output.println(key + "=" + value)
