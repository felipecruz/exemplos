import zipfile

try:
    banco_zip = zipfile.ZipFile("saidax.zip")
    banco_zip.extractall(path="banco")
    banco_zip.close()
except OSError as ose:
    print("Algum problema ao ler o arquivo {}".format(ose.filename))

