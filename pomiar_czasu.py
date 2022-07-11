import time
def measure_time(func,*args,**kwargs):
    start = time.time()
    for i in range(1000):
        func(*args,**kwargs)
    end = time.time()
    return end - start

def silnia(a):
    if a == 1:
        return 1
    else:
        return a*silnia(a-1)

x = 10
