import tkinter as tk
from tkinter import N, W, E, S
from tkinter import ttk
import itertools
import base64

def xor(senha:bytes, conteudo:bytes):
    pares = zip(itertools.cycle(senha), conteudo)
    return bytes(a ^ b for a, b in pares)

class Janela(ttk.Frame):

    def __init__(self, pai):
        super().__init__(pai, padding="3 3 12 12")
        self.pack()
        self.senha = tk.StringVar()
        ttk.Label(self, text='senha:').grid(column=1, row=2, sticky=E)
        self.botao = ttk.Button(self, text='Cifrar', command=self.cifrar)
        self.botao.grid(column=3, row=2, sticky=W)
        ttk.Entry(self, width=30, textvariable=self.senha, show='*').grid(
                column=2, row=2, sticky=(W, E))
        self.texto = tk.Text(self, width=80, height=30)
        self.texto.grid(column=1, row=1, columnspan=3, sticky=(W, E))

        for controle in self.winfo_children():
            controle.grid_configure(padx=5, pady=5)

    def cifrar(self):
        if self.botao['text'] == 'Cifrar':
            entrada = bytes(self.texto.get('1.0', 'end').rstrip(), encoding='utf-8')
            senha = bytes(self.senha.get(), encoding='utf-8')
            saida = xor(senha, entrada)
            self.texto.delete('1.0', 'end')
            self.texto.insert('1.0', base64.b64encode(saida))
            self.botao['text'] = 'Decifrar'
        else:
            entrada = bytes(base64.b64decode(self.texto.get('1.0', 'end')))
            senha = bytes(self.senha.get(), encoding='utf-8')
            saida = xor(senha, entrada)
            self.texto.delete('1.0', 'end')
            self.texto.insert('1.0', str(saida, encoding='utf-8'))
            self.botao['text'] = 'Cifrar'



app = tk.Tk()
app.title('Ofuscador de textos')
janela = Janela(app)
app.mainloop()


