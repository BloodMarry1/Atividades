# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import messagebox

def simular_login():
    login = ent_login.get().strip()
    senha = ent_senha.get()
    
    if not login or not senha:
        lbl_msg.config(text="Preencha o login e a senha.", fg="red")
        return

    # Simulação local para testar a interface no Windows
    if login == "admin" and senha == "123":
        msg = f"Login válido. Bem-vindo(a), {login}!"
        lbl_msg.config(text=msg, fg="green")
        messagebox.showinfo("Sucesso", msg)
    else:
        msg = "Usuário ou senha inválidos."
        lbl_msg.config(text=msg, fg="red")

root = tk.Tk()
root.title("Login - Finanças da Família (Prévia Windows)")
root.geometry("350x250")

tk.Label(root, text="Acesso ao Sistema", font=("Arial", 12, "bold")).pack(pady=15)

tk.Label(root, text="Usuário:", font=("Arial", 9)).pack(anchor="w", padx=35)
ent_login = tk.Entry(root, width=30)
ent_login.pack(padx=35, pady=5)

tk.Label(root, text="Senha:", font=("Arial", 9)).pack(anchor="w", padx=35)
ent_senha = tk.Entry(root, width=30, show="*")
ent_senha.pack(padx=35, pady=5)

btn = tk.Button(root, text="Entrar", command=simular_login, bg="#2196F3", fg="white", width=15, font=("Arial", 9, "bold"))
btn.pack(pady=15)

lbl_msg = tk.Label(root, text="", font=("Arial", 9))
lbl_msg.pack(pady=5)

root.mainloop()