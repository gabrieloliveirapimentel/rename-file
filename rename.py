import os

def rename_file(filename, new_name):
    # Verifica se o arquivo existe
    if os.path.exists(filename):
        # Extrai a extensão do arquivo
        extension = os.path.splitext(filename)[1]

        # Cria o novo nome do arquivo
        new_filename = new_name + extension

        # Renomeia o arquivo
        os.rename(filename, new_filename)
        print("Arquivo renomeado com sucesso!")
    else:
        print("O arquivo não existe.")

# Solicita ao usuário o nome do arquivo e a nova string
#filename = input("Digite o nome do arquivo: ")
#new_name = input("Digite a nova string: ")
filename = "nome original"+".pdf"
new_name = "novo nome"

# Chama a função para renomear o arquivo
rename_file(filename, new_name)
