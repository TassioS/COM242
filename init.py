#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import utils
from tkinter import *

diretorio = utils.checkDir()

if not diretorio:
    utils.saveDir(utils.selectDir())

utils.confirmaDir(diretorio)
