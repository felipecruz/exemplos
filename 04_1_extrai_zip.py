# coding: utf-8

import os
import zipfile
import sys


def main(path):
    if not os.path.exists(path):
        print("Arquivo {} não existe".format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print("Arquivos extraídos")


if __name__ == "__main__":
    main(sys.argv[1])
