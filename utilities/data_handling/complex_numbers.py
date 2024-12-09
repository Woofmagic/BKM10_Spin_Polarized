from decimal import Decimal

def multiply_decimal_with_complex(complex_number: complex, decimal_value: Decimal, ) -> complex:
    real_part = Decimal(complex_number.real) * decimal_value
    imaginary_part = Decimal(complex_number.imag) * decimal_value
    return complex(real_part, imaginary_part)