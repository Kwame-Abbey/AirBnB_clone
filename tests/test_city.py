#!/usr/bin/python3
"""Unittest for City"""
import unittest
from unittest.mock import patch
from datetime import datetime
from models import storage
from models.city import City
from models.base_model import BaseModel



class TestCity(unittest.TestCase):
    """Test cases for City class"""

    # BASIC TESTS
    def test_state_id(self):
        """checks for class attribute state_id"""
        city = City()
        self.assertEqual(city.state_id, "")

    def test_name(self):
        """checks for name clase attribute"""
        city = City()
        self.assertEqual(city.name, "")

    def test_instance_hasattr(self):
        """Tests if an instance has attributes"""
        obj = City()

        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_BaseModel_subclass(self):
        """test if object is an instance of BaseModel"""
        obj = City()
        self.assertIsInstance(obj, BaseModel)

    def test_class_instance(self):
        """test if object is an instance of BaseModel & City"""
        obj = City()
        self.assertIsInstance(obj, City)

    def test_str_representation(self):
        """Test the __str__ method"""
        city = City(name='TestCity', id="7q")
        expected_str = f"[City] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str)

    def test_to_dict_method(self):
        """Test Case for to_dict method"""
        _id = "7q795"
        _created_at = "2023-12-07T09:49:07.936066"
        _updated_at = "2023-12-07T09:49:07.936176"
        _state_id = "new state"
        _name = "the city"

        obj = City(
            id=_id, created_at=_created_at, updated_at=_updated_at,
            state_id = _state_id, name = _name)
        obj_dict = obj.to_dict()
        dictionary = {
            'id': '7q795', 'created_at': "2023-12-07T09:49:07.936066",
            'updated_at': "2023-12-07T09:49:07.936176",
            '__class__': "City",
            'state_id': "new state", 'name': "the city",
            }
        self.assertEqual(dictionary, obj_dict)

    # ATTRIBUTES TESTS
    def test_with_args_id(self):
        """Test with specific args"""
        _id = "7q795"
        obj = City(id=_id)
        self.assertEqual(obj.id, _id)

    def test_with_args_created_at(self):
        """Test with specific created at time"""
        _created_at = "2023-12-07T09:49:07.936066"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_c_at = datetime.strptime(_created_at, d_format)
        obj = City(created_at=_created_at)
        self.assertEqual(obj.created_at, obj_c_at)

    def test_with_args_updated_at(self):
        """Test with specific updated at time"""
        _updated_at = "2023-12-07T09:49:07.936066"
        d_format = "%Y-%m-%dT%H:%M:%S.%f"
        obj_u_at = datetime.strptime(_updated_at, d_format)
        obj = City(created_at=_updated_at)
        self.assertEqual(obj.created_at, obj_u_at)
    
    def test_with_args_state_id(self):
        """Test with specific state id"""
        _state_id = "oldState"
        obj = City(state_id=_state_id)
        self.assertEqual(obj.state_id, _state_id)

    def test_with_args_name(self):
        """Test with specific name"""
        _name = "TestCity"
        obj = City(name=_name)
        self.assertEqual(obj.name, _name)

    def test_instance_has_class_attr(self):
        """Tests if an instance has class attributes"""
        obj = City()
        self.assertTrue(hasattr(obj, 'state_id'))
        self.assertTrue(hasattr(obj, 'name'))

    # FileStorage Tests
    @patch('models.storage.save')
    def test_save_method_updates_storage(self, mock_save):
        """Test whether models.storage.save is called and updates the storage"""
        city = City()
        original_updated_at = city.updated_at
        city.name = 'NewCityName'
        city.save()
        mock_save.assert_called_once()
        self.assertNotEqual(original_updated_at, city.updated_at)

    @patch('models.storage.new')  # helps to mock the new method
    def test_new_method_called_on_instance_creation(self, mock_new):
        """Test whether models.storage.new
        is called when creating an instance
        """
        obj = City()
        mock_new.assert_called_once_with(obj)

if __name__ == '__main__':
    unittest.main()