def rule(rule,alfabeto):
    Estate = {
        'letter': '',
        '->': [],
        'goTo': [],
        'final': False
    }
    toCreate = {
        'letter': '',
        '->': [],
        'final': True
    }
    Estate['letter'] = rule[1]
    for i in range(7,len(rule)):
        if rule[i] == '<':
            Estate['->'].append(rule[i-1])
            Estate['goTo'].append(rule[i+1])
        if (rule[i] in alfabeto) and (rule[i+1] != '<' and rule[i-1] != '<'):
            ##uma LETRA por rule que seja final
            toCreate['letter'] = rule[1]
            toCreate['->'].append(rule[i]),
        if (rule[i]=='ε'):
            Estate['final'] = True
    if toCreate['letter'] == '':
        toCreate = False
    return Estate, toCreate

def findLetter(estados,ALFABETO):
    letters = []
    for estado in estados:
        letters.append(estado['letter'])
    for l in ALFABETO:
        if l not in letters:
            return l
    print('Não tem mais letras')
def token(token,inicial,estados,estadosTocreate,ALFABETO):
    if inicial == None:
        inicial = {
            'letter': 'S',
            '->': [],
            'goTo': [],
            'final': False
        }
    for i in range(len(token)):
        if i == 0:
            inicial['->'].append(token[0])
            letter = findLetter(estados,ALFABETO)
            if len(token)==2:
                final = True
            else:
                final = False
            estados.append('letter': letter,
                    '->': [],
                    'goTo': [],
                    'final': final)

    return inicial,estados,estadosTocreate



f = open("inp.txt", "r")
initial = None
estados = []
estadosToCreate = []
ALFABETO = ['S','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfabeto = ['a','b', 'c', 'd', 'e', 'i', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'x']
for i in f:
    n = list(i)
    if n[0] == '<':
        created, toCreate = rule(n,alfabeto)
        if len(estados) == 0:
            initial = created
        estados.append(created)
        if toCreate != False:
            estadosToCreate.append(toCreate)
f.close()
f = open("inp.txt", "r")
for i in f:
    n = list(i)
    if n[0] != '<' and n[0] != '\n' and n[0] != ' ':
        estados[0],estados, estadosToCrete = token(n,initial,estados,estadosToCreate,ALFABETO)
        initial = estados[0]
print(estados)
print(estadosToCreate)