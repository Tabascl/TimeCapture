import unittest
import os

from data.Persistence import Persistence

class TestPersistence(unittest.TestCase):
    def setUp(self):
        self.path = 'testing/test.gzip'
        self.per = Persistence(self.path)

    def test_load_save(self):
        data = { 'companies': ['a', 'b', 'c'], 'tasks': ['d', 'e', 'f'] }
        self.per.save(data)
        res = self.per.load()
        self.assertDictEqual(data, res)

    def tearDown(self):
        os.remove(self.path)