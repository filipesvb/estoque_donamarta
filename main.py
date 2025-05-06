from interface.terminal import mostrar_menu
from app.produtos import cadastrar_produto, registrar_entrada_produto, registrar_saida_produto, excluir_produto

def main():

    while True:
        opcao = mostrar_menu()

        if opcao == '1':
            # print("👉 Cadastrar produto (em breve)")
            cadastrar_produto()
        elif opcao == '2':
            # print("👉 Entrada no estoque (em breve)")
            registrar_entrada_produto()
        elif opcao == '3':
            # print("👉 Saída de produto (em breve)")
            registrar_saida_produto()
        elif opcao == '4':
            print("👉 Listar produtos (em breve)")
        elif opcao == '5':
            print("👉 Relatório de estoque (em breve)")
        elif opcao == '6':
            print("👉 Editar produto (em breve)")
        elif opcao == '7':
            # print("👉 Excluir produto (em breve)")
            excluir_produto()
        elif opcao == '0':
            print("Saindo do sistema... 👋")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")
        

if __name__ == "__main__":
    main()