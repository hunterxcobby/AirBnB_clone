#!/usr/bin/python3

'''
This module is a test file used to test the BaseModel class of our AirBnB_clone project
'''


# python's path

# modules that will be used here

import unittest
from models.base_model import BaseModel

# helper functions

def is_string(value):
    ''' return true if value is string '''
    return isinstance(value, str)

# Test Cases

class TestBaseModel(unittest.TestCase):
    '''
    This is a test case that is testing all cases in the BaseModel class of our project
    '''

    # testing uuid of every instance

    def test_uuid(self):
        ''' uuids must be equal no matter what '''
        obj1 = BaseModel()
        obj2 = BaseModel()

        # uuids are string
        self.assertTrue(is_string(obj1.id))
        self.assertTrue(is_string(obj2.id))

        # differenct uuids
        self.assertNotEqual(obj1, obj2)
