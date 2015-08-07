class Column:
    def __init__(self, name, kind, description):
        self._name = name
        self._kind = kind
        self._description = description

class PrimaryKey(Column):
    def __init__(self, table, name, kind, description=None):
        super().__init__(name, kind, description=description)
        self._is_pk = True
