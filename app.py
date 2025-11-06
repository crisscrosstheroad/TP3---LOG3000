"""
Flask calculator application

This web application allows the basic arithmetic calculations: addition, substraction, multiplication and division
"""
from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Evaluates a simple arithmetic expression with a single operator and returns the result.
    
    Args:
        expr: mathematical expression
    
    Returns: 
        Result of the mathetical expression
    """
    # Validates that the expr isn't empty
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Extracts the operator in the expr
    for i, ch in enumerate(s):
        if ch in OPS:
            # Validates that there's only one operator
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    # Separates the operants from the operator in order to later convert them.
    left = s[:op_pos]
    right = s[op_pos+1:]

    # Convert string operant to float in order to compute the calculations
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    # Perform the calculation between the two operands with the operator extracted from the expression
    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Handle the main calculator page and its routes

    GET: displays the calculator with an empty result
    POST: processes the inputed expression and displays the result

    Returns:
        Rendered HTML page with the calculator and it's result
    """
    result = ""
    if request.method == 'POST':
        # Obtains the mathematical expression from the form
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    # Runs the program in debug mode
    app.run(debug=True)