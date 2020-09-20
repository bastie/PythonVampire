'''
Created on 20.09.2020

@author: admin
'''
import unittest
from java.lang.Exception import JException
from java.lang.IllegalArgumentException import IllegalArgumentException
from java.lang.RuntimeException import RuntimeException
from java.lang.Throwable import Throwable
from java.lang.UnsupportedOperationException import UnsupportedOperationException


class TestExceptionHandling(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass

    def testMessageStore(self):
        testMessage = "Not yet implemented!"
        notYetImplemented = UnsupportedOperationException(testMessage)
        self.assertEqual("testMessage", notYetImplemented.getMessage(), "Message isn't store in base class java.lang.Throwable")

    def testInstantition(self):
        JException()
        JException(message="msg")
        JException(cause=Throwable())
        JException(message="msg",cause=Throwable())
        
        IllegalArgumentException()
        IllegalArgumentException(message="msg")
        IllegalArgumentException(cause=Throwable())
        IllegalArgumentException(message="msg",cause=Throwable())
        
        RuntimeException()
        RuntimeException(message="msg")
        RuntimeException(cause=Throwable())
        RuntimeException(message="msg",cause=Throwable())
        
        Throwable()
        Throwable(message="msg")
        Throwable(cause=Throwable())
        Throwable(message="msg",cause=Throwable())
        
        UnsupportedOperationException()
        UnsupportedOperationException(message="msg")
        UnsupportedOperationException(cause=Throwable())
        UnsupportedOperationException(message="msg",cause=Throwable())
        
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()