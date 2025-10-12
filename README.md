# Prime Power Tester

A Python package for checking if a given natural number is a prime power and decomposing it into its prime power form.

## What is a Prime Power?

A prime power is a natural number that can be expressed as p^n where:
- p is a prime number
- n is a natural number (positive integer)

Examples of prime powers:
- 2, 3, 5, 7, 11, ... (prime numbers, where n=1)
- 4 = 2², 8 = 2³, 9 = 3², 16 = 2⁴, 25 = 5², ...

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/Prime-Power-Tester.git
cd Prime-Power-Tester
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### As a Python Module

```python
from src.prime_power import is_prime_power, get_prime_power_decomposition

# Check if a number is a prime power
print(is_prime_power(8))  # True
print(is_prime_power(6))  # False

# Get the prime power decomposition
result = get_prime_power_decomposition(8)
if result:
    p, n = result
    print(f"8 = {p}^{n}")  # 8 = 2^3
```

### Command Line Interface

Run the interactive script:

```bash
python src/prime_power.py
```

Then enter a number when prompted:
```
Give me the number q=8
The number 8 is a prime power
The prime number p=2
The natural number n=3
```

## Project Structure

```
Prime-Power-Tester/
├── src/
│   ├── __init__.py
│   └── prime_power.py      # Main module
├── test/
│   └── test_prime_power.py # Test suite
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## API Reference

### `is_prime_power(q: int) -> bool`

Checks if a given number is a prime power.

**Parameters:**
- `q` (int): The natural number to check

**Returns:**
- `bool`: True if q is a prime power, False otherwise

### `get_prime_power_decomposition(q: int) -> Optional[Tuple[int, int]]`

Gets the prime power decomposition of a number.

**Parameters:**
- `q` (int): The natural number to decompose

**Returns:**
- `Optional[Tuple[int, int]]`: A tuple (p, n) where q = p^n, or None if not a prime power

## Testing

Run the test suite:

```bash
python -m pytest test/
```

Or using unittest:

```bash
python test/test_prime_power.py
```

## Dependencies

- `sympy`: For prime factorization functionality

## Examples

```python
# Prime numbers (prime powers with exponent 1)
is_prime_power(7)  # True
get_prime_power_decomposition(7)  # (7, 1)

# Prime powers with higher exponents
is_prime_power(16)  # True
get_prime_power_decomposition(16)  # (2, 4)

# Composite numbers that are not prime powers
is_prime_power(12)  # False
get_prime_power_decomposition(12)  # None
```

## License

This project is open source and available under the MIT License.
