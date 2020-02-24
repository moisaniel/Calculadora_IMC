#Calculadora de IMC
#Data de criação: 24/02/2020
#Autor: Moisaniel Sousa Moraes
#
import tkinter as tk
from tkinter import ttk

#Função que calcula o IMC
def calc_Imc():
    #Le a altura
    altura1 = altura.get()
    altura1 = float(altura1)
    #Lê a massa
    massa = peso.get()
    massa = float(massa)
    #Calcula IMC
    imc = massa / (altura1 * altura1)
    #Arredonda o resultado para duas casas decimais após a virgula
    imc = round (imc, 2)
    label_resultado.configure(text=imc)

win = tk.Tk()
#Define o título da janela
win.title("Calcudadora de IMC")
label1 = ttk.Label(win, text="Digite sua altura")
label1.grid(column = 0, row = 0)
altura = ttk.Entry(win)
altura.grid(column = 1, row = 0)
label2=ttk.Label(win, text="Digite seu peso")
label2.grid(column = 0, row = 1)
peso = ttk.Entry(win)
peso.grid(column = 1, row = 1)
#Botão para calcular o IMc
calcula_Imc = ttk.Button(win, text = "Cacular IMC", command = calc_Imc)
calcula_Imc.grid(column = 1, row = 2)
label3 = ttk.Label(win, text="Seu IMC é: ")
label3.grid(column = 0, row = 3)
label_resultado = ttk.Label(win, text = "Resultado")

label_resultado.grid(column = 1, row = 3)

#inicializa a gui
win.mainloop()