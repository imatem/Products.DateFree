# -*- coding: utf-8 -*-
# import re
# from Products.validation.interfaces.IValidator import IValidator
from Products.CompoundField.validators import CompoundValidator

# from Products.validation.interfaces.IValidator import IValidator
# from zope.interface import implements
from UNAM.imateCVct import _
from DateTime import DateTime
from DateTime.interfaces import DateError
from zope.i18n import translate
# from zope.i18nmessageid import Message
# import re


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

    # def _getSubfields(self, field, form):
    #     import pdb; pdb.set_trace()
    #     return field.Schema().fields()

    def __call__(self, value, instance, errors, field, REQUEST=None,
                 *args, **kwargs):
        if isinstance(value, basestring):
            value = eval(value)
        year = value['Year'][0]
        month = value['Month'][0]
        day = value['Day'][0]

        if year.isdigit() and month.isdigit() and day.isdigit():
            try:
                DateTime(int(year), int(month), int(day))
            except DateError:
                errors[field.getName()] = translate(
                    "Invalid date, please correct.",
                    domain='UNAM.imateCVct',
                    context=REQUEST,
                    default=_("Invalid date, please correct.")
                )
                return errors

        if year.isdigit() and month.isdigit() and (not day.isdigit()):
            try:
                DateTime(int(year), int(month), int('01'))
            except DateError:
                errors[field.getName()] = translate(
                    "Invalid date, please correct.",
                    domain='UNAM.imateCVct',
                    context=REQUEST,
                    default=_("Invalid date, please correct.")
                )
                return errors

        if year.isdigit() and (not month.isdigit()) and day.isdigit():
            errors[field.getName()] = translate(
                "Invalid date, please indicate month.",
                domain='UNAM.imateCVct',
                context=REQUEST,
                default=_("Invalid date, please indicate month.")
            )
            return errors

        if year.isdigit() and (not month.isdigit()) and (not day.isdigit()):
            try:
                DateTime(int(year), int('01'), int('01'))
            except DateError:
                errors[field.getName()] = translate(
                    "Invalid date, please correct.",
                    domain='UNAM.imateCVct',
                    context=REQUEST,
                    default=_("Invalid date, please correct.")
                )
                return errors

        if (not year.isdigit()) and month.isdigit() and day.isdigit():
            errors[field.getName()] = translate(
                "Invalid date, please indicate at least year.",
                domain='UNAM.imateCVct',
                context=REQUEST,
                default=_("Invalid date, please indicate at least year.")
            )
            return errors

        if (not year.isdigit()) and month.isdigit() and (not day.isdigit()):
            errors[field.getName()] = translate(
                "Invalid date, please indicate at least year.",
                domain='UNAM.imateCVct',
                context=REQUEST,
                default=_("Invalid date, please indicate at least year.")
            )
            return errors

        if (not year.isdigit()) and (not month.isdigit()) and day.isdigit():
            errors[field.getName()] = translate(
                "Invalid date, please indicate year and month.",
                domain='UNAM.imateCVct',
                context=REQUEST,
                default=_("Invalid date, please indicate year and month.")
            )
            return errors

        return errors
