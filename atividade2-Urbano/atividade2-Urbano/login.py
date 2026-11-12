# -*- coding: utf-8 -*-
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import repositorio_usuario as repo

class LoginApp:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("login.glade")
        
        self.janela = builder.get_object("janela")
        self.ent_login = builder.get_object("ent_login")
        self.ent_senha = builder.get_object("ent_senha")
        self.btn_entrar = builder.get_object("btn_entrar")
        self.lbl_mensagem = builder.get_object("lbl_mensagem")
        
        self.janela.connect("destroy", Gtk.main_quit)
        self.btn_entrar.connect("clicked", self.ao_clicar_entrar)
        
        self.janela.show_all()

    def mostrar_mensagem(self, texto):
        self.lbl_mensagem.set_text(texto)

    def ao_clicar_entrar(self, componente=None, dados=None):
        login = self.ent_login.get_text().strip()
        senha = self.ent_senha.get_text()
        
        if not login or not senha:
            self.mostrar_mensagem("Preencha o login e a senha.")
            return

        nome = repo.verificar_login(login, senha)
        
        if nome is not None:
            mensagem = f"Login válido. Bem-vindo(a), {nome}!"
            self.mostrar_mensagem(mensagem)
            print(mensagem)
        else:
            mensagem = "Usuário ou senha inválidos."
            self.mostrar_mensagem(mensagem)
            print(mensagem)

if __name__ == "__main__":
    LoginApp()
    Gtk.main()