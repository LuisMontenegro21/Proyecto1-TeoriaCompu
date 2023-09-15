# Universidad del Valle de Guatemala
# Ing. en Ciencias de la Computación
# Teoría de la Computación
# Gabriel García, Luis Montenegro 21699
# Programa para conversión de expresiones regulares

from PostFix import infix_to_postfix as toPostFix



# Example usage:
infix_expression = "3 + 4 * (2 - 1)"
postfix_result = toPostFix(infix_expression)
print("Infix Expression:", infix_expression)
print("Postfix Expression:", postfix_result)
