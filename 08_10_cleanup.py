import unittest

class DataTableTest(unittest.TestCase):
    def setUp(self):
        self.addCleanup(self.my_cleanup, ('cleanup executado'))
        self.out_file = open()

    def my_cleanup(self, msg):
        print(msg)

    def test_add_column(self):
        pass

    def tearDown(self):
        print("Nunca executado")
