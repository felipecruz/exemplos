# coding: utf-8

from decimal import Decimal
from datetime import date

total = Decimal('0')
start_date = date(2009, 1, 1)
end_date = date(2010, 1, 1)

def get_value(info):
    try:
        signature_str_date = info[7]
        year = int(signature_str_date.split('/')[2])
        month = int(signature_str_date.split('/')[1])
        day = int(signature_str_date.split('/')[0])
        signature_date = date(year, month, day)

        if signature_date > start_date and signature_date < end_date:
            str_value = info[5]
            value = Decimal(str_value)
            return value
    except Exception as e:
        print(e)
        pass
    return Decimal('0')

with open('data/data/ExecucaoFinanceira.csv', 'r') as data:
    for line in data:
        total += get_value(line.split(';'))

print("Total gasto com assinaturas entre {} e {} : {}"
    .format(start_date, end_date, total))
