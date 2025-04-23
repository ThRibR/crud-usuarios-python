#1 Criar Usuário
#Campos obrigatórios: nome, email, senha, cpf
#Os dados devem ser armazenados em uma lista de dicionários. 

users= []



def cadastro_usuario(nome,email,senha,cpf):
    novo_user= {
        "nome": nome,
        "email": email,
        "senha": senha,
        "cpf": cpf
    }

    for user in users:
        if user["email"] == email:
            return "Erro: email já cadastrado"

    users.append(novo_user)
    return "user cadastrado"

#cadastro_usuario("louie", "louie@gmail.com", "127127", "33333333345")
#print(users[0])

#--------------------------------------------------------------

#2 Listar Todos os Usuários
# Exibir todos os usuários cadastrados.

def exibir_usuarios():
    return users


#print(exibir_usuarios())


#--------------------------------------------------------------

#3 Listar Apenas Um Usuário
# Buscar usuário pelo CPF.

def listar_um_usuario(cpf):
    for user in users:
        if user["cpf"] == cpf:
            return user
    return "Usuário não encontrado"


#--------------------------------------------------------------

#4 Deletar Usuário
# Remover um usuário da lista pelo CPF.

def deletar_usuario(cpf):
    for user in users:
        if user["cpf"] == cpf:
            users.remove(user) 
            return "Usuário deletado com sucesso"
    return "Usuário não encontrado"
