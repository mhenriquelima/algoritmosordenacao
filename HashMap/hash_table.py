class Aluno:
    def __init__(self, nome, idade, rgm):
        self.nome = nome
        self.idade = idade
        self.rgm = rgm

    def __str__(self):
        return f"Aluno: {self.nome}, Idade: {self.idade}, RGM: {self.rgm}"

class Node:
    def __init__(self, aluno):
        self.aluno = aluno
        self.prox = None

class HashTableChaining:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash_function(self, rgm):
        return rgm % self.tamanho

    def insert(self, aluno):
        index = self.hash_function(aluno.rgm)
        novo_node = Node(aluno)

        atual = self.tabela[index]
        while atual is not None:
            if atual.aluno.rgm == aluno.rgm:
                return print(f"Aluno com o RGM [{aluno.rgm}] já existe na tabela.")
            atual = atual.prox

        if self.tabela[index] is None:
            self.tabela[index] = novo_node
        else:
            novo_node.prox = self.tabela[index]
            self.tabela[index] = novo_node

    def remove(self, rgm):
        index = self.hash_function(rgm)
        atual = self.tabela[index]
        anterior = None

        while atual is not None:
            if atual.aluno.rgm == rgm:
                if anterior is None:
                    self.tabela[index] = atual.prox
                else:
                    anterior.prox = atual.prox
                return True
            anterior = atual
            atual = atual.prox
        return False

    def search(self, rgm):
        index = self.hash_function(rgm)
        atual = self.tabela[index]

        while atual is not None:
            if atual.aluno.rgm == rgm:
                return atual.aluno
            atual = atual.prox
        return None

    def display(self):
        for i in range(self.tamanho):
            print(f"Index {i}: ", end="")
            atual = self.tabela[i]
            while atual is not None:
                print(f"[{atual.aluno}]", end=" -> ")
                atual = atual.prox
            print("None")