'''Escreva um programa que use uma pilha para converter um número hexadecimal para decimal'''

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

def converter_Hex_Dec(num):
    p = Pilha()
    
    for n in num:
        if n.isdigit():
            p.inserir(int(n))
        elif n == 'a' or n == 'A':
            p.inserir(10)
        elif n == 'b' or n == 'B':
            p.inserir(11)
        elif n == 'c' or n == 'C':
            p.inserir(12)
        elif n == 'd' or n == 'D':
            p.inserir(13)
        elif n == 'e' or n == 'E':
            p.inserir(14)   
        elif n == 'f' or n == 'F':
            p.inserir(15)

    b = 1             
    decimal = 0
    
    while not p.is_empty():
        decimal += p.remover() * b
        b *= 16
    return decimal

numero = input('informe o número que deseja converter de hexadeximal para decimal: ')
r = converter_Hex_Dec(numero)
print('Em decimal: ', r)
