# Archivo con las funciones para conversión a postfix 

# Para la presedencia de operadores
precedence = {'|': 1, '.': 2, '*': 3}

# define operadores definidos
def is_operator(token):
        return token in "|.*"

#define la presedencia de los operadores
def has_higher_precedence(op1, op2):
        return precedence[op1] > precedence[op2]

#emplea el algo ritmo shunting yard
def shunting_yard(expression):
        output = []
        operator_stack = []

        # se recorre la expresión
        for token in expression:
            # si el token se encuentra 0-9 o a-z se manda a la cola
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

def infix_to_postfix(expression):
    expression = expression.replace(" ", "")
    tokens = [c for c in expression]

    postfix_tokens = shunting_yard(tokens)
    postfix_expression = "".join(postfix_tokens)
    return postfix_expression