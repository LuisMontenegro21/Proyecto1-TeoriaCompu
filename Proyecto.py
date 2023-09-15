# Universidad del Valle de Guatemala
# Ing. en Ciencias de la Computación
# Teoría de la Computación
# Gabriel García 21352, Luis Montenegro 21699
# Programa para conversión de expresiones regulares

from PostFix import infixToPostfix



def evaluate(r, w):
    # r = regex
    postfix_expr = infixToPostfix(r)
    print(f"Regex: {r}")
    print(f"Postfix: {postfix_expr}")
    print()
    return 0


print("Programa para conversión de expresiones regulares a autómatas\n" + 
          "En este programa se denota a epsilon como e")
r = str(input("Ingrese una expresion regular r: "))
w = str(input("Ingrese una cadena w: "))
evaluate(r, w)

