# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 05.10.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import unittest
from java.lang.System import System
from java.util.Properties import Properties


class testUtilPackage(unittest.TestCase):

    consoleOutput = False

    def setUp(self):
        self.consoleOutput = False
        pass

    def tearDown(self):
        pass

    def testProperties(self):
        props = Properties()

        oldValue = props.setProperty("key", "oldValue")
        self.assertEqual(None, oldValue,
                         "Properties does not store the expected value")
        oldValue = props.setProperty("key", "newValue")
        self.assertEqual("oldValue", oldValue,
                         "Properties does not store the expected value")

        newValue = props.getProperty("key")
        self.assertEqual("newValue", newValue,
                         "Properties does not store the expected value")

        props.setProperty("tooLongText",
                          "Please visit the project site "
                          + "https://bastie.github.io/PythonVampire/")
        if self.consoleOutput:
            props.list(System.out)
        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
