#!/usr/bin/python3
"""
    A module that contains the test suite for the BaseModel class

    Unittest classes:
    TestBaseModel_pre_initialization - line
    TestBaseModel_initialization - line
    TestBaseModel_id_attribute - line
    TestBaseModel_created_at_attribute - line
    TestBaseModel_updated_at_attribute - line
    TestBaseModel_save_method - line
    TestBaseModel_to_dict_method - line

"""
import models
import unittest
from datetime import datetime
from time import sleep

from models.base_model import BaseModel


class TestBaseModel_pre_initialization(unittest.TestCase):
    """
        test class for the BaseModel class pre-initialization
    """


    def test_pre_init_has_no_id(self):
        """
            checks that BaseModel class has no
            'id' attribute pre-initialization
        """

        self.assertFalse(hasattr(BaseModel, 'id'))

    def test_pre_init_has_no_created_at(self):
        """
            checks that BaseModel class has no
            'created_at' attribute pre-initialization
        """

        self.assertFalse(hasattr(BaseModel, 'created_at'))

    def test_pre_init_has_no_updated_at(self):
        """
            checks that BaseModel class has no
            'updated_at' attribute pre-initialization
        """

        self.assertFalse(hasattr(BaseModel, 'updated_at'))




class TestBaseModel_initialization(unittest.TestCase):
    """
        test class for the BaseModel class on initialization
    """

    def test_if_BaseModel_instance_has_id(self):
        """
            checks that instance has an 'id' assigned on initialization
        """

        modelInstance = BaseModel()
        self.assertTrue(hasattr(modelInstance, "id"))

    def test_if_BaseModel_instance_has_created_at(self):
        """
            checks that instance has a 'created_at' assigned on initialization
        """

        modelInstance = BaseModel()
        self.assertTrue(hasattr(modelInstance, "created_at"))

    def test_if_BaseModel_instance_has_updated_at(self):
        """
            checks that instance has a 'updated_at' assigned on initialization
        """

        modelInstance = BaseModel()
        self.assertTrue(hasattr(modelInstance, "updated_at"))

    def test_that_created_at_equals_updated_at(self):
        """
            checks that create_at == updated_at on initialization
        """
        modelInstance = BaseModel()
        self.assertEqual(modelInstance.created_at, modelInstance.updated_at)

    def test_when_kwargs_passed_is_empty(self):
        """
            checks that id, created_at and updated_at are automatically
            generated if they're not in kwargs
        """
        my_dict = {}
        modelInstance = BaseModel(**my_dict)
        self.assertTrue(type(modelInstance.id) is str)
        self.assertTrue(type(modelInstance.created_at) is datetime)
        self.assertTrue(type(modelInstance.updated_at) is datetime)

    def test_when_kwargs_passed_is_not_empty(self):
        """
            checks that id, created_at and updated_at are created from kwargs
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat()}
        modelInstance = BaseModel(**my_dict)
        self.assertEqual(modelInstance.id, my_dict["id"])
        self.assertEqual(modelInstance.created_at,
                         datetime.strptime(my_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(modelInstance.updated_at,
                         datetime.strptime(my_dict["updated_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f"))

    def test_when_args_and_kwargs_are_passed(self):
        """
            checks that when args and kwargs are passed,
            BaseModel init ignores args
        """
        dt = datetime.now()
        dt_iso = dt.isoformat()
        modelInstance = BaseModel("1234", id="234", created_at=dt_iso, name="Firdaus")
        self.assertEqual(modelInstance.id, "234")
        self.assertEqual(modelInstance.created_at, dt)
        self.assertEqual(modelInstance.name, "duplebado")

    def test_when_kwargs_passed_is_more_than_default(self):
        """
            checks BaseModel does not break when kwargs contains more than
            the default attributes
        """
        my_dict = {"id": uuid4(), "created_at": datetime.utcnow().isoformat(),
                   "updated_at": datetime.utcnow().isoformat(),
                   "name": "duplebado"}
        modelInstance = BaseModel(**my_dict)
        self.assertTrue(hasattr(modelInstance, "name"))




class TestBaseModel_id_attribute(unittest.TestCase):
    """
        test class for the BaseModel 'id' attribute
    """

    def test_ids_are_unique(self):
        """
            checks if 'id' is generated randomly and uniquely
        """

        modelInstance_1 = BaseModel()
        modelInstance_2 = BaseModel()
        self.assertNotEqual(modelInstance_1.id, modelInstance_2.id)

    def test_type_of_id_is_str(self):
        """
            checks that 'id' generated is of type str
        """

        modelInstance = BaseModel()
        self.assertTrue(type(modelInstance.id) is str)




class TestBaseModel_created_at_attribute(unittest.TestCase):
    """
        test class for the BaseModel 'created_at' attribute
    """

    def test_created_at_is_datetime(self):
        """
            checks that the attribute 'created_at' is of type datetime
        """

        modelInstance = BaseModel()
        self.assertTrue(type(modelInstance.created_at) is datetime)

    def test_created_at_time_difference(self):
        """
            checks that the attribute 'created_at' of 2 models are different
        """

        modeInstance_1 = BaseModel()
        sleep(0.02)
        modeInstance_2 = BaseModel()
        self.assertLess(modeInstance_1.created_at, modeInstance_2.created_at)




class TestBaseModel_updated_at_attribute(unittest.TestCase):
    """
        test class for the BaseModel 'updated_at' attribute
    """

    def test_updated_at_is_datetime(self):
        """
            checks that the attribute 'updated_at' is of type datetime
        """

        modelInstance = BaseModel()
        self.assertTrue(type(modelInstance.updated_at) is datetime)




class TestBaseModel_save_method(unittest.TestCase):
    """
        test class for the BaseModel 'save' method
    """

    def test_that_save_method_updates_update_at_attribute(self):
        """
            checks that 'save' method updates the updated_at attribute
        """

        modelInstance = BaseModel()
        modelInstance.save()
        self.assertNotEqual(modelInstance.created_at, modelInstance.updated_at)

    def test_save_method_returns_nothing(self):
        """
            checks that 'save' method returns nothing
        """
        modelInstance = BaseModel()
        self.assertEqual(None, modelInstance.save())




class TestBaseModel_to_dict_method(unittest.TestCase):
    """
        test class for the BaseModel 'to_dict' method
    """

    def test_if_to_dict_returns_dict(self):
        """
            checks that 'dict' method returns a dict
        """

        modelInstance = BaseModel()
        self.assertTrue(type(modelInstance.to_dict()) is dict)

    def test_if_to_dict_returns_class_dunder_method(self):
        """
            checks that 'to_dict' return dict contains __class__
        """

        modelInstance = BaseModel()
        self.assertTrue("__class__" in modelInstance.to_dict())

    def test_that_created_at_returned_by_to_dict_is_an_iso_string(self):
        """
            checks that 'created_at' reurned by 'to_dict' is a str obj in ISO format
        """

        modelInstance = BaseModel()
        self.assertEqual(modelInstance.to_dict()["created_at"], modelInstance.created_at.isoformat())

    def test_that_updated_at_returned_by_to_dict_is_an_iso_string(self):
        """
            checks that 'updated_at' reurned by 'to_dict' is a str obj in ISO format
        """

        modelInstance = BaseModel()
        self.assertEqual(modelInstance.to_dict()["updated_at"], modelInstance.updated_at.isoformat())
