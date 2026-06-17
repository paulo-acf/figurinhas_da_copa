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

figurinhas-da-copa/
│
├── album.py
├── figurinha.py
├── fila.py
├── historico.py
├── nodo.py
├── main.py
│
├── dados_copa_paulo.json
├── dados_copa_pedro.json
│
├── README.md
└── .gitignore

## Persistência

Os dados são armazenados em arquivos JSON, permitindo que os álbuns sejam carregados automaticamente na próxima execução.

## Tecnologias

- Python 3
- Estruturas de Dados (Lista Encadeada e Fila Encadeada)# figurinhas_da_copa

## Como clonar

```bash
git clone https://github.com/paulo-acf/figurinhas_da_copa

cd figurinhas_da_copa

python main.py
```bash