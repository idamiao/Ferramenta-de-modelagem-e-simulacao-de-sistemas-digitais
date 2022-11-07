import pandas as pd
import tkinter

import numpy as np

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.figure import Figure


plt.close('all')


root = tkinter.Tk()
root.wm_title("BINARY WAVEFORM")

fig = Figure(figsize=(5, 4), dpi=100)


# Abertura do arquivo

arq_res= open('disp_segment', 'r+')
data = pd.read_csv(arq_res, sep='\t',index_col=False)

header = data.columns.values.tolist()

print(data)


# Numero de linhas e colunas

lin, col = data.shape
print('numero de colunas: ', col)
print('numero de linhas: ', lin)


#Função que constroi uma lista dos dados
lista = []
def constroiLista(col, lin, lista):
    for k in range(0, col):
        coluna = []
        for j in range(0, lin):
            x = data[header[k]][j]
            coluna.append(x)
        lista.append(coluna)





constroiLista(col, lin, lista)

# Converter a lista em um Numpy
lista = np.array(lista)
print(lista)


# Geração do sinal
duração = 32
numero_simbolos = lin
sinal = []
def formaDeOnda(lista):


        for x in lista:
            rand_a = x
            print(rand_a)
            print(type(rand_a))


            "generate signal"
            sig = np.zeros(duração*numero_simbolos)
            id_n = np.where(rand_a == 1)


            for i in id_n[0]:

                temp = int(i*duração)
                sig[temp: temp + duração] = 1
            sinal.append(sig)



formaDeOnda(lista)

# Plotar os gráficos
for h in range(1, col+1):

    ar = fig.add_subplot(col, 1, h)
    ar.plot(sinal[h - 1])
    tit = header[h - 1]
    ar.set_ylabel(tit, fontdict={'fontsize': 8, 'fontweight': 'medium'})




# Desenhando a figura

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



# Ferramentas de Atalho

toolbar = NavigationToolbar2Tk(canvas, root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand = True)


tkinter.mainloop()