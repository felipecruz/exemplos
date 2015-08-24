import unittest

from domain import DataTable

class DataTableTest2(unittest.TestCase):
    def setUp(self):
        self.table = DataTable('A')

    def test_add_column(self):
        self.assertEqual(0, len(self.table._columns))

        self.table.add_column('BId', 'bigint')
        self.assertEqual(1, len(self.table._columns))

        self.table.add_column('value', 'numeric')
        self.assertEqual(2, len(self.table._columns))

        self.table.add_column('desc', 'varchar')
        self.assertEqual(3, len(self.table._columns))

    def test_add_column_invalid_type(self):
        self.assertRaises(Exception, self.table.add_column,
                                     ('col', 'invalid'))

    def test_add_column_invalid_type_fail(self):
        a_table = DataTable('A')
        error = False

        try:
            a_table.add_column('col', 'invalid')
        except:
            error = True

        if not error:
            self.fail("Chamada não gerou erro mas deveria")

    def test_add_relationship(self):
        a_table = DataTable('A')
        col = a_table.add_column('BId', 'bigint')
        b_table = DataTable('B')
        b_table.add_column('BId', 'bigint')
        a_table.add_references('B', b_table, col)

        self.assertEqual(1, len(a_table.references))
        self.assertEqual(0, len(a_table.referenced))

    def test_add_reverse_relationship(self):
        a_table = DataTable('A')
        col = a_table.add_column('BId', 'bigint')
        b_table = DataTable('B')
        col = b_table.add_column('BId', 'bigint')
        b_table.add_referenced('A', a_table, col)

        self.assertEqual(1, len(b_table.referenced))
        self.assertEqual(0, len(b_table.references))

