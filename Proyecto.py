# Universidad del Valle de Guatemala
# Ing. en Ciencias de la Computación
# Teoría de la Computación
# Gabriel García 21352, Luis Montenegro 21699
# Programa para conversión de expresiones regulares

from PostFix import shutingYard
from AFD import AFD
from Reduce import DFA_min
#os.environ["PATH"] += os.pathsep + "C:/Program Files/Graphviz/bin/"


def evaluate(r, w):
    # r = regex
    postfix_expr = shutingYard(r)
    print()
    print(f"Resultado final: {postfix_expr}")
    print()
    
    #pasarle un NFA al argumento de la función
    nfa = []
    AFD.graphing(nfa)

    #pasarle un DFA al argumento de la función para que lo simplifique
    dfa = []
    DFA_min.minimize(dfa)
    
    return 0


print("Programa para conversión de expresiones regulares a autómatas\n" + 
          "En este programa se denota a epsilon como e")
r = str(input("Ingrese una expresion regular r: "))
w = str(input("Ingrese una cadena w: "))
evaluate(r, w)

