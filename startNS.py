# -*- coding: utf-8 -*-
import subprocess

comando = "pyro4-ns -n "+utils.getIP()+" -p 8111"
subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=None, shell=True)