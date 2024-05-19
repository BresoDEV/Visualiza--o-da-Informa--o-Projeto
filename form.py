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
sexo = ["Homens", "Mulheres" ]
sexoN = [104548325, 98532431 ]

etnia = ["Branca","Preta","Amarela","Parda","Indigena"  ]
etniaN = [88252121,20656458,850130,92083286,1227642]

#nao utilizadas no momento...
maisPopulosas = [ "Minas Gerais","São Paulo","Parana","Rio Grande do Sul","Rio de Janeiro","Bahia"  ]
maisPopulosasN = [ 20539989,44411238,11444380,10882965,16055174,14141626 ]

#Variaveis de Texto:
t1 = "Crescimento da População (1872 a 2022) "
t2 = "Ano"
t3 = "População (Milhoes)"

# Gráfico de pizza
def Pizza():
 plt.figure(figsize=(8, 6)) #Cria uma nova figura para o gráfico com o tamanho especificado.
 plt.pie(sexoN, labels=sexo, autopct='%1.1f%%', startangle=140)#Criação do Gráfico de Pizza
 plt.title("Porcentagem de Sexos (2022)")#Título Do Gráfico
 plt.axis('equal') #Define que os eixos devem ser iguais
 plt.show()#Exibe o gráfico

# Gráfico de Barras
def Barra():
 plt.figure(figsize=(10, 6))#Cria uma nova figura para o gráfico com o tamanho especificado
 plt.bar(etnia, etniaN, color='green')#cria um gráfico de barras 
 plt.ylabel("Milhoes")#Define o rótulo do eixo y
 plt.title("Etnias (2022)")#Define o titulo
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

 


 
# Cria a janela principal
janela = tk.Tk()
janela.title("Visualização da Informação") 
janela.geometry("300x300") 

# Label com minhas infos
label = tk.Label(janela, text="Projeto Pratico de Visualização da Informação\nNome: Eduardo Bresolin\nCurso: Ciências da Computação'\nPolo: Caxias do Sul ")
label.pack(pady=10)

# Pizza
botao_1 = tk.Button(janela, text="Diferença de Sexos (Grafico Pizza)", command=Pizza)
botao_1.pack(pady=5)

# Barra
botao_2 = tk.Button(janela, text="Diferença de Etnias (Grafico de Barras)", command=Barra)
botao_2.pack(pady=5)

# Linha
botao_3 = tk.Button(janela, text="Crescimento Populacional (Grafico de Linha)", command=Linha)
botao_3.pack(pady=5)
 

# Meus creditos 
creditos = tk.Label(janela, text="18/05/2024")
creditos.pack(pady=10)

# loop que volta pra janela
janela.mainloop()