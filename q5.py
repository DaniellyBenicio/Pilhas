'''Escreva um programa que use uma pilha para verificar se uma string é um palíndromo 
(ou seja, se é igual quando lida de trás para frente). ex: Roma me tem amor'''

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

def verificar_palindromo(frase):
    p = Pilha()
    frase = frase.replace(' ','')# troca espaço por nada. replace= substituir
    
    for c in frase:
        p.inserir(c)
    
    inverso = ''
    
    while not p.is_empty(): #enquanto for false, continua executando. Ou seja, enquanto a pilha não estiver vazia, executa.
        inverso += p.remover()  #remove o item do topo com o pop e adiciona a nova frase
    return inverso == frase #remove o espaço final extra

texto = input('Digite uma frase: ')
r = verificar_palindromo(texto)
if r: 
    print('A frase/palavra informada é um palíndromo!')
else:
    print('A frase/palavra não é um palíndromo!')
