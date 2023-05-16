'''Escreva um programa que leia uma string contendo caracteres (, ), {, }, [ e ],
e use uma pilha para verificar se os caracteres estão balanceados.'''
#CORRIGIR POIS FALTA AVALIAR A ORDEM DE PRECEDENCIA
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
    abertura = ['(', '[', '{']
    fechamento = [')', ']', '}']
    pilha = Pilha()
    for p in exp:
        if p in abertura:
            pilha.push(p)
        elif p in fechamento:
            if pilha.is_empty():
                return False
            elif p == ')':
                if pilha.topo() == '(':
                    pilha.pop()
                else:
                    return False
            elif p == ']':
                if pilha.topo() == '[':
                    pilha.pop()
                else:
                    return False
            elif p == '}':
                if pilha.topo() == '{':
                    pilha.pop()
                else:
                    return False
    return pilha.is_empty()

exp = input('Informe a expressão matemática com ou sem os caracteres "([{}])": ')
if verificar(exp):
    print('Caracteres estão balanceados!')
else:
    print('Caracteres desbalanceados!')