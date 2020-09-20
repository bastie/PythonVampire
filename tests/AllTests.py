# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 20.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import unittest
import os
import glob


class AllTests(unittest.TestCase):
    '''
    Very simple unit test class to all all test cases in same directory
    with filename pattern ''test*.py''.
    It is using dynamic module load.
    '''

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.testModules = [os.path.splitext(filename)[0]
                            for filename in glob.glob("test*.py")]

    def testAll(self):
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()

        # add tests
        for modulName in self.testModules:
            modul = __import__(modulName)
            suite.addTests(loader.loadTestsFromModule(modul))

        # run it
        runner = unittest.TextTestRunner(verbosity=2)
        runner.run(suite)
    pass
