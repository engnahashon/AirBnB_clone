#!/usr/bin/python3
import unittest
from datetime import datetime, timedelta
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Setup a new instance of the BaseModel for each test case"""
        self.model = BaseModel()

    def test_id(self):
        """Test that a new instance has a unique id"""
        self.assertIsInstance(self.model.id, str)
        self.assertNotEqual(self.model.id, BaseModel().id)

    def test_created_at(self):
        """Test that created_at is set correctly"""
        now = datetime.utcnow()
        self.assertLessEqual(self.model.created_at, now)
        self.assertGreaterEqual(self.model.created_at, now - timedelta(seconds=1))

    def test_updated_at(self):
        """Test that updated_at is set correctly"""
        now = datetime.utcnow()
        self.assertLessEqual(self.model.updated_at, now)
        self.assertGreaterEqual(self.model.updated_at, now - timedelta(seconds=1))

    def test_save(self):
        """Test that save updates the updated_at attribute"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test that to_dict returns a dictionary with correct attributes"""
        dict_representation = self.model.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertEqual(dict_representation['__class__'], 'BaseModel')
        self.assertIsInstance(dict_representation['created_at'], str)
        self.assertIsInstance(dict_representation['updated_at'], str)
        self.assertEqual(dict_representation['created_at'], self.model.created_at.isoformat())
        self.assertEqual(dict_representation['updated_at'], self.model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()

