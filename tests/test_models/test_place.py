#!/usr/bin/python3
""" """
from models.place import Place
from tests.test_models.test_base_model import test_basemodel


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_user_id(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.user_id), str)

    def test_city_id(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.city_id), str)

    def test_description(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.description), str)

    def test_name(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.name), str)

    def test_number_rooms(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.number_rooms), int)

    def test_max_guest(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.max_guest), int)

    def test_price_by_night(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.price_by_night), int)

    def test_number_bathrooms(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.number_bathrooms), int)

    def test_latitude(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.latitude), float)

    def test_amenity_ids(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.amenity_ids), list)

    def test_longitude(self):
        """ """
        newobj = self.value()
        self.assertEqual(type(newobj.latitude), float)

