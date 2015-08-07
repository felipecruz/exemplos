class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._data = []

    def add_column(self, name, kind, description):
        column = Column(name, kind, description)
        self._columns.append(column)
        return column
