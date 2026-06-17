from figurinha import Figurinha
from album import Album
from historico import Historico

# CRIAÇÃO DOS ÁLBUNS

album_paulo = Album()
album_pedro = Album()

historico = Historico()

album_paulo.carregar_json("dados_copa_paulo.json")
album_pedro.carregar_json("dados_copa_pedro.json")

# ESCOLHA DE ÁLBUM

def escolher_album():

    print("\n1 - Paulo")
    print("2 - Pedro")

    opcao = input("Escolha o álbum: ")

    if opcao == "1":
        return album_paulo

    elif opcao == "2":
        return album_pedro

    else:
        print("Opção inválida.")
        return None

# MENU

def mostrar_menu():

    print("\n===== ÁLBUM DE FIGURINHAS DA COPA =====")
    print("1 - Inserir figurinha")
    print("2 - Remover figurinha")
    print("3 - Consultar figurinha")
    print("4 - Ver álbum completo")
    print("5 - Ver porcentagem concluída")
    print("6 - Ver figurinhas repetidas")
    print("7 - Contar figurinhas repetidas")
    print("8 - Buscar por nome do jogador")
    print("9 - Buscar por país/seleção")
    print("10 - Registrar proposta de troca")
    print("11 - Efetuar troca automática")
    print("0 - Sair")

opcao = -1

while opcao != 0:

    mostrar_menu()

    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Digite apenas números.")
        continue

    # INSERIR
  
    if opcao == 1:

        album = escolher_album()

        if album:

            try:
                id = int(input("ID da figurinha: "))
            except ValueError:
                print("ID inválido.")
                continue

            nome = input("Nome: ")
            pais = input("País: ")
            posicao = input("Posição: ")
            camisa = input("Camisa: ")

            figurinha = Figurinha(id, nome, pais, posicao, camisa)

            album.inserir(figurinha)

    # REMOVER
  
    elif opcao == 2:

        album = escolher_album()

        if album:

            try:
                id = int(input("ID para remover: "))
            except ValueError:
                print("ID inválido.")
                continue

            album.remover(id)

    # CONSULTAR
  
    elif opcao == 3:

        album = escolher_album()

        if album:

            try:
                id = int(input("ID: "))
            except ValueError:
                print("ID inválido.")
                continue

            fig = album.consultar(id)

            if fig:
                fig.exibir()
            else:
                print("Não encontrado.")

    # VER ÁLBUM
    
    elif opcao == 4:

        album = escolher_album()

        if album:
            album.ver_album_completo()

    # % COMPLETO
    
    elif opcao == 5:

        album = escolher_album()

        if album:
            album.ver_porcentagem_concluida()

    # REPETIDAS
    
    elif opcao == 6:

        album = escolher_album()

        if album:
            album.mostrar_repetidas()

    elif opcao == 7:

        album = escolher_album()

        if album:
            album.contar_repetidas()

    # BUSCAS
    
    elif opcao == 8:

        album = escolher_album()

        if album:
            nome = input("Nome do jogador: ")
            album.buscar_por_nome(nome)

    elif opcao == 9:

        album = escolher_album()

        if album:
            pais = input("País: ")
            album.buscar_por_pais(pais)

    # TROCA
    
    elif opcao == 10:

        print("\n1 - Paulo")
        print("2 - Pedro")

        try:
            p1 = input("Quem propõe? (1/2): ")
            id1 = int(input("ID repetida do proponente: "))
            p2 = input("Quem recebe? (1/2): ")
            id2 = int(input("ID repetida do outro: "))
        except ValueError:
            print("Erro nos dados.")
            continue

        pessoa1 = "Paulo" if p1 == "1" else "Pedro"
        pessoa2 = "Paulo" if p2 == "1" else "Pedro"

        album1 = album_paulo if p1 == "1" else album_pedro
        album2 = album_paulo if p2 == "1" else album_pedro

        historico.registrar_proposta(pessoa1, id1, pessoa2, id2)
        historico.efetuar_troca_automatica(album1, album2)

    # SAIR + SALVAR JSON
    
    elif opcao == 0:

        album_paulo.salvar_json("dados_copa_paulo.json")
        album_pedro.salvar_json("dados_copa_pedro.json")

        print("Dados salvos. Encerrando...")





















