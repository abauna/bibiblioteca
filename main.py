# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import shutil
import tkinter as tk
from datetime import datetime
from datetime import date
from PIL import Image, ImageTk

def lista_t(parametro):
    lista = []
    arquivo=open(parametro,"r")
    nomes = arquivo.readlines()
    for nome in nomes:
        lista.append(nome)
        print(nome)
    return lista
    pass
def atualiza_l(nome):
    print("entrou")
    listanova = []
    arquivo=open("lista_de_emprestimo.txt","r")
    nomes = arquivo.readlines()
    for nomen in nomes:
        if nome in nomen:
            print("");
        else:
            listanova.append(nomen);
    arquivo.close()
    arquivo = open("lista_de_emprestimo.txt", "w")
    arquivo.writelines(listanova)
    arquivo.close()
    listar()
    pass
def verifica( string1):
   print("alunos")
   lista = 'lista_de_alunos.txt'
   file1 = open(lista, "r")
   readfile = file1.read()
   if string1 in readfile:
      file1.close()
      print("achou")
      return 0
   else:
      file1.close()
      return 1
   pass
def erro(param):

   newWindow = tk.Toplevel(app)
   param="erro : "+param
   labelExample = tk.Label(newWindow, text=param)
   buttonExample = tk.Button(newWindow, text="ok", command=newWindow.destroy)
   labelExample.pack()
   buttonExample.pack()
   print(param)
   pass
def verifica_d(param):
   try:
      f = open('livros dentro/'+param+'.txt')
      f.close()
      return 1
   except:
      print("dddd")
      erro('livro nao encontrado '+param)
      return 0
   pass
def salva_emp(newWindow,a,b):
   if(b==""):
      erro("colocar nome do livro")
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
      newWindow.destroy()
   pass
def salva_dev(a,b):
    if (b == ""):
        erro("colocar nome do livro")
    elif (a == ""):
        erro("colocar nome")
    elif (verifica_d((b))):
        erro("livro  esta na escola")
    elif (verifica(a)):
        erro("aluno nao encontrado")
    else:
       print("aluno",a)
       print("livro",b)
       arquivo = open('lista_de_emprestimo.txt', 'a')
       atualiza_l(a)
       desti = 'livros dentro/' + b + '.txt'
       source = 'livros fora/' + b + '.txt'
       #joao & arte 08/16/2022, 18:08:46
       shutil.move(source, desti)
       app.destroy();
    pass
def salva_alu(newWindowa,c,d,e):
   print("ctr",d)
   print("telefone", e)
   print("nome",c )
   if (0==(verifica(c))):
      erro("ja tem esse nome")
   else:
      arquivo = open('lista_de_alunos.txt', 'a')
      arquivo.write(c+" & "+d+" & "+e+"\n")
      arquivo.close()
      cadlivro(newWindowa)

   pass
def salva_liv(newWindow,new,a,b):
    if (b == ""):
        erro("colocar nome do livro")
    elif (a == ""):
        erro("colocar nome")
    else:
       print("nome",a)
       print("autor",b)
       arquivo = open('lista_de_livros.txt', 'a')
       arquivo.write(a+" & "+b+"\n")
       arquivo.close()
       arquivo = open('livros dentro/'+a+'.txt', 'a')
       arquivo.write("autor: " + b + "\n")
       arquivo.close()
       new.destroy()
       newWindow.destroy()
    pass
def listar():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text="listas")
    buttonExample1 = tk.Button(newWindow, text="lista livros totais", command=listarlivros)
    buttonExample2 = tk.Button(newWindow, text="lista empestimos em abreto", command=listaremp)
    buttonExample3 = tk.Button(newWindow, text="lista alunos cadastrados", command=listaralunos)
    buttonExample4 = tk.Button(newWindow, text="fechar", command=newWindow.destroy)
    labelExample.pack()
    buttonExample1.pack()
    buttonExample2.pack()
    buttonExample3.pack()
    buttonExample4.pack()
    pass
def listarlivros():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text="lista de livros ao todo da escola\nnome do livro, autor")
    labelExamp = tk.Label(newWindow, text=str(''.join(lista_t("lista_de_livros.txt"))))
    buttonExample = tk.Button(newWindow, text="fechar", command=newWindow.destroy)
    labelExample.pack()
    labelExamp.pack()
    buttonExample.pack()
    pass
def listaralunos():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text="lista de alunos da escola\nnome do aluno, ctr, telefone")
    labelExamp = tk.Label(newWindow, text=str(''.join(lista_t("lista_de_alunos.txt"))))
    buttonExample = tk.Button(newWindow, text="fechar", command=newWindow.destroy)
    labelExample.pack()
    labelExamp.pack()
    buttonExample.pack()
    pass
def listaremp():
    newWindow = tk.Toplevel(app)
    labelExample = tk.Label(newWindow, text="lista de livros fora da escola\nnome do aluno, nome do livro,data e hora que pegou")
    labelExamp = tk.Label(newWindow, text=str(''.join(lista_t("lista_de_emprestimo.txt"))))
    buttonExample = tk.Button(newWindow, text="fechar", command=newWindow.destroy)
    labelExample.pack()
    labelExamp.pack()
    buttonExample.pack()
    pass
def cadlivro(newWindowa):
   newWindow = tk.Toplevel(app)
   labelExample = tk.Label(newWindow, text="Nome")
   labelExample.pack()
   entrada = tk.Entry(newWindow, font="arial 15 bold")
   entrada.pack()
   label = tk.Label(newWindow, text="autor")
   label.pack()
   entrad = tk.Entry(newWindow, font="arial 15 bold")
   entrad.pack()

   buttonExample = tk.Button(newWindow, text="proxima",command=lambda: salva_liv(newWindow,newWindowa,entrada.get(),entrad.get()))
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
   buttonExample = tk.Button(newWindow, text="concluir",command=lambda: salva_emp(newWindow,entrada.get(),entrad.get()))
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
   buttonExample = tk.Button(newWindow, text="proxima", command=lambda :salva_alu(newWindow,entrada.get(),entrad.get(),entra.get()))
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

app.configure( )
newWindow = tk.Toplevel(app)
newWindow.destroy()
buttona = tk.Button(app,text="Cadastrar aluno",width=15,height=2, command=cadaluno ,fg="black")
buttonb = tk.Button(app, text="Cadastar o livro",width=15,height=2, command=lambda: cadlivro(newWindow))
buttonc = tk.Button(app,text="emprestar",width=15,height=2,command=emprestar)
buttond = tk.Button(app,text="devolver",width=15,height=2,command=devolver)
buttone = tk.Button(app,text="detalhes",width=30,height=2,command=listar)
buttona.grid(row=1,column=0, padx= 10, pady=10)
buttonb.grid(row=1,column=1, padx= 10, pady=10)
buttonc.grid(row=2,column=1, padx= 10, pady=10)
buttond.grid(row=2,column=0, padx= 10, pady=10)
buttone.grid(row=3,column=0, columnspan=2)
app.mainloop()
