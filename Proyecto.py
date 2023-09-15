# Universidad del Valle de Guatemala
# Ing. en Ciencias de la Computación
# Teoría de la Computación
# Gabriel García, Luis Montenegro 21699
# Programa para conversión de expresiones regulares

from PostFix import infix_to_postfix as toPostFix



def evaluate(r, w):
    postFixExpression = toPostFix(r)
    print("Postfix: " + postFixExpression)
    return 0


print("Programa para conversión de expresiones regulares a autómatas\n" + 
          "En este programa se denota a epsilon como e")
r = str(input("Ingrese una expresion regular r: "))
w = str(input("Ingrese una cadena w: "))
evaluate(r, w)

