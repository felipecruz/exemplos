class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._data = []

class Column:
    def __init__(self, name, kind, description):
        self._name = name
        self._kind = kind
        self._description = description
