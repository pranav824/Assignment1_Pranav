from django.db import models

class Rule(models.Model):
    rule_string = models.TextField()  # Original rule string
    ast = models.JSONField()  # JSON representation of the AST

    def __str__(self):
        return self.rule_string
