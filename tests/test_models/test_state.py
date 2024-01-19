#!/usr/bin/python3
"""Test for State Class """
from models.state import State
from tests.test_models.test_base_model import test_basemodel


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ Instantiate"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
