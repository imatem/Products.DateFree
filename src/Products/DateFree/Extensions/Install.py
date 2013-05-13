# This Python file uses the following encoding: utf-8

"""
$Id: Install.py 375 2011-02-11 04:30:11Z hvelarde $
"""

from Products.CMFCore.utils import getToolByName

from Products.DateFree.config import DEPENDENCIES


def install_dependencies(site):
    """Install required products"""

    qi = getToolByName(site, 'portal_quickinstaller')
    for product in DEPENDENCIES:
        if not qi.isProductInstalled(product):
            if qi.isProductInstallable(product):
                qi.installProduct(product)
            else:
                raise "Product %s not installable" % product


def install(portal):
    install_dependencies(portal)
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-Products.DateFree:default')
    return


def uninstall(portal):
    return
