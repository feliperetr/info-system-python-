import psutil

def rede():
    return psutil.net_io_counters(pernic = True) and psutil.net_io_counters(pernic = False)

def info():
    return psutil.net_connections(kind = 'inet')
