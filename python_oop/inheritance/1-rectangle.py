#!/usr/bin/env python3
"""Module that defines a Rectangle class that inherits from BaseGeometry."""
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle defined by its width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
