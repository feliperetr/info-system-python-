import psutil

def veloc():
    return round(psutil.cpu_freq().corrent/1000,1)
def cores():
    return psutil.cpu_count()
def phyCores():
    return psutil.cpu_count(logical=False)
def porcent():
    return psutil.cpu_times_percent(interval=1)
