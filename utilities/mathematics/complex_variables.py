def two_complex_variable_product(
        z_1_real_part: float,
        z_1_imaginary_part: float,
        z_2_real_part: float,
        z_2_imaginary_part: float) -> complex:
    """
    # Title: `two_complex_variable_product`

    ## Description:
    We take the Real and Imaginary parts of two complex numbers and compute their
    product. A complex number has both a Real and Imaginary part, and we need to
    expand out these parts in order to do the calculation in entirey. You can 
    verify for yourself that the following is true:

    $$z1 * z2 = (x1 * x2 - y1 * y2) + i (y1 * x2 + y2 * x1).$$

    ## Arguments:

        1. `z_1_real_part`: `float`
            Re[z_{1}]

        2. `z_1_imaginary_part`: `float`
            Im[z_{1}]

        3. `z_2_real_part`: `float`
            Re[z_{2}]

        4. `z_1_imaginary_part`: `float`
            Im[z_{2}]

    ## Returns:
    
        1. `complex_number`: `complex`
            A `complex` datatype that contains the real and imaginary part
            of the computation.

    ## Examples:
    ```python
    z = complex(1, 1)
    z_real = z.real
    z_imaginary = z.imaginary
    print(two_complex_variable_product(z_real, z_imaginary, z_real, -1 * z_imaginary))
    >>> 2
    ```
    

    ## Notes:
    """

    # (1): Compute the real part of the expression: x1 * x2 + y1 * y2:
    real_part = z_1_real_part * z_2_real_part - z_1_imaginary_part * z_2_imaginary_part

    # (2): Compute the imaginary part of the expression: x2 * y1 - x1 * y2:
    imaginary_part = z_1_imaginary_part * z_2_real_part + z_2_imaginary_part * z_1_real_part

    # (3): Cast the real part and the imaginary part to the `complex` datatype:
    complex_number = complex(real_part, imaginary_part)

    # (4): Return the complex number:
    return complex_number