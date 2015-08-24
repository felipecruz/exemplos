import decimal
import unittest

class Column:
    def __init__(self, name, kind, description=""):
        self._name = name
        self._kind = kind
        self._description = description

    @staticmethod
    def validate(kind, data):
        if kind == 'bigint':
            if isinstance(data, int):
                return True
            return False
        elif kind == 'varchar':
            if isinstance(data, str):
                return True
            return False
        elif kind == 'numeric':
            try:
                val = decimal.Decimal(data)
            except:
                return False
            return True


class DataTable:
    def __init__(self, name):
        self._name = name
        self._columns = []
        self._references = []
        self._referenced = []
        self._data = []

    def add_column(self, name, kind, description=""):
        self._validate_kind(kind)
        column = Column(name, kind, description=description)
        self._columns.append(column)
        return column

    def _validate_kind(self, kind):
        if not kind in ('bigint', 'numeric', 'varchar'):
            raise Exception("Tipo inválido")


class DataTableTest(unittest.TestCase):
    def test_add_column(self):
        table = DataTable("Test")
        self.assertEqual(0, len(table._columns))

        table.add_column('BId', 'bigint')
        self.assertEqual(1, len(table._columns))

        table.add_column('value', 'numeric')
        self.assertEqual(2, len(table._columns))

        table.add_column('desc', 'varchar')
        self.assertEqual(3, len(table._columns))

    def test_add_column_invalid_type(self):
        a_table = DataTable('A')
        self.assertRaises(Exception,
            a_table.add_column, ('col', 'invalid'))

    def test_add_column_invalid_type_fail(self):
        a_table = DataTable('A')
        error = False

        try:
            a_table.add_column('col', 'invalid')
        except:
            error = True

        if not error:
            self.fail("Chamada não gerou erro, mas deveria")
