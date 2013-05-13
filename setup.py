from setuptools import setup, find_packages

version = '1.0'

setup(
    name='Products.DateFree',
    version=version,
    description="Products.DateFree",
    long_description=open("README.txt").read() + "\n" +
    open('docs/HISTORY.txt').read(),
    # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers,
    #http://www.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Plone',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    platforms='Any',
    author='Marco Rabadan',
    author_email='',
    url='http://www.matem.unam.mx',
    license='GPL',
    namespace_packages=['Products'],
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Products.CompoundField',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
