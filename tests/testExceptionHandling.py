# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 20.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import unittest
from java.lang.Exception import JException
from java.lang.IllegalArgumentException import IllegalArgumentException
from java.lang.IllegalCallerException import IllegalCallerException
from java.lang.RuntimeException import RuntimeException
from java.lang.Throwable import Throwable
from java.lang.UnsupportedOperationException \
     import UnsupportedOperationException
from java.io.IOException import IOException

from java.python.lang.IllegalInstantiationException \
     import IllegalInstantiationException


class TestExceptions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMessageStore(self):
        testMessage = "Not yet implemented!"
        notYetImplemented = UnsupportedOperationException(testMessage)
        self.assertEqual(testMessage,
                         notYetImplemented.getMessage(),
                         "Message isn't store in base class" +
                         " java.lang.Throwable")

    def testExtendedInstantition(self):
        instance = IllegalInstantiationException()
        self.assertEqual("private constructor call",
                         instance.getMessage(),
                         "Unexpected message")
        IllegalInstantiationException(message="msg")
        IllegalInstantiationException(cause=Throwable())
        IllegalInstantiationException(message="msg", cause=Throwable())

    def testJavaInstantition(self):
        JException()
        JException(message="msg")
        JException(cause=Throwable())
        JException(message="msg", cause=Throwable())

        IllegalArgumentException()
        IllegalArgumentException(message="msg")
        IllegalArgumentException(cause=Throwable())
        IllegalArgumentException(message="msg", cause=Throwable())

        IllegalCallerException()
        IllegalCallerException(message="msg")
        IllegalCallerException(cause=Throwable())
        IllegalCallerException(message="msg", cause=Throwable())

        IOException()
        IOException(message="msg")
        IOException(cause=Throwable())
        IOException(message="msg", cause=Throwable())

        RuntimeException()
        RuntimeException(message="msg")
        RuntimeException(cause=Throwable())
        RuntimeException(message="msg", cause=Throwable())

        Throwable()
        Throwable(message="msg")
        Throwable(cause=Throwable())
        Throwable(message="msg", cause=Throwable())

        UnsupportedOperationException()
        UnsupportedOperationException(message="msg")
        UnsupportedOperationException(cause=Throwable())
        UnsupportedOperationException(message="msg", cause=Throwable())

        pass


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
