import psutil

def size():
    return roud(psutil.virtual_memory().total/(1024*1024*1024),1)
def porcent():
    return psutil.virtual_memory().percent
def free():
    return round(psutil.virtual_memory().free/(1024*1024*1024),1)
def used():
    return psutil.virtual_memory().used
