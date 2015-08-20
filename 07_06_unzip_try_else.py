import zipfile

try:
    banco_zip = zipfile.ZipFile("saida.zip")
except (FileNotFoundError, PermissionError):
    print("Algum problema ao ler o arquivo")
else:
    banco_zip.extractall(path="banco")

