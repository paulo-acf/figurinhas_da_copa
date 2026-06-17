from fila import Fila

# PROPOSTA DE TROCA

class PropostaTroca:

    def __init__(
        self,
        pessoa1,
        id_repetida_pessoa1,
        pessoa2,
        id_repetida_pessoa2
    ):

        self.pessoa1 = pessoa1
        self.id_repetida_pessoa1 = id_repetida_pessoa1

        self.pessoa2 = pessoa2
        self.id_repetida_pessoa2 = id_repetida_pessoa2

    def exibir(self):

        print("\n=== PROPOSTA DE TROCA ===")
        print("Pessoa 1:", self.pessoa1)
        print("Figurinha repetida:", self.id_repetida_pessoa1)

        print("Pessoa 2:", self.pessoa2)
        print("Figurinha repetida:", self.id_repetida_pessoa2)

# HISTÓRICO (FILA ENCADEADA)

class Historico:

    def __init__(self):
        self.propostas = Fila()

    def registrar_proposta(
        self,
        pessoa1,
        id_repetida_pessoa1,
        pessoa2,
        id_repetida_pessoa2
    ):

        proposta = PropostaTroca(
            pessoa1,
            id_repetida_pessoa1,
            pessoa2,
            id_repetida_pessoa2
        )

        self.propostas.enqueue(proposta)

        print("Proposta de troca registrada com sucesso.")
  
    def verificar_repetidas(
        self,
        album1,
        id_repetida_pessoa1,
        album2,
        id_repetida_pessoa2
    ):

        repetida1 = album1.consultar_repetida(id_repetida_pessoa1)
        repetida2 = album2.consultar_repetida(id_repetida_pessoa2)

        return repetida1 is not None and repetida2 is not None

    def efetuar_troca_automatica(self, album1, album2):

        proposta = self.propostas.dequeue()

        if proposta is None:
            print("Não há propostas de troca.")
            return

        id1 = proposta.id_repetida_pessoa1
        id2 = proposta.id_repetida_pessoa2

        if not self.verificar_repetidas(album1, id1, album2, id2):
            print("Troca não realizada. Uma das pessoas não possui a figurinha repetida.")
            return

        figurinha1 = album1.consultar_repetida(id1)
        figurinha2 = album2.consultar_repetida(id2)

        album1.inserir(figurinha2)
        album2.inserir(figurinha1)

        album1.diminuir_repetida(id1)
        album2.diminuir_repetida(id2)

        print("Troca realizada automaticamente.")