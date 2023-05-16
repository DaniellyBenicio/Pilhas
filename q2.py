'''Escreva um programa que leia uma string e use uma pilha para inverter a ordem das palavras.'''

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
    
    def topo(self):
        if self.size == 0:
            raise Exception ("A pilha está vazia!")
        return self.top.valor

    def is_empty(self): #estaVazia
        return self.size == 0
    
    def __len__(self): #tamanho ou getsize
        return self.size

def inverter(frase):
    palavras = frase.split()
    pilha = Pilha()
    
    for p in palavras:
        pilha.push(p)
    
    novaFrase = ''
    while not pilha.is_empty(): #enquanto for false, continua executando. Ou seja, enquanto a pilha não estiver vazia, executa.
        novaFrase += pilha.pop() + ' ' #remove o item do topo com o pop e adiciona a nova frase        
    return novaFrase

texto = input('Digite uma string para descobrir seu inverso: ')
palavra = inverter(texto)
print('Palavra inversa: ', palavra)