# Álbum de Figurinhas da Copa

Projeto desenvolvido para a disciplina de Estrutura de Dados.

## Descrição

O sistema simula um álbum de figurinhas da Copa do Mundo, permitindo gerenciar duas coleções de figurinhas, armazenar repetidas e realizar trocas automáticas entre os usuários.

Todas as estruturas de dados foram implementadas utilizando listas encadeadas e fila FIFO próprias, sem o uso de listas (`list`) ou outras estruturas prontas do Python.

## Funcionalidades

- Inserir figurinha
- Remover figurinha
- Consultar figurinha
- Exibir álbum completo
- Mostrar porcentagem concluída
- Armazenar figurinhas repetidas
- Listar repetidas
- Contar repetidas
- Buscar por número
- Buscar por jogador
- Buscar por seleção
- Registrar proposta de troca
- Verificar disponibilidade das repetidas
- Efetuar troca automática
- Salvar e carregar os dados em arquivos JSON

## Estrutura do projeto

- `figurinha.py` – Classe da figurinha.
- `nodo.py` – Nó utilizado nas estruturas encadeadas.
- `fila.py` – Implementação da fila FIFO.
- `album.py` – Gerenciamento do álbum e das figurinhas repetidas.
- `historico.py` – Registro e processamento das propostas de troca.
- `main.py` – Menu principal da aplicação.

## Persistência

Os dados são armazenados em arquivos JSON, permitindo que os álbuns sejam carregados automaticamente na próxima execução.

## Tecnologias

- Python 3
- Estruturas de Dados (Lista Encadeada e Fila Encadeada)# figurinhas_da_copa

