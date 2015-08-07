from decimal import Decimal

class Column:
    def __init__(self, name, kind, description=""):
        self._name = name
        self._kind = kind
        self._description = description

    def __str__(self):
        return "Col: {} : {} {}".format(self._name,
                                        self._kind,
                                        self._description)

    def validate(self, data):
        if self._kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif self._kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif self._kind == 'numeric':
            try:
                val = Decimal(data)
            except:
                return False
            return True

