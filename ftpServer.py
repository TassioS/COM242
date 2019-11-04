#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import utils

authorizer = DummyAuthorizer()

jsonL = utils.abrirJson()
for filial in jsonL['filial']:
    authorizer.add_user(filial['ip'],"", utils.getDir(), perm="elradfmw")




handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer((utils.getIP(), 7777), handler)
server.serve_forever()