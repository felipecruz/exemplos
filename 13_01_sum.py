# coding: utf-8
from decimal import Decimal

total = Decimal('0')

def dec(element, index):
    try:
        return Decimal(element[index])
    except:
        return Decimal('0')

with open('data/data/ExecucaoFinanceira.csv', 'r') as data:
    splited_data = [line.split(';') for line in data]
    total = sum([dec(element, 5) for element in splited_data])

print("Total gasto: {}".format(total))

