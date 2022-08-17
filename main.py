# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import shutil
import tkinter as tk
from datetime import datetime
from datetime import date

from PIL import Image, ImageTk

def verifica( string1):
   print("alunos")
   lista = 'lista_de_alunos.txt'
   file1 = open(lista, "r")
   readfile = file1.read()
   if string1 in readfile:
      file1.close()

      return 0
   else:
      file1.close()
      return 1
   pass
def erro(param):
   print("erro no "+param)
   pass
def verifica_d(param):
   try:
      f = open('livros dentro/'+param+'.txt')
      f.close()
      print('livro encontrado ', param)
      return 1
   except:
      print('livro nao encontrado ',param)
      return 0
   pass
def salva_emp(a,b):

   if(b==""):
      erro("colocar autor")
   elif (a==""):
      erro("colocar nome")
   elif(0==verifica_d((b))):
      erro("livro nao disponivel")
   elif(verifica(a)):
      erro("aluno nao encontrado")
   else:
      print("nome", a)
      print("autor", b)
      now = datetime.now()
      data = now.strftime("%m/%d/%Y, %H:%M:%S")
      source = 'livros dentro/' + b + '.txt'
      desti = 'livros fora/' + b + '.txt'
      shutil.move(source, desti)
      arquivo = open('livros fora/' + b + '.txt', 'a')
      arquivo.write(a + "\n")
      arquivo.close()
      arquivo = open('lista_de_emprestimo.txt', 'a')
      arquivo.write(a + " & " + b+ " "+data+"\n")
      arquivo.close()
   pass


def atualiza_emp(nome):
   #   nome="joao & arte 08/16/2022, 18:08:46"
   arquivo = open('lista_de_emprestimo.txt', 'r')
   arquivo2 = open('lista_de_emprestimo.txt', 'w')
   linhas = arquivo.readlines()
   nlin=" "
   for linha in linhas:
       if nome in linha:
          print("achou")
       else:
          nlin.__add__(linha)
          print("nao achou")
   arquivo2.write(nlin)
   arquivo2.close()
   arquivo.close()
def salva_dev(a,b):
   print("aluno",a)
   print("livro",b)
   arquivo = open('lista_de_emprestimo.txt', 'a')
   atualiza_emp(a)
   desti = 'livros dentro/' + b + '.txt'
   source = 'livros fora/' + b + '.txt'
   #joao & arte 08/16/2022, 18:08:46
   shutil.move(source, desti)

   pass
def salva_alu(a,b,c,d,e):
   print("nomel",a)
   print("ctr",d)
   print("telefone", e)
   print("nome",c )
   print("autor", b)
   if (0==(verifica(c))):
      erro("ja tem esse nome")
   else:
      arquivo = open('lista_de_alunos.txt', 'a')
      arquivo.write(c+" & "+d+" & "+e+"\n")
      arquivo.close()
      salva_liv(a,b)
   pass
def salva_liv(a,b):
   print("nome",a)
   print("autor",b)
   arquivo = open('lista_de_livros.txt', 'a')
   arquivo.write(a+" & "+b+"\n")
   arquivo.close()
   arquivo = open('livros dentro/'+a+'.txt', 'a')
   arquivo.write("autor: " + b + "\n")
   arquivo.close()
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
   label = tk.Label(newWindow, text="autor")
   label.pack()
   entra = tk.Entry(newWindow, font="arial 15 bold")
   entra.pack()
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
app.geometry("300x700")
#Marca d'água 2.png
app.configure( )
buttona = tk.Button(app,text="Cadastrar aluno",width=15,height=2, command=cadaluno ,fg="black")
buttonb = tk.Button(app, text="Cadastar o livro",width=15,height=2, command=lambda: cadlivro(True,0,0,0))
buttonc = tk.Button(app,text="emprestar",width=15,height=2,command=emprestar)
buttond = tk.Button(app,text="devolver",width=15,height=2,command=devolver)
buttone = tk.Button(app,text="detalhes",width=30,height=2,command=listar)
#tk.Label(app, image=tkimage).pack()
#img_label.grid(row=0,column=0,padx= 10, pady=10)
buttona.grid(row=1,column=0, padx= 10, pady=10)
buttonb.grid(row=1,column=1, padx= 10, pady=10)
buttonc.grid(row=2,column=1, padx= 10, pady=10)
buttond.grid(row=2,column=0, padx= 10, pady=10)
buttone.grid(row=3,column=0, columnspan=2)
app.mainloop()
