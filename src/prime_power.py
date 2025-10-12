#!/usr/bin/env python
# coding: utf-8

"""
Prime Power Tester Module

This module provides functionality to check if a given natural number is a prime power.
A prime power is a number that can be expressed as p^n where p is a prime number and n is a natural number.
"""

from sympy.ntheory import factorint
from typing import Tuple, Optional


def is_prime_power(q: int) -> bool:
    """
    Check if a given number is a prime power.
    
    Args:
        q (int): The natural number to check
        
    Returns:
        bool: True if q is a prime power, False otherwise
    """
    if q <= 1:
        return False
    
    fact = factorint(q)
    # A number is a prime power if it has exactly one prime factor
    return len(fact) == 1


def get_prime_power_decomposition(q: int) -> Optional[Tuple[int, int]]:
    """
    Get the prime power decomposition of a number.
    
    Args:
        q (int): The natural number to decompose
        
    Returns:
        Optional[Tuple[int, int]]: A tuple (p, n) where q = p^n, or None if not a prime power
    """
    if not is_prime_power(q):
        return None
    
    fact = factorint(q)
    p = list(fact.keys())[0]
    n = list(fact.values())[0]
    return (p, n)


def main():
    """
    Interactive main function for command-line usage.
    """
    try:
        q = int(input("Give me the number q="))
        
        if is_prime_power(q):
            p, n = get_prime_power_decomposition(q)
            print(f"The number {q} is a prime power")
            print(f"The prime number p={p}")
            print(f"The natural number n={n}")
        else:
            print(f"The number {q} is not a prime power")
            print("Run again the code and input a prime power")
            
    except ValueError:
        print("Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nExiting...")


if __name__ == "__main__":
    main()
