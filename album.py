from nodo import Nodo
from figurinha import Figurinha
import json


class Album:

    def __init__(self):

        self.inicio = None
        self.repetidas = None
        self.quantidade = 0
        self.total_album = 500

    # INSERIR

    def inserir(self, figurinha):

        if self.consultar(figurinha.id) is not None:

            self.armazenar_repetida(figurinha)

            print("Figurinha enviada para repetidas.")
            return

        novo = Nodo(figurinha)

        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = novo

        self.quantidade += 1

        print("Figurinha inserida no álbum.")

    # REMOVER

    def remover(self, id):

        if self.inicio is None:
            print("Álbum vazio.")
            return

        if self.inicio.dado.id == id:

            self.inicio = self.inicio.proximo
            self.quantidade -= 1

            print("Figurinha removida.")
            return

        anterior = self.inicio
        atual = self.inicio.proximo

        while atual is not None:

            if atual.dado.id == id:

                anterior.proximo = atual.proximo
                self.quantidade -= 1

                print("Figurinha removida.")
                return

            anterior = atual
            atual = atual.proximo

        print("Figurinha não encontrada.")

    # CONSULTAR

    def consultar(self, id):

        atual = self.inicio

        while atual is not None:

            if atual.dado.id == id:
                return atual.dado

            atual = atual.proximo

        return None

    # MOSTRAR ÁLBUM

    def ver_album_completo(self):

        if self.inicio is None:
            print("Álbum vazio.")
            return

        atual = self.inicio

        while atual is not None:
            atual.dado.exibir()
            atual = atual.proximo

    # PORCENTAGEM

    def ver_porcentagem_concluida(self):

        if self.total_album == 0:
            return 0

        porcentagem = (self.quantidade / self.total_album) * 100

        print(f"Progresso: {porcentagem:.2f}%")

        return porcentagem

    # REPETIDAS

    def armazenar_repetida(self, figurinha):

        atual = self.repetidas

        while atual is not None:

            if atual.dado.id == figurinha.id:
                atual.dado.quantidade += 1
                return

            atual = atual.proximo

        nova = Nodo(figurinha)
        nova.dado.quantidade = 1

        if self.repetidas is None:
            self.repetidas = nova
        else:
            atual = self.repetidas

            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = nova

    def mostrar_repetidas(self):

        if self.repetidas is None:
            print("Sem repetidas.")
            return

        atual = self.repetidas

        while atual is not None:
            atual.dado.exibir()
            atual = atual.proximo

    def contar_repetidas(self):

        contador = 0
        atual = self.repetidas

        while atual is not None:
            contador += atual.dado.quantidade
            atual = atual.proximo

        print("Total repetidas:", contador)
        return contador

    def consultar_repetida(self, id):

        atual = self.repetidas

        while atual is not None:

            if atual.dado.id == id:
                return atual.dado

            atual = atual.proximo

        return None

    def diminuir_repetida(self, id):

        if self.repetidas is None:
            return

        if self.repetidas.dado.id == id:

            self.repetidas.dado.quantidade -= 1

            if self.repetidas.dado.quantidade <= 0:
                self.repetidas = self.repetidas.proximo

            return

        anterior = self.repetidas
        atual = self.repetidas.proximo

        while atual is not None:

            if atual.dado.id == id:

                atual.dado.quantidade -= 1

                if atual.dado.quantidade <= 0:
                    anterior.proximo = atual.proximo

                return

            anterior = atual
            atual = atual.proximo

    # BUSCAS

    def buscar_por_nome(self, nome):

        atual = self.inicio
        encontrou = False

        while atual is not None:

            if atual.dado.nome.lower() == nome.lower():
                atual.dado.exibir()
                encontrou = True

            atual = atual.proximo

        if not encontrou:
            print("Não encontrado.")

    def buscar_por_pais(self, pais):

        atual = self.inicio
        encontrou = False

        while atual is not None:

            if atual.dado.pais.lower() == pais.lower():
                atual.dado.exibir()
                encontrou = True

            atual = atual.proximo

        if not encontrou:
            print("Não encontrado.")

    def salvar_json(self, arquivo):

        dados = []

        atual = self.inicio

        while atual is not None:

            dados.append({
                "id": atual.dado.id,
                "nome": atual.dado.nome,
                "pais": atual.dado.pais,
                "posicao": atual.dado.posicao,
                "camisa": atual.dado.camisa
            })

            atual = atual.proximo

        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)

        print("Álbum salvo em JSON.")

    def carregar_json(self, arquivo):

        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)

        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return

        for item in dados:

            figurinha = Figurinha(
                item["id"],
                item["nome"],
                item["pais"],
                item["posicao"],
                item["camisa"]
            )

            self.inserir(figurinha)

        print("Álbum carregado do JSON.")