# Universidad del Valle de Guatemala
# Ing. en Ciencias de la Computación
# Teoría de la Computación
# Gabriel García 21352, Luis Montenegro 21699
# Programa para conversión de expresiones regulares

from PostFix import shutingYard
from AFD import *
from Reduce import DFA_min
from Root import *
from PrincipalAFN import *

graf = Graficador()

def evaluate(r, w):
    # r = regex
    postfix_expr = shutingYard(r)
    print()
    print(f"Resultado final: {postfix_expr}")
    print()
    
    # AFN
    root = graf.build(postfix_expr)
    print(root)
    State.count = 1
    afn = thompson(root)
    afnPDF = afn.diagram()
    #Abrira un pdf
    afnPDF.render(f'AFN', view = True, cleanup=True)
    
    # Evaluacion de la cadena 
    w = input(f"Ingrese w para ver si es aceptada por AFN:")
    result = showAFN(afn, w)
    if result:
        print(f"La cadena fue aceptada por el AFN")
        print()
    else:
        print(f"La cadena no fue aceptada por el AFN")
        print()
    
    
    #pasarle un NFA al argumento de la función
    nfa = []
    AFD.graphing(nfa)

    #pasarle un DFA al argumento de la función para que lo simplifique
    dfa = DFA_min()
    dfa.minimize()
    


print("Programa para conversión de expresiones regulares a autómatas\n" + 
          "En este programa se denota a epsilon como e")
r = str(input("Ingrese una expresion regular r: "))
w = str(input("Ingrese una cadena w: "))
evaluate(r, w)

