'''Escreva um programa que use uma pilha para ordenar uma lista de inteiros em ordem crescente.'''

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

def ordemCrescente(qntNumeros):
    p = Pilha()
    
    print('Digite os números que deseja ordenar: ')
    crescente = []
    
    for i in range(qntNumeros):
        num = int(input(f'{i+1}ª número: '))
        crescente.append(num)
        
    crescente.sort(reverse=True)   
        
    for num in crescente:
        p.inserir(num)
    return p    
        
qntNumeros = int(input('Informe a quantidade de números que deseja ordenar: '))
ordem = ordemCrescente(qntNumeros)

while not ordem.is_empty():
    print(ordem.remover())
    