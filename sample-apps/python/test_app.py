#!/usr/bin/env python3
"""
Test suite for the Python sample application
"""

import unittest
from app import greet, add, multiply

class TestApp(unittest.TestCase):
    """Test cases for the sample application."""
    
    def test_greet_default(self):
        """Test greet function with default parameter."""
        self.assertEqual(greet(), "Hello, World!")
    
    def test_greet_with_name(self):
        """Test greet function with a name."""
        self.assertEqual(greet("GitHub"), "Hello, GitHub!")
    
    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(10, 20), 30)
    
    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-5, -3), -8)
    
    def test_add_zero(self):
        """Test adding zero."""
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(5, 0), 5)
    
    def test_add_floats(self):
        """Test adding floating point numbers."""
        self.assertAlmostEqual(add(2.5, 3.7), 6.2, places=1)
    
    def test_add_invalid_input(self):
        """Test add function with invalid input."""
        with self.assertRaises(ValueError):
            add("2", 3)
        with self.assertRaises(ValueError):
            add(2, "3")
    
    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(4, 5), 20)
    
    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(-2, -3), 6)
    
    def test_multiply_zero(self):
        """Test multiplying by zero."""
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
    
    def test_multiply_invalid_input(self):
        """Test multiply function with invalid input."""
        with self.assertRaises(ValueError):
            multiply("2", 3)
        with self.assertRaises(ValueError):
            multiply(2, "3")

if __name__ == "__main__":
    unittest.main()