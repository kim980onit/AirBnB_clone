#!/usr/bin/python3
"""Module for testing BaseModel class.
"""


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class for testing BaseModel class.
    """
    def test_init(self):
        """Tests init."""
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save(self):
        """Tests save."""
        my_model = BaseModel()
        updated_at_before = my_model.updated_at
        updated_at_after = my_model.save()

        self.assertNotEqual(updated_at_before, updated_at_after)

    def test_to_dict(self):
        """Tests to_dict."""
        my_model = BaseModel()
        Mdict = my_model.to_dict()

        self.assertIsInstance(Mdict, dict)
        self.assertEqual(Mdict["__class__"], 'BaseModel')
        self.assertEqual(Mdict['id'], my_model.id)
        self.assertEqual(Mdict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(Mdict['updated_at'], my_model.updated_at.isoformat())

    def test_str(self):
        """Tests str."""
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))
        self.assertIn(my_model.id, str(my_model))
        self.assertIn(str(my_model.__dict__), str(my_model))

    def test_uuid(self):
        """Tests uuid.
        """
        self.assertNotEqual(self.base1.id, self.base2.id)
        self.assertTrue(hasattr(self.base1, "id"))
        self.assertEqual(type(self.base1.id), str)
        self.assertEqual(type(self.base2.id), str)


if __name__ == '__main__':
    unittest.main()