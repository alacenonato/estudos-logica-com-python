# Um algoritmo em Python que utiliza os conceitos de variáveis e listas. Esse exemplo cria um programa que gerencia uma lista de compras:

# Variáveis iniciais
lista_compras = []  # Lista vazia para armazenar os itens de compra
opcao = ""  # Variável para controle do loop

print("Bem-vindo à Lista de Compras!")

# Loop principal
while opcao != "4":
    print("\nEscolha uma opção:")
    print("1. Adicionar item à lista")
    print("2. Remover item da lista")
    print("3. Mostrar lista de compras")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        # Adiciona um item à lista
        item = input("Digite o nome do item que deseja adicionar: ")
        lista_compras.append(item)  # Adiciona o item na lista
        print(f"'{item}' foi adicionado à lista.")
    elif opcao == "2":
        # Remove um item da lista
        item = input("Digite o nome do item que deseja remover: ")
        if item in lista_compras:
            lista_compras.remove(item)  # Remove o item da lista
            print(f"'{item}' foi removido da lista.")
        else:
            print(f"'{item}' não está na lista.")
    elif opcao == "3":
        # Exibe os itens da lista
        if lista_compras:
            print("\nItens na sua lista de compras:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")
        else:
            print("\nSua lista de compras está vazia.")
    elif opcao == "4":
        # Sai do programa
        print("Saindo do programa. Até mais!")
    else:
        print("Opção inválida. Tente novamente.")
