import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# === DADOS DO JOGO ===
temas = {
    "Capitais": {
        "1": ["recife", "joaopessoa", "aracaju", "maceio", "natal"],
        "2": ["brasilia", "curitiba", "manaus", "salvador", "fortaleza"],
        "3": ["londres", "paris", "roma", "madrid", "lisboa"]
    },
    "Animais": {
        "1": ["gato", "cachorro", "coelho", "peixe", "pato"],
        "2": ["leao", "tigre", "elefante", "macaco", "zebra"],
        "3": ["ornitorrinco", "tamandua", "canguru", "avestruz", "pavao"]
    },
    "Frutas": {
        "1": ["abacate", "uva", "banana", "laranja", "morango"],
        "2": ["cupuacu", "pitanga", "buriti", "coco", "caju"],
        "3": ["umbu", "pequi", "acai", "figo", "jabuticaba"]
    }
}

# === VARIÁVEIS GLOBAIS ===
palavra_secreta = ""
letras_usuario = []
chances = 7

# === FUNÇÕES DO JOGO ===
def escolher_palavra():
    global palavra_secreta, letras_usuario, chances
    tema = tema_var.get()
    nivel = nivel_var.get()
    if not tema or not nivel:
        messagebox.showwarning("Erro", "Escolha tema e nível!")
        return
    palavra_secreta = random.choice(temas[tema][nivel])
    letras_usuario = []
    chances = 7
    atualizar_display()

def atualizar_display():
    exibicao = " ".join([k if k in letras_usuario else "_" for k in palavra_secreta])
    palavra_label.config(text=exibicao)
    chances_label.config(text=f"Chances restantes: {chances}")
    usadas_label.config(text=f"Letras usadas: {', '.join(letras_usuario)}")

def tentar_letra():
    global chances, letras_usuario
    letra = entrada_letra.get().lower()
    entrada_letra.delete(0, tk.END)
    if not letra.isalpha() or len(letra) != 1:
        messagebox.showinfo("Aviso", "Digite apenas uma letra!")
        return
    if letra in letras_usuario:
        messagebox.showinfo("Aviso", "Você já tentou essa letra.")
        return
    letras_usuario.append(letra)
    if letra not in palavra_secreta:
        chances -= 1
    atualizar_display()
    verificar_fim()

def verificar_fim():
    if all(j in letras_usuario for j in palavra_secreta):
        mensagem_tela(f"🎉 Você acertou! A palavra era '{palavra_secreta}' 🎉")
        resetar_jogo()
    elif chances <= 0:
        mensagem_tela(f"😢 Poxa! A palavra era '{palavra_secreta}'. 😢")
        resetar_jogo()

def mensagem_tela(msg):
    temp_label = tk.Label(frame_jogo, text=msg, font=("Arial", 16, "bold"), fg="yellow", bg="#2D3333")
    temp_label.grid(row=6, column=0, columnspan=2, pady=10)
    frame_jogo.after(3000, temp_label.destroy)

def resetar_jogo():
    global letras_usuario, chances, palavra_secreta
    letras_usuario = []
    chances = 7
    palavra_secreta = ""
    palavra_label.config(text="")
    entrada_letra.delete(0, tk.END)
    usadas_label.config(text="Letras usadas: ")
    chances_label.config(text="Chances restantes: 7")

# === INTERFACE ===
janela = tk.Tk()
janela.title("🎯 Jogo da Forca")
janela.geometry("1920x1080")

# Fundo
fundo_img = Image.open("imagens/ssala.jpg")
fundo_img = fundo_img.resize((1920, 1080))
fundo = ImageTk.PhotoImage(fundo_img)

canvas = tk.Canvas(janela, width=1920, height=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=fundo, anchor="nw")

# Frame do jogo
frame_jogo = tk.Frame(canvas, bg="#2D3333")
frame_jogo.place(relx=0.48, rely=0.43, anchor="center", width=390, height=350)

# Widgets
tk.Label(frame_jogo, text="Escolha o tema:", bg="#2D3333", fg="white", font=("Times New Roman", 18, "bold")).grid(row=0, column=0, padx=5, pady=5, sticky="w")
tema_var = tk.StringVar(value="Capitais")
tk.OptionMenu(frame_jogo, tema_var, "Capitais", "Animais", "Frutas").grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_jogo, text="Escolha o nível:", bg="#2D3333", fg="white", font=("Times New Roman", 18, "bold")).grid(row=1, column=0, padx=5, pady=5, sticky="w")
nivel_var = tk.StringVar(value="Fácil")
tk.OptionMenu(frame_jogo, nivel_var, "Fácil", "Médio", "Difícil").grid(row=1, column=1, padx=5, pady=5)

tk.Button(frame_jogo, text="🎮 Iniciar Jogo", command=escolher_palavra, bg="#790053", fg="white", width=15).grid(row=2, column=0, columnspan=2, pady=10)

palavra_label = tk.Label(frame_jogo, text="", font=("Times New Roman", 24, "bold"), bg="#2D3333", fg="white")
palavra_label.grid(row=3, column=0, columnspan=2, pady=15)

entrada_letra = tk.Entry(frame_jogo, font=("Times New Roman", 18), width=5, justify="center")
entrada_letra.grid(row=4, column=0, pady=5)
tk.Button(frame_jogo, text="Tentar", command=tentar_letra, bg="#4d0038", fg="white", width=10).grid(row=4, column=1, pady=5)

chances_label = tk.Label(frame_jogo, text="Chances restantes: 7", bg="#2D3333", fg="white", font=("Times New Roman", 14))
chances_label.grid(row=5, column=0, columnspan=2, pady=5)

usadas_label = tk.Label(frame_jogo, text="Letras usadas: ", bg="#2D3333", fg="white", font=("Times New Roman", 14))
usadas_label.grid(row=6, column=0, columnspan=2, pady=5)

janela.mainloop()
