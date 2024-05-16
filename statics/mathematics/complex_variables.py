def two_complex_variable_product(z_1_real_part, z_1_imaginary_part, z_2_real_part, z_2_imaginary_part):
    """
    Recall:

    z1 * z2 = x1 * x2 - y1 * y2 + i (y1 * x2 - y2 * x1).
    """
    real_part = z_1_real_part*z_2_real_part - z_1_imaginary_part*z_2_imaginary_part
    imaginary_part = z_1_imaginary_part*z_2_real_part - z_2_imaginary_part*z_1_real_part
    return complex(real_part, imaginary_part)