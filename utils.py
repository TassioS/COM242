#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *

#Selecionar diretorio
def selectDir():
    root = Tk()
    root.withdraw()
    txt = filedialog.askdirectory()
    root.destroy()
    return(txt)

#Conferir se ja existe um diretorio
def checkDir():
    arq = open("dir.txt","r")
    txt = arq.read()
    arq.close()
    if not txt:
        return False
    else:
        return txt

#Salvar novo diretorio
def saveDir(path):
    arq = open("dir.txt","w")
    arq.write(path)

def confirmaDir(path):
    MsgBox = messagebox.askquestion ('Confirmar diretório','O diretorio para compartilhamento de arquivos esta correto?\n'+path,icon = 'warning')
    if MsgBox == 'no':
        messagebox.showinfo('Selecionar novo diretório','Favor selecionar o diretório correto.')
        saveDir(selectDir())