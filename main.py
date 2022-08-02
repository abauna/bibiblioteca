# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter as tk
def salva_emp(a,b):
   print("nome",a)
   print("autor",b)
   dat=1
   pass
def salva_dev(a,b):
   print("aluno",a)
   print("livro",b)
   dat = 1
   pass
def salva_alu(a,b,c,d,e):
   print("nomel",a)
   print("ctr",d)
   print("telefone", e)
   print("nome",c )
   print("autor", b)
   pass
def salva_liv(a,b):
   print("nome",a)
   print("autor",b)
   pass
def listar():
   pass
def cadlivro(fl,n,t,c):
   newWindow = tk.Toplevel(app)
   labelExample = tk.Label(newWindow, text="Nome")
   labelExample.pack()
   entrada = tk.Entry(newWindow, font="arial 15 bold")
   entrada.pack()
#   print("nome:",entrada.get)
   label = tk.Label(newWindow, text="autor")
   label.pack()
   entrad = tk.Entry(newWindow, font="arial 15 bold")
   entrad.pack()
   #botao = Button(janela, text="Rodar código", command=lambda: querypg(codigo.get()))
   #botao.grid(column=0, row=2)
   if(fl):
      buttonExample = tk.Button(newWindow, text="proxima",command=lambda: salva_liv(entrada.get(),entrad.get()))
      buttonExample.pack()
   else:
      buttonExample = tk.Button(newWindow, text="proxima", command=lambda: salva_alu(entrada.get(), entrad.get(),n,t,c))
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
   buttonExample = tk.Button(newWindow, text="concluir",command=lambda: salva_emp(entrada.get(),entrad.get()))
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
   buttonExample = tk.Button(newWindow, text="concluir",command=lambda: salva_dev(entrada.get(),entrad.get()))
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
   buttonExample = tk.Button(newWindow, text="proxima", command=lambda :cadlivro(False,entrada.get(),entrad.get(),entra.get()))
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
buttonb = tk.Button(app, text="Cadastar o livro", command=lambda: cadlivro(True,0,0,0))
buttonc = tk.Button(app,text="emprestar",command=emprestar)
buttond = tk.Button(app,text="devolver",command=devolver)
buttone = tk.Button(app,text="listar",command=listar)
buttona.pack()
buttonb.pack()
buttonc.pack()
buttond.pack()
buttone.pack()
app.mainloop()