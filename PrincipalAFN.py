from graphviz import Digraph
from state import State
from AFNsimulator import Afn

# Función que implementa el algoritmo de Thompson para construir un AFN a partir de un árbol de expresión regular
def thompson(node):
    if not node.nextC:
        # Si el nodo es una hoja, crea un AFN con un carácter
        return Afn.getCharacter(node.value)  

    if node.value == "*":
        afnTemp = thompson(node.nextC[0])
        start = State()
        end = State()
        # Conexión con transición epsilon desde el nuevo estado inicial al inicio del sub-AFN
        start.add(None, afnTemp.stateS)
        # Conexión con transición epsilon desde el nuevo estado inicial al nuevo estado final
        start.add(None, end)
        # Conexión con transición epsilon desde el estado final del sub-AFN al inicio del sub-AFN
        afnTemp.stateE.add(None, afnTemp.stateS)
        # Conexión con transición epsilon desde el estado final del sub-AFN al nuevo estado final
        afnTemp.stateE.add(None, end)  

        return Afn(start, end)

    if node.value == "|":
        # Construir el AFN para la parte izquierda de la expresión
        nfaL = thompson(node.nextC[0])
        # Construir el AFN para la parte derecha de la expresión
        nfaR = thompson(node.nextC[1])
        start = State()
        end = State()
        # Conexión con transición epsilon desde el nuevo estado inicial al inicio del AFN izquierdo
        start.add(None, nfaL.stateS)
        # Conexión con transición epsilon desde el nuevo estado inicial al inicio del AFN derecho
        start.add(None, nfaR.stateS)
        # Conexión con transición epsilon desde el estado final del AFN izquierdo al nuevo estado final
        nfaL.stateE.add(None, end)
        # Conexión con transición epsilon desde el estado final del AFN derecho al nuevo estado final
        nfaR.stateE.add(None, end)

        return Afn(start, end)

    if node.value == "^":
        # Construir el AFN para la parte izquierda de la expresión
        nfaL = thompson(node.nextC[0])
        # Construir el AFN para la parte derecha de la expresión
        nfaR = thompson(node.nextC[1])
        # Conectar el estado final del AFN izquierdo con el estado inicial del AFN derecho
        nfaL.conection(nfaR)

        return Afn(nfaL.stateS, nfaR.stateE)

# Función para simular un AFN en un input dado
def showAFN(afn, afnValue):
    # Conjunto de estados actuales, inicializado con el estado inicial del AFN
    thisSs = set([afn.stateS])  
    # Calcular cierre epsilon de los estados iniciales
    thisSs = putEpsilon(thisSs)  

    for character in afnValue:
        nextSs = set()
        for state in thisSs:
            if character in state.changes:
                for nextS in state.changes[character]:
                    nextSs.add(nextS)
        # Calcular cierre epsilon de los nuevos estados alcanzados
        nextSs = putEpsilon(nextSs)
        # Actualizar los estados actuales
        thisSs = nextSs  

    for state in thisSs:
        if state.final:
            # Si al menos uno de los estados actuales es final, la cadena es aceptada
            return True  
    # Si ninguno de los estados actuales es final, la cadena es rechazada
    return False  

# Función para calcular el cierre epsilon de un conjunto de estados
def putEpsilon(states):
    # Inicializar una pila con los estados iniciales
    stack = list(states)
    # Crear un conjunto con los estados iniciales
    putEpsilon = set(states)

    while stack:
        # Tomar un estado de la pila
        state = stack.pop()
        if (None) in state.changes:
            # Si el estado tiene una transición epsilon (None), explorarlas
            for nextS in state.changes[None]:
                if nextS not in putEpsilon:
                    # Si el estado siguiente no está en el conjunto de cierre epsilon, agregarlo
                    putEpsilon.add(nextS)
                    # Agregar el estado siguiente a la pila para explorar sus transiciones epsilon
                    stack.append(nextS)
    # Devolver el conjunto resultante de estados con cierre epsilon
    return putEpsilon  