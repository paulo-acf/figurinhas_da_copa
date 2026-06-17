class Figurinha:

    def __init__(
        self,
        id,
        nome,
        pais,
        posicao,
        camisa
    ):

        try:
            self.id = int(id)
        except:
            self.id = -1

        self.nome = nome
        self.pais = pais
        self.posicao = posicao
        self.camisa = camisa

    def exibir(self):

        print("\n===== FIGURINHA =====")
        print("ID:", self.id)
        print("Nome:", self.nome)
        print("País:", self.pais)
        print("Posição:", self.posicao)
        print("Camisa:", self.camisa)
        print("=====================\n")

    def __str__(self):

        return (
            f"ID: {self.id} | "
            f"{self.nome} | "
            f"{self.pais} | "
            f"{self.posicao} | "
            f"{self.camisa}"
        )