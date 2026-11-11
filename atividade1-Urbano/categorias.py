# -*- coding: utf-8 -*-
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from repositorio_categoria import inserir_categoria, listar_categorias, atualizar_categoria, excluir_categoria

class CategoriasApp:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file("categorias.glade")

        self.window = self.builder.get_object("janela")
        if self.window:
            self.window.connect("destroy", Gtk.main_quit)

        self.ent_nome = self.builder.get_object("ent_nome")
        self.cmb_tipo = self.builder.get_object("cmb_tipo")
        self.list_categorias = self.builder.get_object("lst_categorias")
        self.tvw_categorias = self.builder.get_object("tvw_categorias")
        
        self.btn_gravar = self.builder.get_object("btn_gravar")
        self.btn_editar = self.builder.get_object("btn_editar")
        self.btn_excluir = self.builder.get_object("btn_excluir")
        self.lbl_mensagem = self.builder.get_object("lbl_mensagem")

        if self.btn_gravar:
            self.btn_gravar.connect("clicked", self.on_gravar_clicked)
        if self.btn_editar:
            self.btn_editar.connect("clicked", self.on_editar_clicked)
        if self.btn_excluir:
            self.btn_excluir.connect("clicked", self.on_excluir_clicked)

        if self.tvw_categorias:
            selecao = self.tvw_categorias.get_selection()
            selecao.connect("changed", self.on_tabela_selected)

        self.id_selecionado = None
        self.atualizar_tabela()

    def atualizar_tabela(self):
        if not self.list_categorias:
            return
        self.list_categorias.clear()
        categorias = listar_categorias()
        for cat in categorias:
            self.list_categorias.append([cat[0], cat[1], cat[2]])

    def on_tabela_selected(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter is not None:
            self.id_selecionado = model[treeiter][0]
            self.ent_nome.set_text(model[treeiter][1])
            self.cmb_tipo.set_active_id(model[treeiter][2])
            if self.btn_editar:
                self.btn_editar.set_sensitive(True)
            if self.btn_excluir:
                self.btn_excluir.set_sensitive(True)
        else:
            self.id_selecionado = None
            if self.btn_editar:
                self.btn_editar.set_sensitive(False)
            if self.btn_excluir:
                self.btn_excluir.set_sensitive(False)

    def limpar_formulario(self):
        self.ent_nome.set_text("")
        self.cmb_tipo.set_active_id("D")
        self.id_selecionado = None
        if self.btn_editar:
            self.btn_editar.set_sensitive(False)
        if self.btn_excluir:
            self.btn_excluir.set_sensitive(False)

    def on_gravar_clicked(self, button):
        nome = self.ent_nome.get_text().strip()
        tipo = self.cmb_tipo.get_active_id() or "D"

        if not nome:
            if self.lbl_mensagem:
                self.lbl_mensagem.set_text("Preencha o nome!")
            return

        try:
            inserir_categoria(nome, tipo)
            self.limpar_formulario()
            self.atualizar_tabela()
            if self.lbl_mensagem:
                self.lbl_mensagem.set_text("Gravado com sucesso!")
        except Exception as e:
            if self.lbl_mensagem:
                self.lbl_mensagem.set_text(f"Erro: {e}")

    def on_editar_clicked(self, button):
        if self.id_selecionado is None:
            return
        nome = self.ent_nome.get_text().strip()
        tipo = self.cmb_tipo.get_active_id() or "D"

        if not nome:
            return

        try:
            atualizar_categoria(self.id_selecionado, nome, tipo)
            self.limpar_formulario()
            self.atualizar_tabela()
            if self.lbl_mensagem:
                self.lbl_mensagem.set_text("Atualizado com sucesso!")
        except Exception as e:
            if self.lbl_mensagem:
                self.lbl_mensagem.set_text(f"Erro: {e}")

    def on_excluir_clicked(self, button):
        if self.id_selecionado is None:
            return
        try:
            excluir_categoria(self.id_selecionado)
            self.limpar_formulario()
            self.atualizar_tabela()
            if self.lbl_mensagem:
                self.lbl_mensagem.set_text("Excluído com sucesso!")
        except Exception as e:
            if self.lbl_mensagem:
                self.lbl_mensagem.set_text(f"Erro: {e}")

if __name__ == "__main__":
    app = CategoriasApp()
    if app.window:
        app.window.show_all()
    Gtk.main()