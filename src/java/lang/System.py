# SPDX-FileCopyrightText: 2020 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: Apache-2.0

'''
Created on 01.09.2020

@author: Sͬeͥbͭaͭsͤtͬian
'''
import sys
import os
import platform
import getpass
import locale
import tempfile

from java.lang.Object import Object
from java.python.lang.ConsoleOutputPrintStream \
    import ConsoleOutputPrintStream
from java.util.Properties import Properties

from java.python.lang.IllegalInstantiationException \
    import IllegalInstantiationException


class System(Object):
    '''
    classdocs
    '''

    systemProperties = None

    out = ConsoleOutputPrintStream()
    '''
    Delegate object
    '''

    def __init__(self):
        '''
        private Constructor
        '''
        raise IllegalInstantiationException(
            message="java.lang.System is not instantiable")

    @classmethod
    def exit(self, status: int):
        sys.exit(status)

    @classmethod
    def getProperties(self) -> Properties:
        if None is System.systemProperties:
            System.systemProperties = Properties()

            # Java specific environment
            System.systemProperties.setProperty(
                "java.vendor", "Sebastian Ritter")
            System.systemProperties.setProperty(
                "java.vendor.url", "https://bastie.github.io/PythonVampire/")
            System.systemProperties.setProperty(
                "java.version", "0.3.0")
            System.systemProperties.setProperty(
                "file.separator", os.path.sep)
            System.systemProperties.setProperty(
                "path.separator", os.pathsep)
            System.systemProperties.setProperty(
                "line.separator", os.linesep)
            classpath = ""
            for file in sys.path:
                if len(file) > 0:
                    classpath += file
                    + System.systemProperties.getProperty("path.separator")
            if 0 < len(classpath):
                classpath = classpath[:-1]
                # remove last added path separator if not empty
            System.systemProperties.setProperty(
                "java.class.path", classpath)
            System.systemProperties.setProperty(
                "file.encoding", sys.getfilesystemencoding())
            System.systemProperties.setProperty(
                "os.name", platform.system())
            if "Darwin" == System.systemProperties.getProperty("os.name"):
                System.systemProperties.setProperty(
                    "os.name", "macOS")
                System.systemProperties.setProperty(
                    "os.version", platform.mac_ver()[0])
            else:
                System.systemProperties.setProperty(
                    "os.version", platform.release())
            System.systemProperties.setProperty(
                "os.arch", platform.machine())
            System.systemProperties.setProperty(
                "user.dir", os.path.expanduser('~'))
            System.systemProperties.setProperty(
                "user.name", getpass.getuser())
            if None is not locale.getdefaultlocale()[0]:  # Python cli result
                System.systemProperties.setProperty(
                    "user.country",  locale.getdefaultlocale()[0][3:])
                System.systemProperties.setProperty(
                    "user.language", locale.getdefaultlocale()[0][:2])
            else:  # PyDev IDE result
                System.systemProperties.setProperty("user.country",
                                                    "")
                System.systemProperties.setProperty("user.language",
                                                    "")

            # TODO: implement Java 17 module base!
            System.systemProperties.setProperty("java.runtime.version",
                                                "17")
            System.systemProperties.setProperty("java.runtime.name",
                                                "Vampire Runtime Environment")
            # IO properties
            # next using in logging FileHandler
            System.systemProperties.setProperty("java.io.tmpdir",
                                                tempfile.gettempdir())
        return System.systemProperties


'''
string encoding #sys.getdefaultencoding() => utf-8

// store some Java system specific environment
prop.Add("user.timezone", null); // content???
prop.Add("user.variant", null); // content???
// Java net environment
prop.Add("java.protocol.handler.pkgs", "biz.ritter.net.protocol|");
// GUI specific environment
prop.Add("awt.toolkit", "biz.ritter.awt.forms.FormsToolkit");
// Sax specific environment
prop.Add("org.xml.sax.parser", null);
// include the class for the default SAX Parser
//for example: org.apache.xerces.parsers.SaxParser
// Logging properties (see java.util.logging.LogManager)
prop.Add("java.util.logging.config.class", null);
prop.Add("java.util.logging.config.file", null);
prop.Add("java.util.logging.manager", null);
//Security properties - see java.security package
prop.Add("java.security.properties", null);
// Preferences properties
prop.Add("java.util.prefs.PreferencesFactory", null);
// JDBC properties
prop.Add("jdbc.drivers", null);
// Apache properties
prop.Add("org.apache.xml.namespace.QName.
    useCompatibleSerialVersionUID", null);
// ICU properties
prop.Add("ICUDebug", null);
// com.sun properties
prop.Add("com.sun.management.jmxremote.port", null);
prop.Add("com.sun.management.jmxremote.rmi.port", null);
prop.Add("com.sun.management.jmxremote.local.port", null);
// Java 15
prop.Add("jdk.tls.client.SignatureSchemes", null);
prop.Add("jdk.tls.server.SignatureSchemes", null);
prop.Add("jdk.tls.client.enableCAExtension", "false");
prop.Add("jdk.sunec.disableNative", "true");
// Networking:
https://docs.oracle.com/en/java/javase/14/docs/api/
java.base/java/net/doc-files/net-properties.html
prop.Add("java.net.preferIPv4Stack", "false");
prop.Add("java.net.preferIPv6Addresses", "false");
prop.Add("jdk.net.hosts.file", null);
// see https://www.oracle.com/java/technologies/javase/15-relnote-issues.html

// own important environment
'''
