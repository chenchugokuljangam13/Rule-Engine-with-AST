# from django.test import TestCase

# # Create your tests here.
# from .ast import create_rule, evaluate_rule, combine_rules

# class RuleEngineTests(TestCase):

#     def test_create_rule(self):
#         rule = "age > 30 AND department = 'Sales'"
#         ast = create_rule(rule)
#         self.assertIsNotNone(ast)

#     def test_evaluate_rule(self):
#         rule = "age > 30 AND department = 'Sales'"
#         ast = create_rule(rule)
#         data = {"age": 35, "department": "Sales"}
#         result = evaluate_rule(ast, data)
#         self.assertTrue(result, f"Expected True but got {result}")

#     def test_combine_rules(self):
#         rules = [
#             "age > 30 AND department = 'Sales'",
#             "age < 25 AND department = 'Marketing'"
#         ]
#         combined_ast = combine_rules(rules)
#         self.assertIsNotNone(combined_ast)

#     def test_invalid_rule(self):
#         rule = "age >"
#         with self.assertRaises(IndexError):
#             create_rule(rule)

#     def test_evaluate_rule_with_false_data(self):
#         rule = "age > 30 AND department = 'Sales'"
#         ast = create_rule(rule)
#         data = {"age": 25, "department": "Sales"}
#         result = evaluate_rule(ast, data)
#         self.assertFalse(result, f"Expected False but got {result}")



from django.test import TestCase
from .ast import create_rule, evaluate_rule, combine_rules

class RuleEngineTests(TestCase):

    def test_create_rule(self):
        rule = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule)
        self.assertIsNotNone(ast)

    def test_evaluate_rule(self):
        rule = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule)
        data = {"age": 35, "department": "Sales"}
        result = evaluate_rule(ast, data)
        self.assertTrue(result, f"Expected True but got {result}")

    def test_combine_rules(self):
        rules = [
            "age > 30 AND department = 'Sales'",
            "age < 25 AND department = 'Marketing'"
        ]
        combined_ast = combine_rules(rules)
        self.assertIsNotNone(combined_ast)

    def test_invalid_rule(self):
        rule = "age >"
        with self.assertRaises(ValueError):  # Updated to raise ValueError for better error handling
            create_rule(rule)

    def test_evaluate_rule_with_false_data(self):
        rule = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule)
        data = {"age": 25, "department": "Sales"}
        result = evaluate_rule(ast, data)
        self.assertFalse(result, f"Expected False but got {result}")
