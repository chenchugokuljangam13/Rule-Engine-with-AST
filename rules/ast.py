
import re

# Step 1: Define the AST Node class
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left  # Left child (Node)
        self.right = right  # Right child (Node, for operators)
        self.value = value  # Optional value for operand nodes (e.g., for conditions)

    def __repr__(self):
        return f"Node(type={self.type}, left={self.left}, right={self.right}, value={self.value})"


# Step 2: Create rules (parse the rule string into an AST)
def create_rule(rule_string):
    # Tokenize the rule string
    tokens = re.findall(r'\w+|[()<>!=]=|AND|OR', rule_string)
    
    if not tokens:
        raise ValueError("Invalid rule string.")
    
    try:
        return parse_expression(tokens)
    except Exception as e:
        raise ValueError(f"Error parsing rule: {e}")


def parse_expression(tokens):
    if not tokens:
        return None
    
    current_token = tokens.pop(0)
    
    if current_token == '(':  # Handle parentheses (grouped expressions)
        left_node = parse_expression(tokens)
        operator = tokens.pop(0)  # AND/OR
        right_node = parse_expression(tokens)
        tokens.pop(0)  # Remove closing parenthesis ')'
        return Node("operator", left=left_node, right=right_node, value=operator)
    
    elif current_token.isidentifier():  # Handle operands (conditions)
        condition = current_token
        operator = tokens.pop(0)
        value = tokens.pop(0)
        return Node("operand", left=None, right=None, value=(condition, operator, value))

    return None


# Step 3: Combine multiple rules into one AST
def combine_rules(rules):
    combined_ast = None
    
    for rule in rules:
        ast = create_rule(rule)
        if combined_ast is None:
            combined_ast = ast
        else:
            # Combine using OR as default, but you can modify this to use AND if needed
            combined_ast = Node("operator", left=combined_ast, right=ast, value="OR")
    
    return combined_ast


# Step 4: Evaluate the AST against a user-provided data set
VALID_ATTRIBUTES = {"age", "department", "salary", "experience"}

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
        if condition not in VALID_ATTRIBUTES:
            raise ValueError(f"Invalid attribute: {condition}")
        actual_value = data.get(condition)
        if operator == ">":
            return actual_value > int(value)
        elif operator == "<":
            return actual_value < int(value)
        elif operator == "=":
            return actual_value == value
        # Add other comparisons as needed
    
    return False


# Step 5: Modify the AST (modify existing rules)
def modify_rule(ast, condition, new_operator, new_value):
    if ast.type == "operand":
        if ast.value[0] == condition:
            ast.value = (condition, new_operator, new_value)
    elif ast.type == "operator":
        modify_rule(ast.left, condition, new_operator, new_value)
        modify_rule(ast.right, condition, new_operator, new_value)


# Step 6: Example unit tests (to be placed in tests.py or elsewhere)
if __name__ == "__main__":
    # Create a simple rule AST
    rule = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule)
    print("AST for rule:", ast)

    # Example data for evaluation
    data = {"age": 35, "department": "Sales"}
    result = evaluate_rule(ast, data)
    print("Evaluation result:", result)

    # Combining rules
    rules = [
        "age > 30 AND department = 'Sales'",
        "age < 25 AND department = 'Marketing'"
    ]
    combined_ast = combine_rules(rules)
    print("Combined AST for rules:", combined_ast)

    # Modify a rule
    modify_rule(ast, "age", "=", "40")
    print("Modified AST:", ast)

    # Evaluate after modification
    modified_data = {"age": 40, "department": "Sales"}
    modified_result = evaluate_rule(ast, modified_data)
    print("Evaluation result after modification:", modified_result)
