from nodo import Nodo

class Fila:

    def __init__(self):

        self.inicio = None
        self.fim = None
        self.quantidade = 0

    def enqueue(self, dado):

        novo_nodo = Nodo(dado)

        if self.inicio is None:

            self.inicio = novo_nodo
            self.fim = novo_nodo

        else:

            self.fim.proximo = novo_nodo
            self.fim = novo_nodo

        self.quantidade += 1

    def dequeue(self):

        if self.inicio is None:
            print("A fila está vazia.")
            return None

        dado_removido = self.inicio.dado

        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.quantidade -= 1

        return dado_removido

    def limpar(self):

        self.inicio = None
        self.fim = None
        self.quantidade = 0