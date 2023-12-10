#!/usr/bin/python3

"""Unnitest for console
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models import storage


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.console.preloop()

    def tearDown(self):
        self.console.postloop()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, command):
        self.console.onecmd(command)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_create_command(self):
        expected_output = "f1r57-1n574nc3\n"
        self.assert_stdout(expected_output, "create BaseModel")

    def test_show_command(self):
        storage.reset()
        obj = BaseModel()
        expected_output = str(obj) + '\n'
        self.assert_stdout(expected_output, "show BaseModel {}".format(obj.id))

    def test_destroy_command(self):
        storage.reset()
        obj = BaseModel()
        self.assert_stdout("", "destroy BaseModel {}".format(obj.id))
        self.assertNotIn(obj, storage.all().values())

    def test_all_command(self):
        storage.reset()
        obj1 = BaseModel()
        obj2 = BaseModel()
        expected_output = "[{}, {}]\n".format(str(obj1), str(obj2))
        self.assert_stdout(expected_output, "all BaseModel")

    def test_update_command(self):
        storage.reset()
        obj = BaseModel()
        self.assert_stdout("", "update BaseModel {} name \"New Name\"".format(obj.id))
        updated_obj = storage.all()[obj.__class__.__name__ + '.' + obj.id]
        self.assertEqual(updated_obj.name, "New Name")


if __name__ == '__main__':
    unittest.main()
