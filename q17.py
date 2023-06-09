'''Escreva um programa que use uma pilha para converter um número octal para decimal'''

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

def converter_Oct_Dec(num):
    p = Pilha()
    
    for n in num:
        p.inserir(int(n))

    b = 1             
    s = 0
    
    while not p.is_empty():
        s += p.remover() * b
        b *= 8
    return s

num = input('informe o número que deseja converter de octal para decimal: ')
r = converter_Oct_Dec(num)
print('Em decimal: ', r)
