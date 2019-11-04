#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import utils
import subprocess
import multiprocessing
from tkinter import *

def iniciaPyroServer():
    comando = "connect.py"
    subprocess.call(['python',comando])

def iniciaFtpServer():
    comando = "ftpServer.py"
    subprocess.call(['python',comando])

window = Tk()



def midias():
    windowFilial = Toplevel(window)
    windowFilial.geometry("300x200")    
    Label(windowFilial, text="Midias disponíveis").pack()
    
    for filial in utils.abrirJson()['filial']:
        if filial['ip'] != utils.getIP():
            retorno = utils.pyroBusca(filial)
            if retorno == 0:
                continue
            else:
                print(retorno)
    


def main():
    window.geometry("500x300")
    
    Label1 = Label(window, text="Compartilhamento multimídia",font=("arial",16,"bold")).pack()
      
    b1 = Button(window,text="Checar Diretório",command=utils.iniciaDir).pack()

    b2 = Button(window,text="Buscar Midias",command=midias).pack()
    
    b3 = Button(window,text="Fechar",command=window.destroy).pack()
    
    pyroProcess = multiprocessing.Process(target = iniciaPyroServer)
    pyroProcess.start()
    
    #ftpProcess = multiprocessing.Process(target = iniciaFtpServer)
    #ftpProcess.start()

    
    #ftpProcess.join()
    
    window.mainloop()
    pyroProcess.join()
#Define a função main
if __name__ == "__main__":
    main()
        