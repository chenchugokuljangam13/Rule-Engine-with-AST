from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
from django.http import JsonResponse
from .models import Rule
from .ast import Node
def home(request):
    return HttpResponse("Welcome to the Rule Engine!")

def create_rule(rule_string):
    # Placeholder for rule parsing logic; implement a parser to convert the rule_string to an AST.
    pass

def combine_rules(rules):
    # Combine the ASTs of individual rules into one; implement logic to minimize redundancy.
    pass

def evaluate_rule(ast, data):
    # Evaluate the AST against the provided data and return a boolean result.
    pass


from rest_framework.decorators import api_view
from rest_framework.response import Response

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

    if not rule_string or not data:
        return Response({"error": "Both rule_string and data are required"}, status=400)

    ast = create_rule(rule_string)
    result = evaluate_rule(ast, data)
    return Response({"result": result})
