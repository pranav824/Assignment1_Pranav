class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # "operator" or "operand"
        self.value = value  # Operand value or operator type (AND/OR)
        self.left = left  # Left child node
        self.right = right  # Right child node

    def __repr__(self):
        return f"Node(type={self.type}, value={self.value})"


class RuleEngine:
    @staticmethod
    def parse_rule(rule_string):
        # Parses a rule string and generates an AST
        # This is a placeholder for parsing logic
        pass

    @staticmethod
    def combine_rules(rules):
        # Combines multiple ASTs into one
        pass

    @staticmethod
    def evaluate_rule(rule_ast, data):
        # Evaluates a given AST against the provided data
        def eval_node(node, data):
            if node.type == "operand":
                attribute, operator, value = node.value.split()
                attribute_value = data.get(attribute)
                if operator == ">":
                    return attribute_value > int(value)
                elif operator == "<":
                    return attribute_value < int(value)
                elif operator == "=":
                    return attribute_value == value
                else:
                    raise ValueError("Invalid operator")
            elif node.type == "operator":
                if node.value == "AND":
                    return eval_node(node.left, data) and eval_node(node.right, data)
                elif node.value == "OR":
                    return eval_node(node.left, data) or eval_node(node.right, data)
            raise ValueError("Invalid node type")

        return eval_node(rule_ast, data)
