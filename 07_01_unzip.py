import zipfile

banco_zip = zipfile.ZipFile("saida.zip")
banco_zip.extractall(path="banco")
banco_zip.close()
