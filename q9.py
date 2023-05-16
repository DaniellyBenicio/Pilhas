'''Escreva um programa que leia uma string contendo apenas números 
e use uma pilha para verificar se a string é um número de palíndromo.'''

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Pilha:
    def __init__(self):
        self._topo = None
        self.tamanho = 0
   
    def __len__(self):
        return self.tamanho
   
    def is_empty(self):
        return self.tamanho == 0
   
    def inserir(self, valor):
        no = No(valor)
        no.proximo = self._topo
        self._topo = no
        self.tamanho += 1
   
    def remover(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        valor = self._topo.valor
        self._topo = self._topo.proximo
        self.tamanho -= 1
        return valor
   
    def topo(self):
        if self.is_empty():
            raise IndexError("A pilha está vazia")
        return self._topo.valor

def verificarPalindromo(num):
    p = Pilha()
    
    for n in num:
        p.inserir(n)
    for n in num:
        if n != p.remover():
            return False
    return True

numero = input('Informe uma string com números para verificar se é palíndromo: ')
numero = verificarPalindromo(numero)
if numero:
    print('O número informado é palíndromo!')
else:
    print('O número informado NÃO é palíndromo!')