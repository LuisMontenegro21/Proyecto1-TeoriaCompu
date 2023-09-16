# Archivo para la conversión del AFN a un AFD mediante construcción de subconjuntos


class AFD:
    def __init__(self, num_states, states, num_alphabet,
                 alphabet, start, num_final, final_states, 
                 num_transitions, transitions):
        self.num_states = num_states
        self.states = states
        self.num_alphabet = num_alphabet
        self.alphabet = alphabet
        self.start = start
        self.num_final = num_final
        self.final_states = final_states
        self.num_transitions = num_transitions
        self.transitions = transitions

        #self.graph = Digraph()
        self.alphabet.append('e')
        self.num_alphabet += 1

        self.states_dict = dict()
        for i in range(self.num_states):
            self.states_dict[self.states[i]] = i
        self.alphabet_dict = dict()
        for i in range(self.num_alphabet):
            self.alphabet_dict[self.alphabet[i]] = i

        self.transition_table = dict()
        for i in range(self.num_states):
            for j in range(self.num_alphabet):
                self.transition_table[str(i)+str(j)] = []
        for i in range(self.num_transitions):
            self.transition_table[str(self.states_dict[self.transitions[i][0]]) + str(self.alphabet_dict[self.transitions[i][1]])].append(self.states_dict[self.transitions[i][2]])
        
    def gatherInput():

        return 0
    
    def __repr__(self):
        return 'Q : ' + str(self.states) + "\nΣ : " + str(self.alphabets) + "\nq0 : " + str(self.start) +  "\nF : " + str(self.final_states) + "\nδ : \n" + str(self.transition_table)

        return 0
    
    def epsilonClosure(self, state):
        #Se crea un diccionario para ver si el estado ya ha sido visitado
        #y un array va a 
        closure = dict()
        closure[self.states_dict[state]] = 0
        closure_stack = [self.states_dict[state]]
        
        while(len(closure_stack) > 0):
            top = closure_stack.pop(0)
            for i in self.transition_table[str(top)+str(self.alphabet_dict['e'])]:
                if i not in closure.keys():
                    closure[i] = 0
                    closure_stack.append(x)
            closure[top] = 1
        return closure.keys()
    
    def stateName(self, state_list):
        name = ''
        for i in state_list:
            name += self.states[i]
        return name
    
    def isFinalState(self, state_list):
        for i in state_list:
            for j in self.finals:
                if (i == self.states_dict[j]):
                    return True
        return False

    