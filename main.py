"""
"from database import": vai importar as funçoes da outra pasta
"while True:": esse é o laço de repetiçao que so para quando encontra o "break"
"input():sempre retorna texto entao eu uso o "int()" para converter a idade e o ID em numero
"if __name__ == "__main__":":Esse e utilizado por padrao, faz com que so rode quando o arquivo é executado diretamente.
"""
from database import criar_tabela, cadastrar, listar, buscar_por_nome, atualizar, excluir

def exibir_menu():
    print("\n--- SISTEMA DE PASSAGEIROS ---")
    print("1. Cadastrar passageiro")
    print("2. todos")
    print("3. Buscar por nome")
    print("4. Atualizar a linha de um passageiro")
    print("5. Excluir passageiro")
    print("0. Sair")

def main():
    criar_tabela()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opçao: ")

        if opcao == "1":
            nome = input("Nome:")
            idade = int(input("Idade:"))
            linha = input("Linha do ônibus: ")
            cadastrar(nome, idade, linha)
            print("Passageiro cadastrado com sucesso!")

        elif opcao == "2":
            passageiros = listar()
            for p in passageiros:
                print(f"ID: {p[0]} | Nome: {p[1]} | Idade: {p[2]} | linha: {p[3]}")

        elif opcao == "3":
                nome = input("Digite o nome para buscar: ")
                resultado = buscar_por_nome(nome)
                for p in resultado:
                    print (f"ID: {p[0]} | Nome: {p[1]} | Idade: {p[2]} | linha: {p[3]}")

        elif opcao == "4":
            id_passageiro = int(input("ID do passageiro: "))
            nova_linha = input("Nova linha: ")
            atualizar(id_passageiro, nova_linha)
            print("Atualizado com sucesso!")

        elif opcao == "5":
            id_passageiro = int(input("ID do passageiro a excluir: "))
            excluir(id_passageiro)
            print("Excluído com sucesso!")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()



