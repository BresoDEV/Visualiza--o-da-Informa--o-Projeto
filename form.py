#--------------------------------------------------------------------
#       Modulos externos que precisam ser instalados antes de rodar o programa:
#       pip install matplotlib  
# 
#       Projeto feito na versao 3.7.8 do Python
#
#--------------------------------------------------------------------


#Importando o modulo tkinter para criar a janela
import tkinter as tk

#Importando o modulo do sistema operacional 
import os  
 
#importando modulo TIME (usado em sleeps)
import time 

#modulo MATPLOTLIB para a criação dos gráficos
import matplotlib.pyplot as plt


#Variaveis dos Dados 
anos = ["1872", "1890", "1900", "1920", "1940", "1950", "1960", "1970", "1980", "1991", "2000", "2010", "2022"]
pop = [9930478, 14333915, 17438434, 30635605, 41236315, 51944397, 70992343, 94508583, 121150573, 146917459, 169872856, 190755799, 203080756]

#Variaveis de Texto:
t1 = "Crescimento da População (1872 a 2022) "
t2 = "Ano"
t3 = "População (Milhoes)"

# Gráfico de pizza
def Pizza():
 plt.figure(figsize=(8, 6)) #Cria uma nova figura para o gráfico com o tamanho especificado.
 plt.pie(pop, labels=anos, autopct='%1.1f%%', startangle=140)#Criação do Gráfico de Pizza
 plt.title(t1)#Título Do Gráfico
 plt.axis('equal') #Define que os eixos devem ser iguais
 plt.show()#Exibe o gráfico

# Gráfico de Barras
def Barra():
 plt.figure(figsize=(10, 6))#Cria uma nova figura para o gráfico com o tamanho especificado
 plt.bar(anos, pop, color='green')#cria um gráfico de barras
 plt.xlabel(t2)#Define o rótulo do eixo x
 plt.ylabel(t3)#Define o rótulo do eixo y
 plt.title(t1)#Define o titulo
 plt.xticks(rotation=45)#Rotaciona os rótulos do eixo x em 45 graus
 plt.tight_layout() #Ajusta automaticamente o layout do gráfico para que outros elementos não sejam cortados.
 plt.show()  #Exibe o gráfico

# Gráfico de Linhas
def Linha():
 plt.figure(figsize=(10, 6))#Cria uma nova figura para o gráfico com o tamanho especificado
 plt.plot(anos, pop, marker='o', linestyle='-', color='b')#cria um gráfico
 plt.xlabel(t2)#Define o rótulo do eixo x
 plt.ylabel(t3)#Define o rótulo do eixo y
 plt.title(t1)#Define o titulo
 plt.grid(True)#Exibir ou nao a grade
 plt.xticks(rotation=45)#Rotaciona os rótulos do eixo x em 45 graus
 plt.tight_layout()  #Ajusta automaticamente o layout do gráfico para que outros elementos não sejam cortados.
 plt.show()  #Exibe o gráfico

# Gráfico de Dispersão
def Dispersao(): 
 anos_int = list(map(int, anos))#conversão de valores
 plt.figure(figsize=(10, 6))#Cria uma nova figura para o gráfico com o tamanho especificado
 plt.scatter(anos_int, pop, color='green')#cria um gráfico
 plt.xlabel(t2)#Define o rótulo do eixo x
 plt.ylabel(t3)#Define o rótulo do eixo y
 plt.title(t1)#Define o titulo
 plt.grid(True)#Exibir ou nao a grade
 plt.xticks(anos_int, rotation=45)#Rotaciona os rótulos do eixo x em 45 graus
 plt.tight_layout() #Ajusta automaticamente o layout do gráfico para que outros elementos não sejam cortados.
 plt.show()#Exibe o gráfico


 
# Cria a janela principal
janela = tk.Tk()
janela.title("Visualização da Informação") 
janela.geometry("300x300") 

# Label com minhas infos
label = tk.Label(janela, text="Projeto Pratico de Visualização da Informação\nNome: Eduardo Bresolin\nCurso: Ciências da Computação'\nPolo: Caxias do Sul ")
label.pack(pady=10)

# Pizza
botao_1 = tk.Button(janela, text="Pizza", command=Pizza)
botao_1.pack(pady=5)

# Barra
botao_2 = tk.Button(janela, text="Barra", command=Barra)
botao_2.pack(pady=5)

# Linha
botao_3 = tk.Button(janela, text="Linha", command=Linha)
botao_3.pack(pady=5)

# Dispersao
botao_4 = tk.Button(janela, text="Dispersao", command=Dispersao)
botao_4.pack(pady=5)

# Meus creditos 
creditos = tk.Label(janela, text="18/05/2024")
creditos.pack(pady=10)

# loop que volta pra janela
janela.mainloop()