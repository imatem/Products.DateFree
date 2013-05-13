# This Python file uses the following encoding: utf-8

"""
$Id$
"""

import unittest

from Products.DateFree.config import DEPENDENCIES
from Products.DateFree.config import PROJECTNAME
from Products.DateFree.tests.base import TestCase


class TestInstall(TestCase):
    """ensure product is properly installed"""

    def afterSetUp(self):
        """"""

    def test_skins(self):
        portal_skins = self.portal.portal_skins
        self.failUnless('DateFree' in portal_skins.objectIds())

    def test_dependencies_installed(self):
        portal_quickinstaller = self.portal.portal_quickinstaller
        for p in DEPENDENCIES:
            self.failUnless(portal_quickinstaller.isProductInstalled(p),
                            '%s not installed' % p)


class TestUninstall(TestCase):
    """ensure product is properly uninstalled"""

    def afterSetUp(self):
        self.qi = getattr(self.portal, 'portal_quickinstaller')
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_product_uninstalled(self):
        self.failIf(self.qi.isProductInstalled(PROJECTNAME))

    def test_skins(self):
        self.failIf('DateFree' in self.portal.portal_skins.objectIds())


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestInstall))
    suite.addTest(unittest.makeSuite(TestUninstall))
    return suite
