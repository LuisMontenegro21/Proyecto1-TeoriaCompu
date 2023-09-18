# libreria regular expressions = re
import re

def shutingYard(regex):
    openCaracter = ["(", "[", "}"]
    closeCaracter = [")", "]", "}"]
    def getPrecedence(c):
        # Si no es un operador, retorna 0
        precedence = {
            "|": 1,
            "^": 2,
            "*": 3
        }
        return precedence.get(c, 0)

    def plusToAsterisk(regex):
        #ConvertRegex = cRegex
        cRegex = ""
        i = 0
        for c in regex:
            if c == '+':
                if regex[i-1] in closeCaracter:
                    # i-1, i-2, i-3
                    for j in range(i-1, -1, -1):
                        if regex[j] in openCaracter:
                            cRegex += regex[j:i] + "*"
                            break
            # Si no es + no lo cambia
            else:
                cRegex += c
            i += 1
        return cRegex


    def caracterClass(regex):
        cRegex = ""
        i = 0
        conf = True
        for c in regex:
            if (conf):
                if c == "[":
                    cRegex += "("
                    conf = False
                else:
                    if c == "]":
                        cRegex += ")"
                    else:
                        cRegex += c
            else:
                if regex[i+1] == "]":
                    cRegex += c
                    conf = True
                else:
                    cRegex += c + "|"
            i += 1
        return cRegex   
                    
    def interrogationToEpsilon(regex):
        stack = []
        #Open Caracter List = openCList
        openCList = []
        i = 0
        for c in regex:
            if c == '?':
                if regex[i - 1] == ")":
                    # i-1, i-2, i-3
                    for j in range(i-1, -1, -1):
                        if regex[j] == ")":
                            stack.append(regex[j])
                        else:
                            if regex[j] == "(":
                                stack.pop()
                                if len(stack) == 0:
                                    openCList.append(j + 1)
                                    break
                else:
                    openCList.append(i-1)
            i += 1
        cRegex = ""
        i = 0
        for c in regex:
            if i in openCList:
                count = openCList.count(i)
                cRegex += "(" * count + c
            else:
                if c == "?":
                    cRegex += c + ")"
                else:
                    cRegex += c
            i += 1

        return cRegex.replace('?', '|ε')
    
    
    def concatenation(regex):
        # raw String
        pattern = r'(?<=[a-zA-Z0-9*.ε)\\])(?=[a-zA-Z0-9.(\\@ε])'
        regex = re.sub(pattern, '^', regex)
        # raw String
        pattern = r'(?<=[)\\@])(?=[(a-zA-Z0-9.ε\\@])'
        regex = re.sub(pattern, '^', regex)
        regex = regex.replace('\\^', '\\')
        i = 0
        cRegex = ""
        for c in regex:
            if i != 0 and i != len(regex) - 1:
                if c in openCaracter or c in closeCaracter:
                    if regex[i - 1] == "\\":
                        if regex[i + 1] != "^":
                            cRegex += c + "^"
                        else:
                            cRegex += c
                    else:
                        cRegex += c
                else:
                    cRegex += c
            else:
                cRegex += c
            i += 1

        return cRegex
    
    
    def convert(regex):
        cRegex = concatenation(interrogationToEpsilon(caracterClass(plusToAsterisk(regex))).replace("E", "ε"))
        return cRegex
    
    
    queue = []
    stack = []
    i = 0
    postfix_expr = convert(regex)
    print(f"Expresion: {regex}")
    print(f"Postfix: {postfix_expr}")
    
    for char in regex:
        if char.isalnum() or (char == "(" and regex[i - 1] == "\\") or (char == ")" and regex[i - 1] == "\\"):
            if char == "n":
                if regex[i - 1] != "\\":
                    queue.append(char)
                else:
                    queue.append("\\"+char)
            else:
                queue.append(char)
        else:
            if getPrecedence(char):
                while stack and getPrecedence(stack[-1]) >= getPrecedence(char):
                    c = stack.pop()
                    queue.append(c)
                stack.append(char)
            else:
                if char == "(" and regex[i - 1] != "\\":
                    stack.append(char)
                else:
                    if char == ")" and regex[i - 1] != "\\":
                        while stack and stack[-1] != "(":
                            c  = stack.pop()
                            queue.append(c)
                        c = stack.pop()
                    i += 1
    while stack:
        c = stack.pop()
        queue.append(c)
        
    
    string = "".join(queue)
    
    res = ""
    i = 0
    for c in string:  
        if c == '\\':
            if string[i + 1] == "n":
                res += "\\"
            else:
                res += ""
        else:
            res += c
        i += 1

    return res
