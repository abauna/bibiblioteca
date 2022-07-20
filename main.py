# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk

def listar():
   pass
def cadlivro():
   newWindow = tk.Toplevel(app)
   labelExample = tk.Label(newWindow, text="Nome")
   labelExample.pack()
   entrada = tk.Entry(newWindow, font="arial 15 bold")
   entrada.pack()
   label = tk.Label(newWindow, text="autor")
   label.pack()
   entrad = tk.Entry(newWindow, font="arial 15 bold")
   entrad.pack()
   buttonExample = tk.Button(newWindow, text="proxima",command=newWindow.destroy)
   buttonExample.pack()
   buttonExample = tk.Button(newWindow, text="cancelar", command=newWindow.destroy)
   buttonExample.pack()
   pass

def emprestar():
   newWindow = tk.Toplevel(app)
   labelExample = tk.Label(newWindow, text="aluno")
   labelExample.pack()
   entrada = tk.Entry(newWindow, font="arial 15 bold")
   entrada.pack()
   label = tk.Label(newWindow, text="livro")
   label.pack()
   entrad = tk.Entry(newWindow, font="arial 15 bold")
   entrad.pack()
   buttonExample = tk.Button(newWindow, text="concluir",command=newWindow.destroy)
   buttonExample.pack()
   buttonExample = tk.Button(newWindow, text="cancelar", command=newWindow.destroy)
   buttonExample.pack()
   pass
def devolver():
   newWindow = tk.Toplevel(app)
   labelExample = tk.Label(newWindow, text="aluno")
   labelExample.pack()
   entrada = tk.Entry(newWindow, font="arial 15 bold")
   entrada.pack()
   label = tk.Label(newWindow, text="livro")
   label.pack()
   entrad = tk.Entry(newWindow, font="arial 15 bold")
   entrad.pack()
   label = tk.Label(newWindow, text="data")
   label.pack()
   buttonExample = tk.Button(newWindow, text="concluir",command=newWindow.destroy)
   buttonExample.pack()
   buttonExample = tk.Button(newWindow, text="cancelar", command=newWindow.destroy)
   buttonExample.pack()
   pass

def cadaluno():
   newWindow = tk.Toplevel(app)
   labelExample = tk.Label(newWindow, text="Nome")
   labelExample.pack()
   entrada = tk.Entry(newWindow, font="arial 15 bold")
   entrada.pack()
   label = tk.Label(newWindow, text="ctr")
   label.pack()
   entrad = tk.Entry(newWindow, font="arial 15 bold")
   entrad.pack()
   labele = tk.Label(newWindow, text="telefone")
   labele.pack()
   entra = tk.Entry(newWindow, font="arial 15 bold")
   entra.pack()
   buttonExample = tk.Button(newWindow, text="proxima", command=cadlivro)
   buttonExample.pack()
   buttonExample = tk.Button(newWindow, text="cancelar", command=newWindow.destroy)
   buttonExample.pack()
   pass
def createNewWindow():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text = "New Window")
    buttonExample = tk.Button(newWindow, text = "New Window button",command=createNewWindow)
    labelExample.pack()
    buttonExample.pack()
    pass
app = tk.Tk()
buttona = tk.Button(app,text="Cadastrar aluno",command=cadaluno)
buttonb = tk.Button(app,text="Cadastar o livro",command=cadlivro)
buttonc = tk.Button(app,text="emprestar",command=emprestar)
buttond = tk.Button(app,text="devolver",command=devolver)
buttone = tk.Button(app,text="listar",command=listar)
buttona.pack()
buttonb.pack()
buttonc.pack()
buttond.pack()
buttone.pack()
app.mainloop()