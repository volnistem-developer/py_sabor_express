import os 

restaurantes = []

def exibir_nome_do_programa():
    print("""
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀""")
    
def voltar_ao_menu_principal():
    input("\nAperte uma tecla para voltar ao menu principal: ")
    main()

def limpar_terminal():
    os.system('cls')
    
def exibir_opcoes():
    print("\n1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alternar estado do restaurante")
    print("4. Sair\n")

def escolher_opcoes():
    try:
        escolha = int(input("Escolha uma opção: "))

        if escolha == 1:
            cadastrar_novo_restaurante()
        elif escolha == 2:
            listar_restaurantes()
        elif escolha == 3:
            alternar_estado_restaurante()
        elif escolha == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
    
def finalizar_app():
    limpar_terminal()
    print("Programa Finalizado\n")
    os.system("exit")

def opcao_invalida(voltar_ao_menu=True):
    print("Opção Inválida!!\n")

    if voltar_ao_menu == True:
        voltar_ao_menu_principal()

def cadastrar_novo_restaurante():
    limpar_terminal()
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input("Digite a categoria do restaurante: (Japonesa, Italiana, Brasileira...)")
    restaurantes.append({
        "nome": nome_do_restaurante,
        "categoria": categoria,
        "ativo": False
    })
    print("Restaurante cadastrado com sucesso!")
    voltar_ao_menu_principal()

def listar_restaurantes(voltar_ao_menu=True):
    limpar_terminal()
    for (index, restaurante) in enumerate(restaurantes, start=1):
        print(f"{index} - {restaurante["nome"]}          [{restaurante["categoria"]}]    {"Ativo" if restaurante["ativo"] == True else "Inativo"}")

    if voltar_ao_menu == True:
        voltar_ao_menu_principal()

def alternar_estado_restaurante():
    limpar_terminal()
    listar_restaurantes(voltar_ao_menu=False)
    try:
        escolha = int(input("Digite o número do restaurante que deseja alternar o estado: "))
            
        for (index,restaurante) in enumerate(restaurantes, start=1):
            if index == escolha:
                restaurante["ativo"] = not restaurante["ativo"]
                print(f"\nRestaurante {"Ativado" if restaurante["ativo"] else "Desativado"} com sucesso")
                voltar_ao_menu_principal()
            else:
                opcao_invalida(voltar_ao_menu=False)
                input("Aperte uma tecla para continuar")
                alternar_estado_restaurante()
                    
    except:
        opcao_invalida(voltar_ao_menu=False)

def main():
    limpar_terminal()
    exibir_nome_do_programa()  
    exibir_opcoes()
    escolher_opcoes()


if __name__ == '__main__':
    main()