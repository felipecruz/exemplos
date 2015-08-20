import zipfile

try:
    banco_zip = zipfile.ZipFile("saida.zip")
    banco_zip.extractall(path="banco")
    banco_zip.close()
except FileNotFoundError:
    print("Arquivo inexistente")
except PermissionError as pme:
    print("Erro de permissao")

