'''Escreva um programa que use uma pilha para converter um número binário para hexadecimal.'''

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
    
def converterBinpDec(num):
    p = Pilha()
    
    for n in num:
        p.inserir(int(n))
    
    decimal = 0
    base = 1
    
    while not p.is_empty():
        decimal += p.remover() * base
        base = base * 2
    return decimal
    
def converter_dec_hex(n):
    p = Pilha()
    q = n
    while n > 0:
        r = n % 16
        n = n // 16
        p.inserir(hex(r)[2:].upper())
    return p

n = (input('Digite um número binário para conversão: '))
decimal = converterBinpDec(n)
r = converter_dec_hex(decimal)

print('Em Hexadecimal: ', end='')
while not r.is_empty():
    print(r.remover(), end='')
