#--------------------------------------------------------------------
#       Modulos externos que precisam ser instalados antes de rodar o programa:
#       pip install matplotlib  
# 
#       Projeto feito na versao 3.7.8 do Python
#
#--------------------------------------------------------------------


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

#Executa caso o usuario digite uma opção inválida
def Nada():
 limpar()
 os.system('color 0c')
 print('\n\n    Escolha uma opção valida!!')

#Limpa o console usando o comando CLS do prompt
def limpar():
 os.system('cls')
 os.system('color 0a')
 
#Finaliza o script
def sair():
 limpar()
 print('\n\n    Muito obrigado')
 time.sleep(3)

#Exibe um header com todas opções de graficos disponíveis
def cabecalho():
 print('\n\n     ---------------------------------------------  ')
 print('     | Projeto Pratico de Visualização da Informação ')
 print('     | ')
 print('     | Nome: Eduardo Bresolin')
 print('     | Curso: Ciências da Computação')
 print('     | RGM: 33877751')
 print('     | Polo: Caxias do Sul ')
 print('     ---------------------------------------------\n\n')
 print('     0 : Grafico Pizza')
 print('     1 : Grafico de Barra')
 print('     2 : Grafico de Linhas') 
 print('     3 : Gráfico de Dispersão\n')
 print('     4 : Sair do programa\n\n')
 print('     Selecione um dos modelos de graficos disponíveis que deseja exibir: ')


#Simulação de um SWITCH CASE
opcoes = {
    0:Pizza,        #Pizza    
    1:Barra,        #Barra
    2:Linha,        #Linha
    3:Dispersao,    #Dispersao           
    4:sair,         #Sair do programa
}

#variavel de controle do loop WHILE
loop = 1



while loop == 1:
    limpar()                    #Limpa o console usando o comando CLS do prompt
    cabecalho()                 #Exibe um header com todas opções de graficos disponíveis
    escolha = int(input())      #Obtem a escolha do usuário e converte pra INT

    if escolha == 4:            #Verifica se a opção escolhida é 4 (Sair)
     loop = 0                   #Desativa o loop WHILE
    
    opcoes.get(escolha,Nada)()  #Executa a void selecionada. Caso seja um numero inválido, executa Nada()
    
#------------------------------------------------------------------------------    
    
