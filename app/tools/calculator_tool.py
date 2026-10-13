import ast
import operator as op

from crewai.tools import tool


OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
}


def safe_calculate(expression):
    if not isinstance(expression, str) or len(expression) > 200:
        raise ValueError("Expression must be a string of at most 200 characters.")

    def evaluate(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value

        if isinstance(node, ast.BinOp) and type(node.op) in OPERATORS:
            left = evaluate(node.left)
            right = evaluate(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Exponent must be between -10 and 10.")
            return OPERATORS[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATORS:
            return OPERATORS[type(node.op)](evaluate(node.operand))

        raise ValueError("Only basic mathematical expressions are allowed.")

    tree = ast.parse(expression, mode="eval")
    return evaluate(tree.body)


@tool("business_calculator")
def business_calculator(expression: str) -> str:
    """Calculate basic mathematical expressions for business analysis."""
    try:
        result = safe_calculate(expression)
        return str(result)
    except Exception as exc:
        return f"Calculation error: {exc}"