'''Escreva um programa que use uma pilha para converter um número decimal para hexadecimal.'''

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
    
def converter_dec_hex(n):
    p = Pilha()
    q = n
    while n > 0:
        r = n % 16
        n = n // 16
        p.inserir(hex(r)[2:].upper()) #converta decimal em hexadecimal e deixa em maiusculo. Em linguagens com sintaxes como C# e Java) prefixam-se os #hexadecimais com “0x”, por exemplo “0x5A3”.                           
    return p

n = int(input('Digite um número para converter para hexadecimal: '))
r = converter_dec_hex(n)

while not r.is_empty():
    print(r.remover(), end='')
