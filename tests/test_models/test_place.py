#!/usr/bin/python3
'''Define unittests'''
from model.city import City
from tests.test_model.test_base_model import test_basemodel

class test_Place(test_basemodel):
    ''' '''

    def __init__(self, *args, **kwargs):
        '''  '''
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = "Place"

    def test_city_id(self):
        '''  '''
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.number_roome), int)

    def test_number_bathrooms(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.price_by_nigh), int)

    def test_latitude(self):
        '''  '''
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        '''   '''
        new = self.value()
        self.assertEqual(type(new.longitude), float)

    def test_amenity_ids(self):
        ''' '''
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list
