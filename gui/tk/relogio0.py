"""
O mais breve programa Tkinter que faz alguma coisa, escrito da forma
mais breve que eu consegui, mas necessariamente a melhor.
"""

import tkinter
from time import strftime

def tic():
    rel['text'] = strftime('%H:%M:%S')

def tac():
    tic()
    rel.after(1000, tac)

rel = tkinter.Label()
rel.pack()
rel['font'] = 'Helvetica 120 bold'
rel['text'] = strftime('%H:%M:%S')

tac()

# no console, esta linha é desncessária
rel.mainloop()  # inicia o loop de eventos do Tkinter
