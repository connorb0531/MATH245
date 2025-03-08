# Connor Buckley
# 5550124589

import itertools
import re
import pandas as pd

# Function to extract variables from a logical formula
def parse_formula(formula):
    formula = formula.replace(' ', '')  # Remove spaces
    variables = set()

    # Regular expression to find variables (letters)
    for match in re.findall(r'[A-Za-z]', formula):
        variables.add(match)

    return sorted(variables)  # Return sorted list of unique variables

# Function to evaluate logical expressions
def evaluate_expression(expression, values):
    expr = expression

    # Replace variables with their truth values
    for var, val in values.items():
        expr = expr.replace(var, str(val))

    # Replace logical operators with Python equivalents
    expr = (expr.replace('<->', '==')  # Biconditional
                .replace('->', ' or not ')  # Implication
                .replace('^', ' and ')  # Conjunction
                .replace('v', ' or ')  # Disjunction
                .replace('~', 'not '))  # Negation

    return eval(expr)  # Evaluate the boolean expression

# Example formula demonstrating implication and contradiction
formula_ex = "~P ^ (P -> Q)"
variables = parse_formula(formula_ex)

# Generate all possible truth assignments
all_combinations = list(itertools.product([0, 1], repeat=len(variables)))

# Evaluate for each combination and store results
truth_table = []
for values in all_combinations:
    truth_values = dict(zip(variables, values))
    result = evaluate_expression(formula_ex, truth_values)
    truth_table.append(list(values) + [result])

# Create a DataFrame for the truth table
columns = variables + ["Result"]
df = pd.DataFrame(truth_table, columns=columns)

# Print the truth table
print("Truth Table for:", formula_ex)
print(df.to_string(index=False))

# Demonstrate proof by contrapositive (P -> Q is equivalent to ~Q -> ~P)
contrapositive_ex = "~Q -> ~P"
print("\nChecking if", formula_ex, "is equivalent to its contrapositive", contrapositive_ex)

def check_equivalence(expr1, expr2):
    equivalent = True
    for values in all_combinations:
        truth_values = dict(zip(variables, values))
        result1 = evaluate_expression(expr1, truth_values)
        result2 = evaluate_expression(expr2, truth_values)
        if result1 != result2:
            equivalent = False
            break
    return equivalent

if check_equivalence("P -> Q", "~Q -> ~P"):
    print("Implication P -> Q is equivalent to its contrapositive ~Q -> ~P")
else:
    print("Implication P -> Q is NOT equivalent to its contrapositive ~Q -> ~P")

# Proof by contradiction example
def proof_by_contradiction(proposition):
    print("\nAttempting proof by contradiction on:", proposition)
    for values in all_combinations:
        truth_values = dict(zip(variables, values))
        result = evaluate_expression(proposition, truth_values)
        if not result:  # If we reach a contradiction (false result), the proposition must be true
            print("Contradiction reached at:", truth_values)
            print("Thus, the negation of the proposition leads to a contradiction, proving the original claim is true.")
            return
    print("No contradiction found, proposition may not be provable this way.")

# Example: Proving (P ^ -Q) -> (P -> Q) by contradiction
proof_by_contradiction("(P ^ ~Q) -> (P -> Q)")