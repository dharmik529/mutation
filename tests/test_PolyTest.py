import sys

import pytest

sys.path.append("../mutation")
from mutation.mutants import MutatedPolynomialWrapper
from mutation.Polynomial import Polynomial


def test_init():
    poly = Polynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]


def test_str():
    poly = Polynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    poly2 = Polynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = Polynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""


def test_add():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]


def test_sub():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3, -1, 3]


def test_mul():
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    poly_product = poly1 * poly2
    assert poly_product.coefficients == [3, -3, 2, -2]


def test_first_degree_polynomial():
    poly = Polynomial([2, -3])  # Represents 2x - 3
    root = poly.find_root_bisection(0, 5)
    assert abs(root - 1.5) < 1e-6


def test_second_degree_polynomial():
    poly = Polynomial([1, 0, -2])  # Represents x^2 - 2
    root = poly.find_root_bisection(1, 2)
    assert abs(root - 2.0**0.5) < 1e-6


def test_third_degree_polynomial():
    poly = Polynomial([1, 0, -2, 0])  # Represents x^3 - 2x
    root = poly.find_root_bisection(-2, 2)
    assert abs(root - 0.0) < 1e-6


# Mutation testing for each test case


def test_mutated_init():
    mutated_poly = MutatedPolynomialWrapper([3, 0, 2])
    assert mutated_poly.coefficients != [3, 0, 2]  # Mutated coefficients


def test_mutated_str():
    mutated_poly = MutatedPolynomialWrapper([3, 0, 2])
    assert str(mutated_poly) != "3x^2 + 2"  # Mutated __str__ representation


def test_mutated_add():
    poly1 = MutatedPolynomialWrapper([3, 0, 2])
    poly2 = MutatedPolynomialWrapper([1, -1])

    # Mutated addition
    poly_sum = poly1 + poly2
    assert poly_sum.coefficients != [3, 1, 1]  # Mutated addition


def test_mutated_sub():
    poly1 = MutatedPolynomialWrapper([3, 0, 2])
    poly2 = MutatedPolynomialWrapper([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients != [3, -1, 3]  # Mutated subtraction


# Existing test
def test_mutated_mul():
    poly1 = MutatedPolynomialWrapper([3, 0, 2])
    poly2 = MutatedPolynomialWrapper([1, -1])

    # Mutated multiplication
    poly_product = poly1 * poly2
    assert poly_product.coefficients != [3, -3, 2, -2]  # Mutated multiplication


# Additional test to detect AOR mutation in test_mutated_mul
def test_mutated_mul_aor():
    poly1 = MutatedPolynomialWrapper([3, 0, 2])
    poly2 = MutatedPolynomialWrapper([1, -1])

    # Mutated multiplication
    poly_product = poly1 * poly2
    assert poly_product.coefficients != [3, -2, 2, -2]  # Mutated multiplication


def test_polynomial_add_zero():
    poly = Polynomial([3, 0, 2])
    zero_poly = Polynomial([0])
    result = poly + zero_poly
    assert (
        result.coefficients == poly.coefficients
    ), "Adding zero polynomial should have no effect"


def test_polynomial_subtract_self():
    poly = Polynomial([3, 0, 2])
    result = poly - poly
    assert result.coefficients == [0] * len(
        poly.coefficients
    ), "Subtracting the same polynomial should result in a zero polynomial"


def test_polynomial_multiply_by_zero():
    poly = Polynomial([3, 0, 2])
    zero_poly = Polynomial([0])
    result = poly * zero_poly
    assert result.coefficients == [0] * (
        len(poly.coefficients) + len(zero_poly.coefficients) - 1
    ), "Multiplying by zero should result in a zero polynomial"


def test_negative_and_fractional_coefficients():
    poly = Polynomial([-1.5, 3, 0, -2.5])
    assert poly.coefficients == [
        -1.5,
        3,
        0,
        -2.5,
    ], "Should handle negative and fractional coefficients"


def test_str_with_leading_zeros():
    poly = Polynomial([0, 0, 1])
    assert str(poly) == "1", "Should ignore leading zero coefficients"


def test_str_with_single_coefficient():
    poly = Polynomial([42])
    assert str(poly) == "42", "Should handle single coefficient polynomials correctly"


def test_operations_with_zero_polynomial():
    zero_poly = Polynomial([0])
    poly = Polynomial([1, -1, 1])

    # Adding zero should not change the polynomial
    result_add = poly + zero_poly
    assert (
        result_add.coefficients == poly.coefficients
    ), "Adding zero should not change the polynomial"

    # Subtracting zero should not change the polynomial
    result_sub = poly - zero_poly
    assert (
        result_sub.coefficients == poly.coefficients
    ), "Subtracting zero should not change the polynomial"

    # Multiplying by zero should result in a zero polynomial
    result_mul = poly * zero_poly
    assert result_mul.coefficients == [
        0 for _ in range(len(poly.coefficients) + len(zero_poly.coefficients) - 1)
    ], "Multiplying by zero should result in a zero polynomial"


def test_multiply_by_monomial():
    poly1 = Polynomial([2, 3])
    poly2 = Polynomial([1, 0])  # Represents x
    product = poly1 * poly2
    assert product.coefficients == [
        2,
        3,
        0,
    ], "Should correctly multiply a polynomial by a monomial"


def test_find_root_edge_cases():
    poly = Polynomial([1, 0, -4])  # Roots at x = -2 and x = 2

    # Should find a negative root
    root_negative = poly.find_root_bisection(-3, -1)
    assert abs(root_negative + 2) < 1e-6, "Should find a negative root"

    # Should find a positive root
    root_positive = poly.find_root_bisection(1, 3)
    assert abs(root_positive - 2) < 1e-6, "Should find a positive root"


def test_subtraction_to_zero():
    poly1 = Polynomial([1, -1, 1])
    poly2 = Polynomial([1, -1, 1])
    result = poly1 - poly2
    assert all(
        coef == 0 for coef in result.coefficients
    ), "Subtracting the polynomial from itself should yield a zero polynomial"


def test_evaluate_at_zero():
    poly = Polynomial([3, -4, 2])
    assert poly.evaluate(0) == 2, "Evaluating at x=0 should return the constant term"


def test_add_different_lengths():
    poly1 = Polynomial([2, 3])
    poly2 = Polynomial([1, 0, -5])
    result = poly1 + poly2
    assert result.coefficients == [
        1,
        2,
        -2,
    ], "Should correctly add polynomials of different lengths"


def test_multiply_by_non_unit_monomial():
    poly1 = Polynomial([1, 3, -2])
    poly2 = Polynomial([2, 0])  # Represents 2x
    product = poly1 * poly2
    assert product.coefficients == [
        2,
        6,
        -4,
        0,
    ], "Should correctly multiply a polynomial by a monomial with a coefficient other than 1"


def test_incompetent_4():
    # Incompetent mutant #4: AOR mutation
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    # Check the mutated condition where the mutant survived
    result = poly1 + poly2
    assert result.coefficients != [4, -1, 3], "Should detect the mutated condition"


def test_incompetent_7():
    # Incompetent mutant #7: AOR mutation
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    # Check the mutated condition where the mutant survived
    result = poly1 + poly2
    assert result.coefficients != [4, 0, 2], "Should detect the mutated condition"


def test_incompetent_8():
    # Incompetent mutant #8: AOR mutation
    poly1 = Polynomial([3, 0, 2])
    poly2 = Polynomial([1, -1])

    # Check the mutated condition where the mutant survived
    result = poly1 + poly2
    assert result.coefficients != [4, -1, 2], "Should detect the mutated condition"


# Existing test
def test_mutated_init():
    mutated_poly = MutatedPolynomialWrapper([3, 0, 2])
    assert mutated_poly.coefficients != [3, 0, 2]  # Mutated coefficients


# Additional test to detect IOD mutation
def test_mutated_init_iod():
    # Mutated initialization of MutatedPolynomialWrapper
    mutated_poly = MutatedPolynomialWrapper([3, 0, 2, 1])
    assert mutated_poly.coefficients != [3, 0, 2, 1]


def test_mutated_add_aor():
    poly1 = MutatedPolynomialWrapper([3, 0, 2])
    poly2 = MutatedPolynomialWrapper([1, -1])

    # Mutated addition
    poly_sum = poly1 + poly2
    assert poly_sum.coefficients != [3, 1, 2]  # Mutated addition


def test_mutated_mul_red_code():
    # Additional test to detect redundant code in multiplication
    poly1 = MutatedPolynomialWrapper([3, 0, 2])
    poly2 = MutatedPolynomialWrapper([1, -1])

    # Mutated multiplication with redundant code
    poly_product = poly1 * poly2
    assert poly_product.coefficients != [
        3,
        -3,
        2,
        -2,
    ]  # Mutated multiplication with redundant code


def test_mutated_add_sub():
    # Additional test to detect mutated addition and subtraction
    poly1 = MutatedPolynomialWrapper([3, 0, 2])
    poly2 = MutatedPolynomialWrapper([1, -1])

    # Mutated addition and subtraction
    poly_sum = poly1 + poly2
    poly_diff = poly1 - poly2
    assert poly_sum.coefficients != [3, 1, 1] and poly_diff.coefficients != [
        3,
        -1,
        3,
    ], "Mutated addition or subtraction not detected"


# Additional test to detect mutated coefficients
def test_mutated_coefficients():
    poly = MutatedPolynomialWrapper([3, 0, 2])
    assert poly.coefficients != [3, 0, 2], "Mutated coefficients not detected"


# Additional test to detect mutated initialization
def test_mutated_init():
    mutated_poly = MutatedPolynomialWrapper([3, 0, 2])
    assert mutated_poly.coefficients != [3, 0, 2], "Mutated initialization not detected"


# Additional test to detect mutated __str__ representation
def test_mutated_str():
    mutated_poly = MutatedPolynomialWrapper([3, 0, 2])
    assert (
        str(mutated_poly) != "3x^2 + 2"
    ), "Mutated __str__ representation not detected"


# Additional test to detect mutated multiplication with AOR
def test_mutated_mul_aor():
    poly1 = MutatedPolynomialWrapper([3, 0, 2])
    poly2 = MutatedPolynomialWrapper([1, -1])

    # Mutated multiplication with AOR
    poly_product = poly1 * poly2
    assert poly_product.coefficients != [
        3,
        -2,
        2,
        -2,
    ]  # Mutated multiplication with AOR


# Additional test to detect mutated multiplication with altered coefficients
def test_mutated_mul_altered_coeff():
    poly1 = MutatedPolynomialWrapper([3, 0, 2])
    poly2 = MutatedPolynomialWrapper([1, -1])

    # Mutated multiplication with altered coefficients
    poly_product = poly1 * poly2
    assert poly_product.coefficients != [
        3,
        1,
        1,
    ]  # Mutated multiplication with altered coefficients
