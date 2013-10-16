# -*- coding: utf-8 -*-
from Products.Archetypes import atapi
from Products.Archetypes.Registry import registerField
from Products.Archetypes.Registry import registerWidget
from Products.Archetypes.Widget import TypesWidget
from Products.Archetypes.atapi import DisplayList
from Products.CompoundField.CompoundWidget import CompoundWidget
from Products.CompoundField.CompoundField import CompoundField
from DateTime import DateTime
from datetime import date
from Products.DateFree import DateFreeMessageFactory as _
from Products.DateFree.validators import DateFreeValidator

emptyYear='----'
emptyMonthDay='--'

YEAR_VOCABULARY = [emptyYear] + map(str,range(date.today().year + 5, 1939, -1))
MONTH_VOCABULARY = DisplayList(((emptyMonthDay, emptyMonthDay),
      ('1', 'Enero'), ('2', 'Febrero'),\
      ('3', 'Marzo'), ('4', 'Abril'), ('5', 'Mayo'), ('6', 'Junio'),\
      ('7', 'Julio'), ('8', 'Agosto'), ('9', 'Septiembre'), ('10', 'Octubre'),\
      ('11', 'Noviembre'), ('12', 'Diciembre')))
DAY_VOCABULARY = [emptyMonthDay] + map(str, range(1, 32))


def test(x, y, z):
    if x:
        return y
    return z


def getLastDay(year, month):
    # fecha=DateTime(year, month, 1)
    mes=month%12+1
    nextMonth=DateTime(year, mes, 1)
    return nextMonth-1


def getFirstDay(year, month):
    return DateTime(year, month, 1)


schema = atapi.Schema((
    atapi.StringField('Year',
        widget=atapi.StringWidget(
            label=_(u"Año"),
            # description=_(u"Field description"),
            size=4,
            maxlength=4,
        ),
        vocabulary=YEAR_VOCABULARY,
    ),

    atapi.StringField('Month',
        widget=atapi.StringWidget(
            label=_(u"Mes"),
            size=2,
            maxlength=2,
        ),
        vocabulary=MONTH_VOCABULARY,
    ),

    atapi.StringField('Day',
        widget=atapi.StringWidget(
            label=_(u"Día"),
            size=2,
            maxlength=2,
         ),
        vocabulary=DAY_VOCABULARY,
    ),
))


class DateFreeField(CompoundField):
    """
    """
    _properties = CompoundField._properties.copy()
    _properties.update({
        'type': 'datefreefield',
        'validators': DateFreeValidator(),
    })

    schema = schema

    def getDate(self, instance, name):
        valor=self.getRaw(instance)
        nname=name[-3:]
        res=None
        for key in valor.keys():
            if key.find(nname) >=0:
                res = valor.get(key, emptyMonthDay)
                break
        return res != emptyYear and res or ""

    def setDate(self, instance, year='----', month='--', day='--'):
        self.set(instance, {'Year': year, 'Month': month, 'Day': day})

    def getDictDate(self, instance):
        valor=self.getRaw(instance)
        nDic={}
        for key in valor.keys():
            try:
                nDic[key]=int(valor[key].replace(emptyMonthDay, '0'))
            except:
                nDic[key]=0
        return nDic

    def getFormattedDate(self, instance):
        ''' return string representation in format dd/mm/yyyy
        '''
        value = self.getRaw(instance)
        return ('%02s/%02s/%04s' % (value['Day'],
                    value['Month'], value['Year'])).replace(' ', '0')

    def getValueExistDate(self, instance):
        valor=self.getRaw(instance)
        Year=Month=Day=""
        for key in valor.keys():
            if key == 'Year':
                Year=valor[key].rjust(4).replace(' ', '0').replace('0000', '').replace('----', '')
            elif key == 'Month':
                Month=valor[key].rjust(2).replace(' ', '0').replace('00', '').replace('--', '')
            elif key == 'Day':
                Day=valor[key].rjust(2).replace(' ', '0').replace('00', '').replace('--', '')
        dateExist=""
        if Day != "":
            dateExist=Day
            dateExist+='/'
            if Month == "":
                dateExist+='/'
        if Month != "":
            dateExist+=Month
            dateExist+='/'
        dateExist+=Year
        return dateExist

    def emptyDate(self, instance):
        valor=self.getRaw(instance)
        for key in valor.keys():
            if valor[key]!=emptyMonthDay and valor[key]!='0':
                return False
        return True

    def getDateTime(self, instancia, minimo=True):
        dictFecha=self.getDictDate(instancia)
        year=dictFecha['Year'] or minimo and 1000 or 9999
        month=test(dictFecha['Month'], dictFecha['Month'], (minimo and 1) or 12)
        day=test(dictFecha['Day'], dictFecha['Day'], (minimo and 1) or 31)
        try:
            fecha=DateTime(year, month, day)
        except:
            if month<1 or month>12:
                if minimo:
                    month=1
                else:
                    month=12
            try:
                fecha=DateTime(year, month, day)
            except:
                fecha=test(minimo, getFirstDay(year, month), getLastDay(year, month))
        return fecha

registerField(DateFreeField,
    title='DateFreeField',
    description=('Almacena fechas en un diccionario sin ser obligatorios el año, mes y día.'),
)


class DateFreeWidget(CompoundWidget):
    _properties=TypesWidget._properties.copy()
    _properties.update({
        'macro': 'template_datefree',
    })

registerWidget(DateFreeWidget,
    title='DateFreeWidget',
    description=('Widget for display date on dateFreeField type format'),
    used_for=('Products.Archetypes.Field.StringField', ),
)
