#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import filedialog,messagebox,Tk
import os

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
    root = Tk()
    root.withdraw()
    MsgBox = messagebox.askquestion ('Confirmar diretório','O diretorio para compartilhamento de mídias esta correto?\n'+path,icon = 'warning')
    if MsgBox == 'no':
        messagebox.showinfo('Selecionar novo diretório','Favor selecionar o diretório correto.')
        txt = selectDir()
        saveDir(txt)
        return txt
    else: return path
    
def listaMidias(path):
    lista = os.listdir(path)
    return lista