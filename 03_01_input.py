salario = int(input('Salario? '))
imposto = float(input('Imposto em % (ex: 27.5)? '))
print("Valor real: {0}".format(salario - (salario * (imposto * 0.01))))
