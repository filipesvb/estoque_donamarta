import json
import os

CAMINHO_PASTA = "data"
CAMINHO_PRODUTOS = os.path.join(CAMINHO_PASTA, "estoque.json")

def garantir_estrutura():
    if not os.path.exists(CAMINHO_PASTA):
        os.makedirs(CAMINHO_PASTA)
    if not os.path.exists(CAMINHO_PRODUTOS):
        with open(CAMINHO_PRODUTOS, 'w', encoding='utf-8') as arq:
            json.dump([], arq, indent=4, ensure_ascii=False)


def carregar_produtos(caminho : str = CAMINHO_PRODUTOS):
    garantir_estrutura()
    if not os.path.exists(CAMINHO_PRODUTOS):
        return []
    with open(CAMINHO_PRODUTOS, 'r', encoding='utf-8') as arq:
        return json.load(arq)
    
def salvar_produto(lista_produtos):

    with open(CAMINHO_PRODUTOS, 'w', encoding='utf-8') as arq:
        json.dump(lista_produtos, arq, indent=4, ensure_ascii=False)

def gerar_id_produto(lista_produtos):
    if not lista_produtos:
        return 1
    id = max(prod['id'] for prod in lista_produtos) + 1
    return id

def cadastrar_produto():
    try:
        print("="*40)
        print("CADASTRO DE PRODUTOS".center(40))
        print("="*40)
        nome = input("Nome do produto: ").strip()
        if not nome:
            print(f"❌ Nome não pode ser vazio!")
            return
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço unitário (R$): "))

        produtos = carregar_produtos()

        novo_produto = {
            "id" : gerar_id_produto(produtos),
            "nome" : nome,
            "preco" : preco,
            "quantidade": quantidade,
            "vendido": 0
        }

        produtos.append(novo_produto)

        salvar_produto(produtos)

        print(f"✅ Produto '{nome}' cadastrado com sucesso!")
    except ValueError:
        print("❌ Valor inválido. Certifique-se de digitar números válidos para quantidade e preço.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")



