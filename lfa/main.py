import tabulate
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
    sequence = ''
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
            sequence = letter
            if len(token)==2:
                final = True
                aponta = ""
            else:
                aponta = token[i+1]
                final = False
            estados.append({'letter': letter,
                    '->': [aponta],
                    'goTo': [],
                    'final': final})
            estados[0]['goTo'].append(letter)
            goLetter = findLetter(estados,ALFABETO)
            estados[len(estados)-1]['goTo'].append(goLetter)
        
        if token[i+1]=='\n':
            letter = findLetter(estados,ALFABETO)
            letter2 = findLetter(estados,ALFABETO)
            
            estados.append({'letter': letter2,
                    '->': [],
                    'goTo': [],
                    'final': True}
            )
            break
        if token[i]!='\n' and i != 0:
            letter = findLetter(estados,ALFABETO)
            estados.append({'letter': letter,
                    '->': [token[i+1]],
                    'goTo': [],
                    'final': False})
            estados[-1]['goTo'].append(findLetter(estados,ALFABETO))

    return inicial,estados,estadosTocreate

def group(estados):
    for estado in estados:
        for i in range(len(estado['->'])):
            qtd = 0
            for y in range(len(estado['->'])):
                if estado['->'][i]==estado['->'][y]:
                    qtd+=1
                    if qtd>1:
                        aux = estado['goTo'][i]
                        estado['goTo'][i] = [estado['goTo'][i],estado['goTo'][y]]
                        estado['->'].pop(y)
                        estado['goTo'].pop(y)
                        qtd-=1
                        estados = group(estados)
                        return  estados
    return estados





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

for estate in estadosToCreate:
    for estadoExistete in estados:
            if estate['letter']==estadoExistete['letter']:
                newState = findLetter(estados,ALFABETO)
                estados.append({
                    'letter': newState,
                    '->': [],
                    'goTo': [],
                    'final': True})
                estadoExistete['->'].append(estate['->'][0])
                estadoExistete['goTo'].append(newState)

print("até aqui o codigo faz isso")
for estado in estados:
    print(estado)
print("----------------------------------------------------------------------------")


estados = group(estados)
for estado in estados:
    print(estado)
print("----------------------------------------------------------------------------")


for estado in estados:
    for i in range(len(estado['goTo'])):
        if len(estado['goTo'][i])>1:
            estate = estado['goTo'][i]
            new = ({'letter': estate,
                    '->': [],
                    'goTo': [],
                    'final': False})
            for n in estate:
                for est in estados:
                    if n == est['letter']:
                        new['->'].append(est['->'])
                        new['goTo'].append(est['goTo'])
                        if est['final']==True:
                            new['final'] = True
            estados.append(new)

estados = group(estados)
for estado in estados:
    print(estado)
print("----------------------------------------------------------------------------")


