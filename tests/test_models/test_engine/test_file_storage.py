#!/usr/bin/python3
"""Module to test FileStorage class.
"""

import unittest
import os
from models.base_model import BaseModel
from models.engine.file_stroage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Class to test FileStorage."""
    def setUp(self):
        """Tests class setup."""
        self.storage = FileStorage()

    def test_all(self):
        """Tests all."""
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new(self):
        """Tests new."""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Tests save."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Tests reload."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, new_storage.all())


if __name__ == '__main__':
    unittest.main()