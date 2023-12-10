#!/usr/bin/python3

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up a clean slate for each test."""
        storage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after each test."""
        storage._FileStorage__file_path = "file.json"
        storage._FileStorage__objects = {}

    def assert_stdout(self, command, expected_output):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().onecmd(command)
            self.assertIn(expected_output, mock_stdout.getvalue())

    def test_create_command(self):
        self.assert_stdout("create BaseModel", "BaseModel")

    def test_show_command(self):
        storage._FileStorage__objects['BaseModel.1'] = BaseModel()
        self.assert_stdout("show BaseModel 1", "BaseModel")

    def test_destroy_command(self):
        storage._FileStorage__objects['BaseModel.1'] = BaseModel()
        self.assert_stdout("destroy BaseModel 1", "")

    def test_all_command(self):
        storage._FileStorage__objects['BaseModel.1'] = BaseModel()
        self.assert_stdout("all BaseModel", "BaseModel")

    def test_update_command(self):
        storage._FileStorage__objects['BaseModel.1'] = BaseModel()
        self.assert_stdout("update BaseModel 1 name 'NewName'", "")

    def test_custom_command(self):
        storage._FileStorage__objects['BaseModel.1'] = BaseModel()
        self.assert_stdout("BaseModel.show(1)", "BaseModel")

    def test_invalid_command(self):
        self.assert_stdout("invalidCommand", "Unrecognized command:")

    def test_emptyline_command(self):
        self.assert_stdout("", "")

    def test_EOF_command(self):
        with self.assertRaises(SystemExit):
            self.assert_stdout("EOF", "")

if __name__ == '__main__':
    unittest.main()