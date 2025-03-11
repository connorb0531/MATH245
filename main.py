# Connor Buckley
# 5550124589

import itertools  # For generating all possible truth table combinations
import re  # For parsing logical expressions
import pandas as pd  # For displaying truth tables in a structured format


# Function to extract variables from a logical formula
def parse_formula(formula):
    formula = formula.replace(' ', '')  # Remove spaces for uniform processing
    variables = set(re.findall(r'[A-Za-z]', formula))  # Extract unique variables
    return sorted(variables)  # Return sorted list of variables


# Function to evaluate logical expressions
def evaluate_expression(expression, values):
    # Convert implication (P -> Q) into (not P or Q)
    expr = re.sub(r'([~]?\b\w+\b)\s*->\s*([~]?\b\w+\b)', r'(not \1 or \2)', expression)

    # Substitute variables with their corresponding truth values
    for var, val in values.items():
        expr = re.sub(rf'\b{var}\b', str(val), expr)

    # Replace logical operators with Python-compatible syntax
    expr = (expr.replace('^', ' and ')  # Conjunction (AND)
            .replace('v', ' or ')  # Disjunction (OR)
            .replace('~', 'not '))  # Negation (NOT)

    return bool(eval(expr))  # Evaluate the modified logical expression


# Function to generate a truth table
def generate_truth_table(formula):
    variables = parse_formula(formula)  # Extract variables from the formula
    all_combinations = list(itertools.product([0, 1], repeat=len(variables)))  # Generate all possible truth assignments

    truth_table = []
    for values in all_combinations:
        truth_values = dict(zip(variables, values))  # Map variables to truth values
        result = evaluate_expression(formula, truth_values)  # Evaluate the expression
        truth_table.append(list(values) + [result])  # Store row in the truth table

    # Create DataFrame for a structured display
    columns = variables + ["Result"]
    df = pd.DataFrame(truth_table, columns=columns)

    # Display the truth table
    print("\nTruth Table for:", formula)
    print(df.to_string(index=False))


# Function to check logical equivalence
def check_equivalence(expr1, expr2):
    variables = list(set(parse_formula(expr1) + parse_formula(expr2)))  # Extract all unique variables
    all_combinations = list(itertools.product([0, 1], repeat=len(variables)))  # Generate all possible truth assignments

    for values in all_combinations:
        truth_values = dict(zip(variables, values))  # Assign truth values
        if evaluate_expression(expr1, truth_values) != evaluate_expression(expr2, truth_values):  # Compare results
            return False  # If there is a mismatch, expressions are not equivalent
    return True  # Expressions are equivalent


# Function for proof by contradiction
def proof_by_contradiction(proposition):
    variables = parse_formula(proposition)  # Extract variables
    all_combinations = list(itertools.product([0, 1], repeat=len(variables)))  # Generate all possible truth assignments

    print("\nProof by contradiction on:", proposition)
    for values in all_combinations:
        truth_values = dict(zip(variables, values))  # Assign truth values
        if not evaluate_expression(proposition, truth_values):  # If false, a contradiction is found
            print("Contradiction reached at:", truth_values)
            print("Thus, the negation of the proposition leads to a contradiction, proving the original claim is true.")
            return
    print("No contradiction found, proposition may not be provable this way.")


# Example Usage
formula_example_1 = "~P ^ (P -> Q)"  # Example formula
generate_truth_table(formula_example_1)

print("\n===========================================")

formula_example_2a = "P -> Q"
formula_example_2b = "~Q -> ~P"

# Check equivalence of P -> Q and ~Q -> ~P (Contrapositive)
if check_equivalence(formula_example_2a, formula_example_2b):
    print(f"\nImplication P -> Q is equivalent to its contrapositive {formula_example_2a}")
else:
    print(f"\nImplication P -> Q is NOT equivalent to its contrapositive {formula_example_2b}")

generate_truth_table(formula_example_2a)
generate_truth_table(formula_example_2b)

print("\n===========================================")

# Proof by contradiction for P -> Q
proof_by_contradiction("P -> Q")
