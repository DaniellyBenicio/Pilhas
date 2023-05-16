'''Escreva um programa que use uma pilha para verificar se uma expressão aritmética é válida. 
A expressão é válida se para cada parêntese aberto houver um parêntese fechado correspondente e,
para cada operação matemática, houver dois operandos.'''

class Item: #Node ou nó
    def __init__(self, valor): #valor ou data
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, valor): #empilha
        novoItem = Item(valor)
        novoItem.next = self.top
        self.top = novoItem
        self.size += 1
        
    def pop(self): #desempilha
        if self.size == 0:
            raise Exception("A pilha está vazia!")
        valor = self.top.valor
        self.top = self.top.next
        self.size -= 1
        return valor
    
    def topo(self): #peek ou topo
        if self.size == 0:
            raise Exception ("A pilha está vazia!")
        return self.top.valor

    def is_empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size
    

def verificar(exp):
    pilha = Pilha()
    for p in exp:
        if p == '(':
            pilha.push(p)
        elif p == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.push(p)
    return pilha.is_empty()

def infixa_para_posfixa(expressao):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operadores = Pilha()
    posfixa = []
    numeros = '0123456789'
    for caracter in expressao:
        if caracter in numeros:
            posfixa.append(caracter)
        elif caracter == '(':
            operadores.push(caracter)
        elif caracter == ')':
            while operadores.topo() != '(':
                posfixa.append(operadores.pop())
            operadores.pop()
        elif caracter in precedencia:
            while not operadores.is_empty()  \
                and operadores.topo() != '(' \
                and precedencia[caracter] <= precedencia[operadores.topo()]:
                posfixa.append(operadores.pop())
            operadores.push(caracter)
    while not operadores.is_empty():
        posfixa.append(operadores.pop())
    return ''.join(posfixa)
    
def calcular(exp):
    p = Pilha()
    for caractere in exp:
        if caractere.isdigit():
            p.push(caractere)
        else:
            num2 = p.pop()
            num1 = p.pop()
        if caractere == '+':
            resultado = int(num1) + int(num2)
            p.push(str(resultado))
        elif caractere == '-':
            resultado = int(num1) - int(num2)
            p.push(str(resultado))
        elif caractere == '*':
            resultado = int(num1) * int(num2)
            p.push(str(resultado))
        elif caractere == '/':
            resultado = int(num1) / int(num2)
            p.push(str(resultado))
    return p.pop()

s = input('Digite a expressão matemática: ')
if not verificar(s):
    print('A expressão informada é INVÁLIDA!')
else:
    r = infixa_para_posfixa(s)
    resultado = calcular(r)
    print('Resultado: ', resultado)
    

