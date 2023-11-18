import random
import importlib
import sys
sys.path.append("../mutation")
from mutation.Polynomial import Polynomial

# Mutation Operator 1: Change Coefficients
def mutate_coefficients(poly_instance):
    mutated_coefficients = [coef + random.randint(-1, 1) for coef in poly_instance.coefficients]
    poly_instance.coefficients = mutated_coefficients

# Mutation Operator 2: Modify Addition Operation
def mutate_addition(poly_instance):
    original_add = poly_instance.__add__
    def new_add(self, other):
        # Inverting addition to subtraction for mutation
        return original_add(self, Polynomial([-coeff for coeff in other.coefficients]))
    poly_instance.__add__ = new_add.__get__(poly_instance, Polynomial)

# Mutation Operator 3: Introduce Redundant Code in Multiplication
def mutate_multiplication(poly_instance):
    original_mul = poly_instance.__mul__
    def new_mul(self, other):
        # Introducing redundant operation (adding and subtracting 1)
        result = original_mul(self, other)
        result.coefficients = [coef + 1 - 1 for coef in result.coefficients]
        return result
    poly_instance.__mul__ = new_mul.__get__(poly_instance, Polynomial)

# Mutation Operator 4: Alter Exponent in Evaluation
def mutate_evaluation(poly_instance):
    original_evaluate = poly_instance.evaluate
    def new_evaluate(self, x):
        # Changing exponent calculation
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** (len(self.coefficients) - i))  # Incorrect exponent
        return result
    poly_instance.evaluate = new_evaluate.__get__(poly_instance, Polynomial)

# Function to apply all mutations
def apply_mutations(poly_instance):
    mutate_coefficients(poly_instance)
    mutate_addition(poly_instance)
    mutate_multiplication(poly_instance)
    mutate_evaluation(poly_instance)

# Dynamically import the original Polynomial class from src.py
src_module = importlib.import_module("mutation.Polynomial")
original_polynomial_class = getattr(src_module, "Polynomial")

# Create a wrapper class that inherits from the original Polynomial class
class MutatedPolynomialWrapper(original_polynomial_class):
    def __init__(self, coefficients):
        # Initialize the base Polynomial class
        super().__init__(coefficients)
        
        # Apply mutations to the instance
        apply_mutations(self)

# Example usage of MutatedPolynomialWrapper
mutated_poly_wrapper = MutatedPolynomialWrapper([1, 2, 3])
print(mutated_poly_wrapper)
