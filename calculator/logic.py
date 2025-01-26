def evaluate_expression(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except Exception:
        return "Error"
