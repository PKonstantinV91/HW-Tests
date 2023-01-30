import unittest
from main2 import YaCreateFolder


class TestCreateFolder(unittest.TestCase, YaCreateFolder):

    def test_res200(self):
        res = YaCreateFolder().create_folder("TesT")
        self.assertEqual(res, 200)

    @unittest.expectedFailure
    def test_folder_exist(self):
        res = YaCreateFolder().create_folder("TesT")
        self.assertEqual(res, 409)