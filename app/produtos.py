import json
import os
from datetime import datetime

from core.logging import registrar_log
from core.backup import registrar_backup

from utils.validador import validar_edicao_nome, validar_edicao_preco, validar_edicao_quantidade

from errors.exceptions import ErroNomeInvalido, ErroPrecoInvalido, ErroQuantidadeInvalida

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
    try:
        with open(CAMINHO_PRODUTOS, 'r', encoding='utf-8') as arq:
            return json.load(arq)
    except json.JSONDecodeError:
        return []
    
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
        data_hora = datetime.now().strftime("%d/%m/%Y - %H:%M:%S")

        produtos = carregar_produtos()

        novo_produto = {
            "id" : gerar_id_produto(produtos),
            "nome" : nome,
            "preco" : preco,
            "quantidade": quantidade,
            "vendido": 0,
            "data_hora": data_hora
        }

        registrar_backup(produtos)

        produtos.append(novo_produto)

        salvar_produto(produtos)

        print(f"✅ Produto '{nome}' cadastrado com sucesso!")
        registrar_log(f"Produto cadastrado: {nome}")
    except ValueError:
        print("❌ Valor inválido. Certifique-se de digitar números válidos para quantidade e preço.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

def registrar_entrada_produto():
    try:
        estoque = carregar_produtos()
        if not estoque:
            print("⚠️ Estoque vazio. Não há produtos para atualizar.")
            return

        print("\nProdutos disponíveis:")
        for prod in estoque:
            print(f"ID: {prod['id']} | {prod['nome']} | Qtd atual: {prod['quantidade']}")

        id_busca = int(input("\nDigite o ID do produto para registrar entrada: "))
        produto = next((p for p in estoque if p['id'] == id_busca), None)

        if not produto:
            print("❌ Produto não encontrado.")
            return

        qtd_adicional = int(input("Quantidade a adicionar: "))
        if qtd_adicional <= 0:
            print("❌ Quantidade deve ser maior que zero.")
            return

        produto['quantidade'] += qtd_adicional
        salvar_produto(estoque)

        registrar_log(f"Entrada registrada: {qtd_adicional} unidades para '{produto['nome']}' (ID {produto['id']})")
        print(f"✅ Entrada registrada com sucesso! Novo total: {produto['quantidade']} unidades.")

    except ValueError:
        print("❌ Valor inválido. Use apenas números.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        registrar_log(f"Erro ao registrar entrada de produto: {e}")

def registrar_saida_produto():
    try:
        estoque = carregar_produtos()
        if not estoque:
            print("⚠️ Estoque vazio. Não há produtos para atualizar.")
            return

        print("\nProdutos disponíveis:")
        for prod in estoque:
            print(f"ID: {prod['id']} | {prod['nome']} | Qtd atual: {prod['quantidade']}")

        id_busca = int(input("\nDigite o ID do produto para registrar saída: "))
        produto = next((p for p in estoque if p['id'] == id_busca), None)

        if not produto:
            print("❌ Produto não encontrado.")
            return

        qtd_retirada = int(input("Quantidade a retirar: "))
        if qtd_retirada <= 0:
            print("❌ Quantidade deve ser maior que zero.")
            return

        if qtd_retirada > produto['quantidade']:
            print(f"❌ Quantidade insuficiente. Estoque atual: {produto['quantidade']}")
            return

        produto['quantidade'] -= qtd_retirada
        produto['vendido'] += qtd_retirada
        salvar_produto(estoque)

        registrar_log(f"Saída registrada: {qtd_retirada} unidades de '{produto['nome']}' (ID {produto['id']})")
        print(f"✅ Saída registrada com sucesso! Novo total: {produto['quantidade']} unidades.")

    except ValueError:
        print("❌ Valor inválido. Use apenas números.")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        registrar_log(f"Erro ao registrar saída de produto: {e}")

def editar_produto():
    estoque = carregar_produtos()

    if not estoque:
        print("⚠️ Estoque vazio. Não há produtos para editar.")
        return

    print("="*40)
    print("Produtos disponíveis".center(40))
    print("="*40)
    for prod in estoque:
        print(f"ID: {prod['id']} | {prod['nome']} | Preço: {float(prod['preco']):.2f} | Qtd Atual: {prod['quantidade']}")

    try:
        id_produto = int(input(f"Digite o ID do produto que deseja editar: "))
    except ValueError:
        print("❌ ID inválido. Digite um número inteiro.")
        return
    
    produto_escolhido = next((p for p in estoque if p['id'] == id_produto), None)

    if not produto_escolhido:
        print("❌ Produto não encontrado.")
        return

    print(f"\nVocê escolheu: {produto_escolhido['nome']} (ID: {produto_escolhido['id']})")

    produto_antigo = {
        "nome": produto_escolhido['nome'],
        "quantidade": produto_escolhido['quantidade'],
        "preco": produto_escolhido['preco']
    }

    chaves_comum = ["nome", "quantidade", "preco"]

    novo_nome : str
    nova_quantidade: int
    novo_preco: float

    while True:
        try:
            novo_nome = validar_edicao_nome(input(f"Nome: [{produto_escolhido['nome']}]").strip())
            nova_quantidade = validar_edicao_quantidade(input(f"Quantidade: [{produto_escolhido['quantidade']}]").strip())
            novo_preco = validar_edicao_preco(input(f"Preço: [{produto_escolhido['preco']}]").strip())

            print(novo_nome)
            break
        except ErroNomeInvalido as e:
            print(str(e))
        except ErroQuantidadeInvalida as e:
            print(str(e))
        except ErroPrecoInvalido as e:
            print(str(e))
        except Exception:
            print("⚠️ Ocorreu um erro. Tente novamente.")

    if not novo_nome and not nova_quantidade and not novo_preco:
        print("⚠️ Nada foi alterado.")
        return

    print(f"Novo nome: {novo_nome}")

    if novo_nome:
        produto_escolhido['nome'] = novo_nome
    if nova_quantidade:
        produto_escolhido['quantidade'] = nova_quantidade
    if novo_preco:
        produto_escolhido['preco'] = novo_preco

    is_equal = all(produto_escolhido[k] == produto_antigo[k] for k in chaves_comum)
    if is_equal:
        print("⚠️ Nada foi alterado. Retornando...")
        return
    registrar_backup(estoque)
    salvar_produto(estoque)

    registrar_log(f"Produto {produto_escolhido['id']} editado. [{produto_antigo['nome']} | {produto_antigo['preco']} | {produto_antigo['quantidade']}] => [{produto_escolhido['nome']} | {produto_escolhido['preco']} | {produto_escolhido['quantidade']}]")
    print(f"✅ Produto editado com sucesso: ID {produto_escolhido['id']} - {produto_escolhido['nome']}")

def excluir_produto():

    try:
        estoque = carregar_produtos()

        if not estoque:
            print("⚠️ Estoque vazio. Não há produtos para atualizar.")
            return

        print("="*40)
        print("PRODUTOS CADASTRADOS".center(40))
        print("="*40)
        for produto in estoque:
            print(f"ID: {produto['id']} | {produto['nome']} | Qtd atual: {produto['quantidade']}")

        id_produto = int(input("\nEscolha o ID do produto que deseja excluir: "))
        produto = next((p for p in estoque if p['id'] == id_produto), None)

        if not produto:
            print("❌ ID não encontrado")
            return
        
        confirmacao = input(f"Você confirma que deseja excluir o produto: {produto['nome']} (ID: {produto['id']})?   [s / n]")

        if confirmacao != 's':
            print("❌ Exclusão cancelada.")
            return
        
        print(produto)
        estoque.remove(produto)
        salvar_produto(estoque)

        registrar_log(f"Produto excluído: {produto['nome']} (ID {produto['id']})")
        print("✅ Produto excluído com sucesso!")

    except Exception as e:
        print(f"❌ Erro ao excluir produto: {e}")
        registrar_log(f"Erro ao excluir produto: {e}")

