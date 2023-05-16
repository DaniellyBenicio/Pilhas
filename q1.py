'''Escreva um programa que leia uma expressão matemática na forma de string e
utilize uma pilha para verificar se os parênteses estão balanceados.'''

class Item:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def push(self, valor): #empilhar
        novoItem = Item(valor)
        novoItem.next = self.top
        self.top = novoItem
        self.size += 1
        
    def pop(self): #desempilhar
        if self.size == 0:
            raise Exception("A pilha está vazia!")
        valor = self.top.valor
        self.top = self.top.next
        self.size -= 1
        return valor
    
    def topo(self): #verTopo
        if self.size == 0:
            raise Exception ("A pilha está vazia!")
        return self.top.valor

    def is_empty(self): #estaVazia
        return self.size == 0
    
    def __len__(self): #tamanho ou getsize
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

exp = input('Informe a expressão matemática com ou sem parênteses: ')
if verificar(exp):
    print('Parênteses estão balanceados!')
else:
    print('Parênteses desbalanceados!')