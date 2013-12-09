"""
O mais breve programa Tkinter que faz alguma coisa, escrito
com uma classe para representar a janela principal.
"""

import tkinter
from time import strftime

class Janela(tkinter.Frame):

    def __init__(self, pai):
        super().__init__(pai)
        self.visor = tkinter.Label(self)
        self.visor['font'] = 'Helvetica 120 bold'
        self.pack()
        self.visor.pack()
        self.tac()

    def tic(self):
        self.visor['text'] = strftime('%H:%M:%S')

    def tac(self):
        self.tic()
        self.after(1000, self.tac)


root = tkinter.Tk()
janela = Janela(root)
root.mainloop()  # inicia o loop de eventos do Tkinter
