#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import filedialog,messagebox,Tk,Label,Toplevel
import os
import json
import socket
import tkinter as tk
from Pyro4  import naming,Proxy
import Pyro4
from ftplib import FTP


#Selecionar diretorio
def selectDir():  
    #root = Tk()
    #root.withdraw()
    txt = filedialog.askdirectory()
    #root.destroy()
    return(txt)

#Conferir se ja existe um diretorio
def checkDir():
    dados = abrirJson()
    #Se nao existir diretorio: Seleciona um novo. Se existir: Confirme se está correto.
    if not dados['filial'][getFilialPos()]['diretorio']:
        saveDir(selectDir())
    else:
        confirmaDir(dados)

#Salvar novo diretorio
def saveDir(path):   
    dados = abrirJson()
    dados['filial'][getFilialPos()]['diretorio'] = path
    salvarJson(dados)

def confirmaDir(dados):
    #root = Tk()
    #root.withdraw()
    MsgBox = messagebox.askquestion ('Confirmar diretório','O diretorio para compartilhamento de mídias esta correto?\n'+dados['filial'][getFilialPos()]['diretorio'],icon = 'warning')
    if MsgBox == 'no':
        messagebox.showinfo('Selecionar novo diretório','Favor selecionar o diretório correto.')
        txt = selectDir()
        saveDir(txt)
    else:
        return
    
def listaMidias():
    jsonL = abrirJson()
    lista = os.listdir(jsonL['filial'][getFilialPos()]['diretorio'])
    return lista

def getDir():
    jsonL = abrirJson()
    return jsonL['filial'][getFilialPos()]['diretorio']

def abrirJson():
    with open('dados.json','r') as json_file:
        jsonL = json.load(json_file)
        json_file.close()
        return jsonL
    
def salvarJson(dados):
    with open ('dados.json','w') as json_file:
        json.dump(dados,json_file)
        json_file.close()


def iniciaDir():
    #checando se existe diretorio definido
    checkDir()
  
def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    ip_local = s.getsockname()[0]
    return ip_local

def getFilialPos():
    jsonL = abrirJson()
    for i,filial in enumerate(jsonL['filial']):
        if filial['ip']  ==  getIP():
            return i

def pyroBusca(filial):
    try:
        ns = Pyro4.locateNS(filial['ip'],filial['pyroPort'])
        uri = ns.lookup(filial['ip'])
        metodos = Pyro4.Proxy(uri)
        return metodos.getListaMidias()

    except Exception as e:
        print(str(e))
        return 0
    
  
def selecionaMidia(filial):
    print(filial)

def baixaMidia(nomeMidia,filial):
    ftp = FTP('')
    ftp.connect('localhost',1026)
    ftp.login()
    
    tmp_a = os.getcwd()
    os.chdir(abrirJson['filial'][getFilialPos]['diretorio'])
    for midia in nomeMidia:
        arqLocal = open(midia, 'wb')
        ftp.retrbinary('RETR ' + midia, arqLocal.write, 1024)
        arqLocal.close()
    os.chdir(tmp_a)
    ftp.quit()