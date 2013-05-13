Introduction
=============

The intention of dateFreeField is to allow selection of partial date.

All dict values must be numbers
    >>> from Products.DateFree import Date
    >>> datefreefield = Date.DateFreeField('datefield')

dateFreeField should fail with 0 input
    >>> datefreefield.setDate(datefreefield, '2010', '--', '1')
    >>> datefreefield.getFormattedDate(datefreefield)
    '01/--/2010'
    >>> datefreefield.setDate(datefreefield, '2010', '4', '--')
    >>> datefreefield.getFormattedDate(datefreefield)
    '--/04/2010'
    >>> datefreefield.setDate(datefreefield, '2010', '11', '13')
    >>> datefreefield.getFormattedDate(datefreefield)
    '13/11/2010'
