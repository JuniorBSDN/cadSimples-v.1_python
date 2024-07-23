import tkinter as tk
from tkinter import messagebox
import os  # Importar módulo os

def logar():
    # Obter valores digitados
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()

    # Validação de login (simulação simples)
    if usuario == "admin" and senha == "senha123":
        # Login bem-sucedido! Redirecionar para outro script
        try:
            os.system("python cadClient.py")  # Executar outro_script.py
            janela_login.destroy()  # Fechar janela de login
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao executar outro script: {e}")
    else:
        # Login falhou
        messagebox.showerror("Erro de Login", "Usuário ou senha inválidos.")

janela_login = tk.Tk()
janela_login.title("Login")

# Rótulos e campos de entrada
label_usuario = tk.Label(janela_login, text="Usuário:")
label_usuario.grid(row=0, column=0)

entrada_usuario = tk.Entry(janela_login)
entrada_usuario.grid(row=0, column=1)

label_senha = tk.Label(janela_login, text="Senha:")
label_senha.grid(row=1, column=0)

entrada_senha = tk.Entry(janela_login, show="*")  # Ocultar digitação
entrada_senha.grid(row=1, column=1)

# Botão de login
botao_login = tk.Button(janela_login, text="Entrar", command=logar)
botao_login.grid(row=2, column=0, columnspan=2)

# Manter a janela em execução
janela_login.mainloop()
