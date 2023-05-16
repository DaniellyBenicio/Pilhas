'''Escreva um programa que use uma pilha para converter um número binário para octal.'''

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
    
def converter_dec_oct(n):
    p = Pilha()
    q = n
    while n > 0:
        r = n % 8
        n = n // 8
        p.inserir(str(r))

    return p

numero = (input('Digite o número que deseja converter de binário para octal: '))
decimal = converterBinpDec(numero)
conversaoOctal = converter_dec_oct(decimal)

print('Em Octal: ', end='')
while not conversaoOctal.is_empty(): # verifica aqui se ainda existe elementos na pilha, enquanto tiver, vai remover.
    print(conversaoOctal.remover(), end='')
