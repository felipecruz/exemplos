from decimal import Decimal
from datetime import datetime, timedelta

totals = {2010:0, 2011:0, 2012:0, 2013:0, 2014:0, 2015:0}

def check_signature_interval(info, year_start_date, year_end_date):
    try:
        start_str_date = info[8]
        end_str_date = info[9]
        start_date = datetime.strptime(start_str_date, '%d/%m/%Y')
        end_date = datetime.strptime(end_str_date, '%d/%m/%Y')

        if start_date > year_start_date and start_date < year_end_date:
            return 1
    except Exception as e:
        pass

    return 0

for year in totals.keys():
    start_date = datetime(year, 1, 1)
    end_date = start_date + timedelta(days=365)
    with open('data/data/ExecucaoFinanceira.csv', 'r') as data:
        for line in data:
            totals[year] += check_signature_interval(line.strip().split(';'),
                start_date, end_date)

for year, signed in totals.items():
    print("{} execuções assinadas em {}".format(signed, year))
