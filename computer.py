import platform
     ### funções do sistema do computador

def iform():
    return platform.uname().system

def SO_Version():
    return platform.uname().version

def name_Rede():
    return platform.uname().node

def arctetura():
     return platform.uname().machine

def cpu():
     return platform.uname().processor

def Linux():
     if iform() == 'Linux':
        return platform.linux_distribution()
     else:
        return iform()
