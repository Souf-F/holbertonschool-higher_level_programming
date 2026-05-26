#!/usr/bin/env python3
"""Module for custom object serialization using pickle."""
import pickle


class CustomObject:
    """Custom class for demonstration of pickle serialization."""

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject.

        Args:
            name: Name of the person (string)
            age: Age of the person (integer)
            is_student: Student status (boolean)
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename: Name of the file to save the serialized object
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file using pickle.

        Args:
            filename: Name of the file containing the serialized object

        Returns:
            CustomObject instance or None if error occurs
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
