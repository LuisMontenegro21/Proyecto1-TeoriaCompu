# Retorna la precedencia del operador c
def getPrecedence(c):
    # Si no es un operador, retorna 0
    precedence = {
        '(': 1,
        '|': 2,
        '.': 3,
        '?': 4,
        '*': 4,
        '+': 4,
        '^': 5
    }
    return precedence.get(c, 0)
# Agrega puntos para denotar concatenación implícita entre operandos
def formatRegEx(regex):
    # Retorna la expresión regular formateada
    allOperators = ['|', '?', '+', '*', '^']
    binaryOperators = ['^', '|']
    res = ""

    for i in range(len(regex)):
        c1 = regex[i]

        if i + 1 < len(regex):
            c2 = regex[i + 1]

            res += c1

            if (c1 != '(' and c2 != ')' and c2 not in allOperators and c1 not in binaryOperators):
                res += '.'
                
    # Concatena el último carácter de la expresión regular
    res += regex[-1]
    return res

# Convierte la expresión de infix a postfix
def infixToPostfix(regex):
    postfix = ""
    stack = []
    formattedRegEx = formatRegEx(regex)

    for c in formattedRegEx:
        if c == '(':
            stack.append(c)
        elif c == ')':
            # Extrae operadores de la pila hasta encontrar '(' correspondiente
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()  # Elimina el '(' de la pila
        else:
            # Procesa operadores basándose en su precedencia
            while stack and getPrecedence(stack[-1]) >= getPrecedence(c):
                postfix += stack.pop()
            stack.append(c)

    # Añade los operadores restantes de la pila al resultado final
    while stack:
        postfix += stack.pop()

    return postfix # Fin de la función