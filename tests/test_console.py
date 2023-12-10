#!/usr/bin/python3

import unittest
from unittest.mock import patch
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

    def test_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertIn("BaseModel", f.getvalue())

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("show BaseModel")
            self.assertIn("BaseModel", f.getvalue())

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("destroy BaseModel")
            self.assertNotIn("BaseModel", f.getvalue())

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("all BaseModel")
            self.assertIn("BaseModel", f.getvalue())

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("update BaseModel 1 name 'NewName'")
            self.assertIn("NewName", f.getvalue())

    def test_custom_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("BaseModel.show(1)")
            self.assertIn("BaseModel", f.getvalue())

    def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("invalidCommand")
            self.assertIn("Unrecognized command:", f.getvalue())

if __name__ == '__main__':
    unittest.main()
