import unittest
from unittest.mock import patch
import app.controller
class TestApp(unittest.TestCase):

#--------------------------------------------------------------

# 1 Teste cadastro de usuário

    @patch("app.controller.cadastro_usuario", return_value="user cadastrado")
    def test_cadastro_usuario_valido(self, mock_salvar):
        nome = "Louie"
        email = "louie@gmail.com"
        senha = "127127"
        cpf = "33333333345"

        resultado = app.controller.cadastro_usuario(nome, email, senha, cpf)

        self.assertEqual(resultado, "user cadastrado")
        mock_salvar.assert_called_once_with(nome, email, senha, cpf)

    
#--------------------------------------------------------------

#2 Teste exibir usuários

    @patch("app.controller.exibir_usuarios", return_value=[{"nome": "Bob", "email": "bob@email.com", "senha": "136136", "cpf": "33333333345"}])
    def test_chamada_exibir_usuarios(self, mock_exibir):
        resultado = app.controller.exibir_usuarios()
        self.assertEqual(resultado, [{"nome": "Bob", "email": "bob@email.com", "senha": "136136", "cpf": "33333333345"}])
        mock_exibir.assert_called_once()

#--------------------------------------------------------------

#3 Listar apenas um usuário

    @patch("app.controller.listar_um_usuario", return_value={"nome": "Bob", "email": "bob@email.com", "senha": "136136", "cpf": "33333333345"})
    def test_listar_um_usuario_encontrado(self, mock_listar):
        resultado = app.controller.listar_um_usuario("33333333345")
        esperado = {"nome": "Bob", "email": "bob@email.com", "senha": "136136", "cpf": "33333333345"}
        self.assertEqual(resultado, esperado)
        mock_listar.assert_called_once_with("33333333345")  # Verifica se a função foi chamada com o CPF correto

    @patch("app.controller.listar_um_usuario")
    def test_listar_um_usuario_nao_encontrado(self, mock_listar):
        mock_listar.return_value = "Usuário não encontrado"

        resultado = app.controller.listar_um_usuario("11111111111")  
        self.assertEqual(resultado, "Usuário não encontrado")
        
        mock_listar.assert_called_once_with("11111111111")
    

#--------------------------------------------------------------

#4 Deletar um usuário

    @patch("app.controller.deletar_usuario", return_value="Usuário deletado com sucesso")
    def test_deletar_usuario_encontrado(self, mock_deletar):  
        resultado = app.controller.deletar_usuario("33333333345")
        self.assertEqual(resultado, "Usuário deletado com sucesso")
        
        mock_deletar.assert_called_once_with("33333333345")

        self.assertNotIn({"nome": "Bob", "email": "bob@email.com", "senha": "136136", "cpf": "33333333345"}, app.controller.users)

   
    @patch("app.controller.users", [{"nome": "Bob", "email": "bob@email.com", "senha": "136136", "cpf": "33333333345"}])  
    def test_deletar_usuario_nao_encontrado(self):
        resultado = app.controller.deletar_usuario("11111111111")  
        
        self.assertEqual(resultado, "Usuário não encontrado")
        
        self.assertIn({"nome": "Bob", "email": "bob@email.com", "senha": "136136", "cpf": "33333333345"}, app.controller.users)
        self.assertEqual(len(app.controller.users), 1)  
        