# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 05.10.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import unittest
from java.lang.System import System

from java.lang.Throwable import Throwable


class testLangPackage(unittest.TestCase):

    consoleOutput = True

    def setUp(self):
        self.consoleOutput = False
        pass

    def tearDown(self):
        pass

    def testSystem(self):
        try:
            System()
        except Throwable:
            pass

        prop = System.getProperties()
        if self.consoleOutput:
            prop.list(System.out)
            print(System.getProperties().getProperty("java.class.path"))
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
