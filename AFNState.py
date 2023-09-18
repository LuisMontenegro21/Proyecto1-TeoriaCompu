class State:
    # Se inicia en 1
    count = 1  

    def __init__(self):
        # Asignar un número único de estado basado en el contador
        self.number = State.count
        # Inicializar un diccionario para almacenar las transiciones salientes
        self.changes = {}
        # Inicializar el estado como no final
        self.final = False
        # Incrementar el contador de estados para el próximo estado creado
        State.count += 1  

    def add(self, character, state):
        if character not in self.changes:
            # Crear una lista vacía si el carácter no está en las transiciones
            self.changes[character] = []  
        # Agregar el estado de destino a las transiciones con el carácter dado
        self.changes[character].append(state)  

