# Mutation Testing

**Set up the Environment** 
- Ensure you have access to the `Polynomial` class, your unit tests, and the pytest testing framework.

Used Poetry

**Define Mutation Operators**

- Identify and define specific mutation operators that you will apply to the `Polynomial` class. Each mutation operator should be well-documented. Example operators may include changing coefficients, modifying arithmetic operations, introducing redundant code, and more.

1. Coefficient Mutation:

- Operator: Randomly change the value of a coefficient in the Polynomial.
- Purpose: Check if the test suite can identify changes in individual coefficients.

2. Arithmetic Operation Mutation:

- Operator: Change the arithmetic operation in one of the methods (__add__, __sub__, __mul__).
- Purpose: Verify that the test suite detects changes in the core arithmetic operations.

3. Zero Coefficient Insertion:

- Operator: Insert a zero coefficient at a random position in the coefficients list.
- Purpose: Test if the system can handle zero coefficients appropriately.

4. Coefficient Deletion:

- Operator: Remove a coefficient from the list.
- Purpose: Check if the code can handle missing coefficients correctly.

5. Boundary Mutation:

- Operator: Adjust the boundaries in the find_root_bisection method (change a or b).
- Purpose: Ensure that the root-finding method is robust to changes in the search interval.

6. Redundant Code Insertion:

- Operator: Introduce redundant code inside one of the methods.
- Purpose: Assess whether the test suite can identify unnecessary or redundant code.

7. Derivative Coefficient Mutation:

- Operator: Modify the coefficients of the derivative polynomial.
- Purpose: Verify if the derivative calculation is sensitive to changes in coefficients.

8. Epsilon Mutation:

- Operator: Change the value of epsilon in the find_root_bisection method.
- Purpose: Check if the choice of epsilon affects the accuracy of root approximation.

9. Iteration Limit Mutation:

- Operator: Modify the maximum iteration limit in the find_root_bisection method.
- Purpose: Evaluate if the iteration limit affects the convergence of the bisection method.

10. Print Statement Deletion:

- Operator: Remove the print statement inside the find_root_bisection method.
- Purpose: Confirm that the mutation testing can identify changes related to debugging or logging.
