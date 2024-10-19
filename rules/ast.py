import re

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type
        self.left = left
        self.right = right
        self.value = value

def create_rule(rule_string):
    tokens = re.findall(r'\w+|[()<>!=]=|AND|OR|\'[^\']*\'|\d+', rule_string)
    print(f"Tokens: {tokens}")
    return parse_expression(tokens)

def parse_expression(tokens):
    if not tokens:
        return None

    token = tokens.pop(0)

    if token == '(':
        left_node = parse_expression(tokens)
        operator = tokens.pop(0)  # Expecting AND/OR
        right_node = parse_expression(tokens)
        tokens.pop(0)  # Remove closing parenthesis
        return Node("operator", left=left_node, right=right_node, value=operator)

    # Check if the first token is a valid variable (condition)
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):  # Operand (variable)
        condition = token
        
        # Ensure we have an operator next
        if not tokens:
            raise ValueError(f"Missing operator after condition '{condition}'")
        operator = tokens.pop(0)  # Get the operator (>, <, =)

        # Ensure operator is valid
        if operator not in [">", "<", "="]:
            raise ValueError(f"Unsupported operator: {operator}")

        # Now, expect a value token
        if not tokens:
            raise ValueError(f"Missing value after operator '{operator}'")
        value = tokens.pop(0)  # Get the value

        # Ensure the value is either a number or a string
        if not re.match(r'^\d+$|^\'[^\']*\'$', value):  # Numbers or quoted strings
            raise ValueError(f"Unsupported value: {value}")

        # Remove single quotes from the value if it's a string
        if value.startswith("'") and value.endswith("'"):
            value = value[1:-1]

        # Convert numeric string to int
        if value.isdigit():
            value = int(value)

        return Node("operand", value=(condition, operator, value))

    raise ValueError(f"Unexpected token: {token}")

def evaluate_rule(ast, data):
    if ast.type == "operator":
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    elif ast.type == "operand":
        condition, operator, value = ast.value
        actual_value = data.get(condition)

        print(f"Checking: {condition} {operator} {value} (actual: {actual_value})")
        
        # Handle None case
        if actual_value is None:
            print(f"Condition '{condition}' not found in data.")
            return False

        # Perform comparison
        if operator == ">":
            return actual_value > value
        elif operator == "<":
            return actual_value < value
        elif operator == "=":
            return actual_value == value

    return False

def combine_rules(rules):
    combined_ast = None

    for rule in rules:
        ast = create_rule(rule)
        if combined_ast is None:
            combined_ast = ast
        else:
            combined_ast = Node("operator", left=combined_ast, right=ast, value="OR")

    return combined_ast
