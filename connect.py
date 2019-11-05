import Pyro4
import utils
import subprocess

#Ligando o nameserver rodando script no terminal(Onde são armazenados as classes e metodos expostos)
"""comando = "pyro4-ns -n "+utils.getIP()+" -p 8111"
subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=None, shell=True)"""

@Pyro4.expose
class metodos():
    def getListaMidias(self):
        return utils.listaMidias()

jsonL = utils.abrirJson()
#Gera um daemon(Servidor)
daemon = Pyro4.Daemon(utils.getIP())
#Localiza Nameserver
ns = Pyro4.locateNS(utils.getIP(),jsonL['filial'][0]['pyroPort'])
#Registra a classe metodos no com um URI(assinatura para a localizar o objeto) no  daemon
uri = daemon.register(metodos)
#registra o uri no nameserver
ns.register(utils.getIP(), uri)
#Inicia a espera por requisições
daemon.requestLoop()
#Fecha Conexão
daemon.close()


