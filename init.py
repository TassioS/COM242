#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import utils

def iniciaDir():
    #checando se existe diretorio definido
    diretorio = utils.checkDir()
    
    #Se nao existir diretorio: Seleciona um novo. Se existir: Confirme se está correto.
    if not diretorio:
        utils.saveDir(utils.selectDir())
    else:
        diretorio = utils.confirmaDir(diretorio)
    
    return diretorio
    
#listaItens = utils.listaMidias(diretorio)
    
def main():
    diretorio = iniciaDir()
    
    

#Define a função main
if __name__ == "__main__":
    main()
        