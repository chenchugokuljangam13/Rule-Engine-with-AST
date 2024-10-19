from django.db import models

# Create your models here.
from django.db import models

class Rule(models.Model):
    rule_string = models.TextField()  # To store the rule as a string
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for updates

    def __str__(self):
        return self.rule_string  # String representation of the rule
