from watchDogs import computer
from watchDogs import cpu
from watchDogs import memoria
from watchDogs import tools
from watchDogs import disk
from watchDogs import network
from  cryptography.fernet import Fernet
from time import sleep
import psutil
import sys


result = sys.argv
#result2 = sys.argv
#result3 = sys.argv
#result4 = sys.argv

print('   _____________________')
print('    PROJETO WATCH DOGS      ')
print('  _____________________')


if len(result) >= 0:
    if result[1] == "--iform" or "--system":
        print('Sistema operacional:', computer.iform())
        print('Versão:', computer.SO_Version())

if len(result) >= 0:
    if result[1] == "--name_r":
        print('Nome de rede:', computer.name_Rede())


if result[1] == "--arc":
        print('Arquitetura:', computer.arctetura())


if result[1] == "--cpu":
    if len(result) == 4 and result[2] == '//porcent' and int(result[3]) >= 1:
        for x in range(int(result[3])):
            consume = cpu.porcent()
            print(consume)
            print('________________________________________')


elif len(result) == 4 and result[2] == 'benchmarking' and int(result[3]) >= 1:
    print('Analisando o uso da CPU...'.sleep)     # benchmarking
    consume = cpu.porcent()
    media = 0
    for y in range(int(result[3])):
        media +=  consume.user + consume.system
        media = media/int(result[3])
    else:
        print('Processador:', computer.cpu())
        print('Velocidade:', cpu.freq(), "GHz")
        print('Cores:', cpu.cores())
        print("Cores Fisicos:", cpu.phyCores())

elif result[1] == 'memory' or '-m':
    if str(result).find("size" or '--memory') > 0 :
        print('memory', memory.size(), "GB")
    if str(result).find("percent") > 0:
        print('consume memory', memory.porcent(), '%')
    if str(result).find("free") > 0 :
            print('memoria livre', memory.free())
    if str(result).find("used") > 0:
            print('memoria usada', memory.used())

elif result[1] == 'disk' or '--d':
    if str(result).find("disk" or "--d") > 0:
        disklist = disk.info()
        i = 0
        print('N de disco:', len(disklist))

            #i = 1
        while i < len(disklist):
            print(________________________)
            print('Ponto de montagem:', disklist[i].mountpoint)
            print('Sistema de arquivo:', disklist[i].fstype)
            i += 1

elif result[1] == 'network':
    if str(result).find('bytes') > 0:
        bytesNetwork = network.rede()

        print('Bytes enviados:', round(bytesNetwork.bytes_sent/(1024*1024*1024), 1))
        prin('Bytes recebidos:', round(bytesNetwork.bytes_recv/(1024*1024*1024), 1))
    if str(result).find('pack') > 0:
        packNetwork = network.rede()

        print('Packs enviados:', round(packNetwork.packets_sent/(1024*1024*1024), 1))
        print('Packs recebidos:', round(packNetwork.packets_recv/(1024*1024*1024), 1))

elif result[1] == 'traffic' or '--t':
    if str(result).find('errin'):
        errinTraffc = traffic.rede()
        print('Numeros de erros de recebimento:', errinTraffc.errin)
        print('Numero total de erros de envio:', errinTraffc.errout)


elif result[1] == 'shutdown -s':
    print('Desligando a maquina...')
    tools.shutdown
elif result[1] == 'shutdown -r':
    prit('Reiniciando a maquina...')
    tools.reboot
else:
    pass
if result[1] == "help":
    print("Para informações do sistema (--iform ou --system,-- name_r, --arc, --cpu) ")




from cryptgraphy import Frenet




#if result[1] == '//cryptography__' or '-cgp':
#    print('_______________')
#    print('  criptografia ')
#    print('_______________')
#pass

#toke = input('digite a menssagem:')
#key = fernet.generate_key()
#f = Fernet(key)
#token = f.encrypt(toke)
#print(computer.inform(), computer.SO_Version)
#print(computer.name_Rede())
#print(computer.cpu())
#print(computer.arc())
#print(computer.Linux())
