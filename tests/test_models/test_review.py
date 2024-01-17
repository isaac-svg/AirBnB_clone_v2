#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_text(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.text), str)

    def test_place_id(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.place_id), str)

    def test_user_id(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.user_id), str)

