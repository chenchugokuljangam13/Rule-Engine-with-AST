from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Rule
from .ast import Node  # Ensure the Node and related functions are defined in ast.py
import re
def home(request):
    return render(request, 'rules/index.html')
def create_rule(rule_string):
    # Tokenize the rule string and parse it into an AST
    tokens = re.findall(r'\w+|[()<>!=]=|AND|OR', rule_string)
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
    elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', token):  # Operand (variable)
        condition = token
        operator = tokens.pop(0)  # Get the operator (>, <, =)
        value = tokens.pop(0)      # Get the value
        return Node("operand", value=(condition, operator, value))
    return None

def combine_rules(rules):
    combined_ast = None

    for rule in rules:
        ast = create_rule(rule)
        if combined_ast is None:
            combined_ast = ast
        else:
            combined_ast = Node("operator", left=combined_ast, right=ast, value="OR")

    return combined_ast

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
        if operator == ">":
            return actual_value > int(value)
        elif operator == "<":
            return actual_value < int(value)
        elif operator == "=":
            return actual_value == value

    return False

@api_view(['POST'])
def add_rule(request):
    rule_string = request.data.get('rule_string')
    if not rule_string:
        return Response({"error": "Rule string is required"}, status=400)
    
    rule = Rule.objects.create(rule_string=rule_string)
    return Response({"id": rule.id, "rule_string": rule.rule_string})

@api_view(['POST'])
def evaluate(request):
    rule_string = request.data.get('rule_string')
    data = request.data.get('data')

    # if not rule_string or not data:
    #     return Response({"error": "Both rule_string and data are required"}, status=400)

    # ast = create_rule(rule_string)
    # result = evaluate_rule(ast, data)
    # return Response({"result": result})
    if not rule_string or not data:
        return JsonResponse({"error": "Both rule_string and data are required"}, status=400)

    ast = create_rule(rule_string)
    result = evaluate_rule(ast, data)
    return JsonResponse({"result": result})
