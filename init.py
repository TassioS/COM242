#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import utils
import subprocess
import multiprocessing
from tkinter import *
from tkinter import ttk

def iniciaPyroServer():
    comando = "connect.py"
    subprocess.call(['python',comando])

def iniciaFtpServer():
    comando = "ftpServer.py"
    subprocess.call(['python',comando])

window = Tk()


def exibeMidia(filial,top):
        windowLista = Toplevel(top)
        windowLista.geometry("300x300")
        lb = Label(windowLista,text="Midias Disponíveis em: "+filial['name'])
        midias = []
        i= 0
        def addMidias():
            midias.append(cmb.get())
            listb1.insert(i,cmb.get())
            self.i = i+1
            
        btn1 = Button(windowLista,text="Adicionar",command=addMidias)
        
        listb1 = Listbox(windowLista)
        cmb = ttk.Combobox(windowLista)
        
        
        retorno = utils.pyroBusca(filial)
        if(retorno != 0):
            cmb.configure(values=retorno)
        else:
            cmb.configure(values=['Erro ao buscar midias'])

        btn = Button(windowLista,text="Baixar",command=lambda arg=midias,arg1=filial: utils.baixaMidia(arg,arg1))
        
        
        lb.pack()
        btn1.pack()
        cmb.current(0)
        cmb.pack()
        listb1.pack()
        btn.pack()
        windowLista.mainloop()
        

def midias():
    windowFilial = Toplevel(window)
    windowFilial.geometry("400x250")    
    Label(windowFilial, text="Midias disponíveis").pack()
    jsonL = utils.abrirJson()['filial']
    for filial in jsonL:
        if filial['ip'] != utils.getIP():
            Button(windowFilial,text= filial['name'],command=lambda arg=filial,arg1=windowFilial: exibeMidia(arg,arg1)).pack()
    windowFilial.mainloop()


def main():
    window.geometry("500x300")
    
    Label1 = Label(window, text="Compartilhamento multimídia",font=("arial",16,"bold")).pack()
      
    b1 = Button(window,text="Checar Diretório",command=utils.iniciaDir).pack()

    b2 = Button(window,text="Buscar Midias",command=midias).pack()
    
    b3 = Button(window,text="Fechar",command=window.destroy).pack()
    
    pyroProcess = multiprocessing.Process(target = iniciaPyroServer)
    pyroProcess.start()
    
    ftpProcess = multiprocessing.Process(target = iniciaFtpServer)
    ftpProcess.start()

    
    #ftpProcess.join()
    
    window.mainloop()
    #pyroProcess.join()
    pyroProcess.terminate()
    ftpProcess.terminate()
#Define a função main
if __name__ == "__main__":
    main()
        