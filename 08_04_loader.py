import unittest
import test_column

suite = unittest.TestLoader().loadTestsFromModule(test_column)
unittest.TextTestRunner(verbosity=2).run(suite)
