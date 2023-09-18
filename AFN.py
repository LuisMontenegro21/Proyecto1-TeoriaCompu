from graphviz import Digraph
from AFNstate import State  


class Afn:
    @staticmethod
    def getCharacter(character):
        # Crear un AFN con un solo carácter
        start = State()  # Crear un estado inicial
        end = State()    # Crear un estado final
        start.add(character, end)  # Conectar el estado inicial con el final usando el carácter

        return Afn(start, end)  # Devolver el AFN creado

    def __init__(self, start=None, end=None):
        # Constructor de la clase Afn para crear un AFN
        if start:
            self.stateS = start
        else:
            self.stateS = State()  # Crear un estado inicial por defecto si no se proporciona uno

        if end:
            self.stateE = end
        else:
            self.stateE = State()  # Crear un estado final por defecto si no se proporciona uno
        self.stateE.final = True  # Marcar el estado final como final

    def conection(self, nfaN, character=None):
        # Conectar este AFN con otro AFN usando un carácter
        self.stateE.add(character, nfaN.stateS)  # Conectar el estado final de este AFN con el estado inicial del otro

    def diagram(self):
        # Visualizar el AFN usando graphviz
        dot = Digraph()
        NewS = [self.stateS]  # Lista de estados nuevos a explorar
        pastS = set()  # Conjunto de estados ya explorados

        while NewS:
            thisS = NewS.pop()  # Tomar un estado de la lista de estados nuevos
            for character, nextSs in thisS.changes.items():
                for nextS in nextSs:
                    # Agregar nodos al gráfico
                    if thisS == self.stateS:
                        dot.node(str(id(thisS)), label=f"Inicio", shape="circle")
                    else:
                        dot.node(str(id(thisS)), label=str(thisS.number), shape="circle")

                    if nextS.final and nextS == self.stateE:
                        dot.node(str(id(nextS)), label=f"Final", shape="doublecircle")
                    else:
                        dot.node(str(id(nextS)), label=str(nextS.number), shape="circle")

                    # Agregar bordes al gráfico
                    if character:
                        dot.edge(str(id(thisS)), str(id(nextS)), label=character)
                    else:
                        dot.edge(str(id(thisS)), str(id(nextS)), label="ε")

                    if nextS not in pastS:
                        NewS.append(nextS)  # Agregar estados no explorados a la lista

            pastS.add(thisS)  # Marcar este estado como explorado
        # Devolver el gráfico del AFN
        return dot  