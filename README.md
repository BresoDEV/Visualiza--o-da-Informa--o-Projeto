#  Documentação do Código Python: Visualização de Dados Demográficos   
#### Descrição do Projeto
Este projeto cria uma aplicação de visualização de dados demográficos usando a biblioteca tkinter para a interface gráfica e matplotlib para a geração de gráficos. A aplicação exibe gráficos de pizza, barras e linhas com base em dados populacionais do Brasil de 1872 a 2022, além de dados de distribuição de sexo e etnias em 2022.

# Requisitos  
- `tkinter`: Incluído na biblioteca padrão do Python.
- `os`: Incluído na biblioteca padrão do Python.
- `time`: Incluído na biblioteca padrão do Python.
- `matplotlib`: Deve ser instalado separadamente.

### Para instalar o matplotlib, execute:

```bash 
pip install matplotlib
```   
### Versão do Python
Este projeto foi desenvolvido na versão 3.7.8 do Python.

# Estrutura do Código
- Importações
```python 
import tkinter as tk
import os  
import time 
import matplotlib.pyplot as plt
```
- `tkinter`: Para criar a interface gráfica.
- `os`: Para operações relacionadas ao sistema operacional (não utilizado diretamente no código).
- `time`: Para funções de atraso (não utilizado diretamente no código).
- `matplotlib.pyplot`: Para criação dos gráficos.  
 
### Dados
```python 
anos = ["1872", "1890", "1900", "1920", "1940", "1950", "1960", "1970", "1980", "1991", "2000", "2010", "2022"]
pop = [9930478, 14333915, 17438434, 30635605, 41236315, 51944397, 70992343, 94508583, 121150573, 146917459, 169872856, 190755799, 203080756]
sexo = ["Homens", "Mulheres"]
sexoN = [104548325, 98532431]
etnia = ["Branca", "Preta", "Amarela", "Parda", "Indigena"]
etniaN = [88252121, 20656458, 850130, 92083286, 1227642]
maisPopulosas = ["Minas Gerais", "São Paulo", "Parana", "Rio Grande do Sul", "Rio de Janeiro", "Bahia"]
maisPopulosasN = [20539989, 44411238, 11444380, 10882965, 16055174, 14141626]
t1 = "Crescimento da População (1872 a 2022)"
t2 = "Ano"
t3 = "População (Milhões)"
```
## Funções de Geração de Gráficos
### Gráfico de Pizza
```python 
def Pizza():
    plt.figure(figsize=(8, 6))
    plt.pie(sexoN, labels=sexo, autopct='%1.1f%%', startangle=140)
    plt.title("Porcentagem de Sexos (2022)")
    plt.axis('equal')
    plt.show()
```  
### Gráfico de Barras
```python 
def Barra():
    plt.figure(figsize=(10, 6))
    plt.bar(etnia, etniaN, color='green')
    plt.ylabel("Milhões")
    plt.title("Etnias (2022)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

```
 
## Gráfico de Linhas
```python 
def Linha():
    plt.figure(figsize=(10, 6))
    plt.plot(anos, pop, marker='o', linestyle='-', color='b')
    plt.xlabel(t2)
    plt.ylabel(t3)
    plt.title(t1)
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
```    


## Interface Gráfica com tkinter
#### Criação da Janela Principal
```python 
janela = tk.Tk()
janela.title("Visualização da Informação")
janela.geometry("300x300")
```
#### Informações do Projeto
```python
label = tk.Label(janela, text="Projeto Pratico de Visualização da Informação\nNome: Eduardo Bresolin\nCurso: Ciências da Computação'\nPolo: Caxias do Sul ")
label.pack(pady=10)
```
#### Botões para Geração de Gráficos
```python
botao_1 = tk.Button(janela, text="Diferença de Sexos (Grafico Pizza)", command=Pizza)
botao_1.pack(pady=5)

botao_2 = tk.Button(janela, text="Diferença de Etnias (Grafico de Barras)", command=Barra)
botao_2.pack(pady=5)

botao_3 = tk.Button(janela, text="Crescimento Populacional (Grafico de Linha)", command=Linha)
botao_3.pack(pady=5)
```
#### Créditos
```python
creditos = tk.Label(janela, text="18/05/2024")
creditos.pack(pady=10)
```
#### Loop Principal
```python
janela.mainloop()
```
 
# Uso
Execute o código em um ambiente Python com a versão `3.7.8` ou superior.
Certifique-se de ter instalado o `matplotlib` conforme descrito na seção de requisitos.
Interaja com a interface gráfica para visualizar os diferentes gráficos clicando nos botões correspondentes.
Este projeto é uma ferramenta prática para a visualização de dados demográficos históricos e contemporâneos do Brasil, permitindo ao usuário explorar informações de maneira interativa e visual.

 
