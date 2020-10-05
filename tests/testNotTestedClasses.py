# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 20.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import unittest

from java.io.File import File
from java.io.PrintStream import PrintStream
from java.lang.Object import Object
from java.nio.file.Files import Files
from java.nio.file.FileSystem import FileSystem
from java.nio.file.FileSystems import FileSystems
from java.nio.file.Path import Path
from java.lang.UnsupportedOperationException \
     import UnsupportedOperationException

from java.python.lang.ConsoleOutputPrintStream \
     import ConsoleOutputPrintStream


class TestUntested(unittest.TestCase):
    '''
      If nowhere is tested, here is tested
    '''

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInstantiation(self):
        '''
          test some semantic Python runtime check
        '''
        ConsoleOutputPrintStream()
        File(".")
        try:
            File()
        except UnsupportedOperationException:
            pass
        Files()
        FileSystem()
        FileSystems()
        Object()
        try:
            Path()
        except TypeError:
            pass
        Path("")
        PrintStream()

        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
