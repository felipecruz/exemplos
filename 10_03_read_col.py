with open('data/data/ExecucaoFinanceira.csv', 'r') as data:
    for line in data:
        print(line.split(';')[5])
