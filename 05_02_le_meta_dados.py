import os

def main():
    meta = {}
    for meta_data_file in os.listdir("data/meta-data"):
        table_name = meta_data_file.split('.')[0]
        print(table_name)

    for key, val in meta.items():
        print("Tabela {}".format(key))
        print(" Attributes: ")
        for col in val:
            print("  {}: {}".format(col[1], col[0]))


if __name__ == "__main__":
    main()

