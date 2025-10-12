#!/usr/bin/env python
# coding: utf-8

"""
Test suite for the Prime Power Tester module.
"""

import unittest
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from prime_power import is_prime_power, get_prime_power_decomposition


class TestPrimePower(unittest.TestCase):
    """Test cases for prime power functionality."""
    
    def test_is_prime_power_true_cases(self):
        """Test cases where numbers are prime powers."""
        # Test prime numbers (p^1)
        self.assertTrue(is_prime_power(2))
        self.assertTrue(is_prime_power(3))
        self.assertTrue(is_prime_power(5))
        self.assertTrue(is_prime_power(7))
        self.assertTrue(is_prime_power(11))
        
        # Test prime powers (p^n where n > 1)
        self.assertTrue(is_prime_power(4))  # 2^2
        self.assertTrue(is_prime_power(8))  # 2^3
        self.assertTrue(is_prime_power(9))  # 3^2
        self.assertTrue(is_prime_power(16))  # 2^4
        self.assertTrue(is_prime_power(25))  # 5^2
        self.assertTrue(is_prime_power(27))  # 3^3
        self.assertTrue(is_prime_power(32))  # 2^5
        self.assertTrue(is_prime_power(49))  # 7^2
        self.assertTrue(is_prime_power(81))  # 3^4
        self.assertTrue(is_prime_power(125))  # 5^3
    
    def test_is_prime_power_false_cases(self):
        """Test cases where numbers are not prime powers."""
        # Test composite numbers that are not prime powers
        self.assertFalse(is_prime_power(6))   # 2 * 3
        self.assertFalse(is_prime_power(10))  # 2 * 5
        self.assertFalse(is_prime_power(12))  # 2^2 * 3
        self.assertFalse(is_prime_power(14))  # 2 * 7
        self.assertFalse(is_prime_power(15))  # 3 * 5
        self.assertFalse(is_prime_power(18))  # 2 * 3^2
        self.assertFalse(is_prime_power(20))  # 2^2 * 5
        self.assertFalse(is_prime_power(24))  # 2^3 * 3
        self.assertFalse(is_prime_power(30))  # 2 * 3 * 5
        
        # Test edge cases
        self.assertFalse(is_prime_power(1))
        self.assertFalse(is_prime_power(0))
        self.assertFalse(is_prime_power(-1))
    
    def test_get_prime_power_decomposition(self):
        """Test prime power decomposition."""
        # Test prime numbers
        self.assertEqual(get_prime_power_decomposition(2), (2, 1))
        self.assertEqual(get_prime_power_decomposition(3), (3, 1))
        self.assertEqual(get_prime_power_decomposition(5), (5, 1))
        
        # Test prime powers
        self.assertEqual(get_prime_power_decomposition(4), (2, 2))
        self.assertEqual(get_prime_power_decomposition(8), (2, 3))
        self.assertEqual(get_prime_power_decomposition(9), (3, 2))
        self.assertEqual(get_prime_power_decomposition(16), (2, 4))
        self.assertEqual(get_prime_power_decomposition(25), (5, 2))
        self.assertEqual(get_prime_power_decomposition(27), (3, 3))
        self.assertEqual(get_prime_power_decomposition(32), (2, 5))
        self.assertEqual(get_prime_power_decomposition(49), (7, 2))
        self.assertEqual(get_prime_power_decomposition(81), (3, 4))
        self.assertEqual(get_prime_power_decomposition(125), (5, 3))
        
        # Test non-prime powers
        self.assertIsNone(get_prime_power_decomposition(6))
        self.assertIsNone(get_prime_power_decomposition(10))
        self.assertIsNone(get_prime_power_decomposition(12))
        self.assertIsNone(get_prime_power_decomposition(1))
        self.assertIsNone(get_prime_power_decomposition(0))
        self.assertIsNone(get_prime_power_decomposition(-1))
    
    def test_large_numbers(self):
        """Test with larger numbers."""
        # Test some larger prime powers
        self.assertTrue(is_prime_power(1024))  # 2^10
        self.assertEqual(get_prime_power_decomposition(1024), (2, 10))
        
        self.assertTrue(is_prime_power(3125))  # 5^5
        self.assertEqual(get_prime_power_decomposition(3125), (5, 5))
        
        # Test large composite numbers
        self.assertFalse(is_prime_power(1000))  # 2^3 * 5^3
        self.assertIsNone(get_prime_power_decomposition(1000))


if __name__ == "__main__":
    unittest.main()
