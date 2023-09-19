# Universidad del Valle de Guatemala
# Ing. en Ciencias de la Computación
# Teoría de la Computación
# Gabriel García 21352, Luis Montenegro 21699
# Programa para conversión de expresiones regulares

from PostFix import infix_to_postfix as toPostFix
from AFD import *
from Reduce import DFA_min
from Root import *
from PrincipalAFN import *

graf = Graficador()

def evaluate(r):
    # r => regex
    postfix_expr = toPostFix(r)
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
    
    nfa = AFD(
    4,  # number of states
    ['A', 'B', 'C', 'D'],  # array of states
    3,  # number of alphabets
    ['a', 'b', 'c'],  # array of alphabets
    'A',  # start state
    1,  # number of final states
    ['D'],  # array of final states
    7,  # number of transitions
    [['A', 'a', 'A'], ['A', 'e', 'B'], ['B', 'b', 'B'],
     ['A', 'e', 'C'], ['C', 'c', 'C'], ['B', 'b', 'D'],
     ['C', 'c', 'D']])
    #pasarle un NFA al argumento de la función
    AFD.graphing(nfa, nfa)

    #pasarle un DFA al argumento de la función para que lo simplifique
    dfa = DFA_min()
    dfa.minimize()
    


print("Programa para conversión de expresiones regulares a autómatas\n" + 
          "En este programa se denota a epsilon como e")
r = str(input("Ingrese una expresion regular r: "))
# w = str(input("Ingrese una cadena w: "))
evaluate(r)

