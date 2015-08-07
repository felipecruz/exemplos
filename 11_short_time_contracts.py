from decimal import Decimal
from datetime import datetime

total = Decimal('0')
start_date = datetime(2014, 1, 1)

def get_value(info):
    try:
        start_str_date = info[8]
        end_str_date = info[9]
        start_date = datetime.strptime(start_str_date, '%d/%m/%Y')
        end_date = datetime.strptime(end_str_date, '%d/%m/%Y')
        date_diff = end_date - start_date
        if date_diff.days < 10:
            str_value = info[5]
            value = Decimal(str_value)
            return value
    except Exception as e:
        print(info)
        pass
    return Decimal('0')

with open('data/data/ExecucaoFinanceira.csv', 'r') as data:
    for line in data:
        total += get_value(line.strip().split(';'))

print("Total gasto com contrados de menos de 11 dias {}"
    .format(total))
