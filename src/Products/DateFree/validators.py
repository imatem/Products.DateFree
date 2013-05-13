# -*- coding: utf-8 -*-
import re
from Products.validation.interfaces.IValidator import IValidator
from Products.CompoundField.validators import CompoundValidator


class DateFreeValidator(CompoundValidator):
    """ Validator for DateFreeField
    """

    # __implements__ = (IValidator, )

    name = 'datefreefieldvalidator'

    # def __init__(self, errormsg=None):
    #     self.errormsg = errormsg
    # 
    # def __call__(self, value, instance, errors, field, REQUEST=None,
    #             *args, **kwargs):
    #     patternYear=re.compile(r'Year\Z')
    #     #patternMonth=re.compile(r'Month\Z')
    #     #patternDay=re.compile(r'Day\Z')
    #     patternNumber=re.compile(r'\d+')
    #     #instancia=kwargs.get('instance',None)
    #     campo=kwargs.get('field', None)
    #     Year=Month=Day=0
    #     for key in value.keys():
    #         if campo and campo.required:
    #             if patternYear.search(key):
    #                 val= value[key]
    #                 if not(val) or not(patternNumber.search(val[0])):
    #                     return("Es obligatorio que proporcione el año")
    #     return 1
