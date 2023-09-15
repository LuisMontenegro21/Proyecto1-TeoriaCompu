# Clase con las funciones para conversión a postfix 

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def is_operator(token):
        return token in "+-*/^"

    def has_higher_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

    def shunting_yard(expression):
        output = []
        operator_stack = []

        for token in expression:
            if token.isalnum():  
                output.append(token)
            elif is_operator(token):
                while (operator_stack and is_operator(operator_stack[-1]) and
                       has_higher_precedence(operator_stack[-1], token)):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':  
                operator_stack.append(token)
            elif token == ')':  
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()

        while operator_stack:
            output.append(operator_stack.pop())

        return output

    expression = expression.replace(" ", "")
    tokens = [c for c in expression]

    postfix_tokens = shunting_yard(tokens)
    postfix_expression = "".join(postfix_tokens)
    return postfix_expression