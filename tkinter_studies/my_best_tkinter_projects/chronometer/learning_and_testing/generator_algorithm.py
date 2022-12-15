import time


def gen_alg():
    seg = 0 
    dez_seg = 0 
    mi = 0 
    dez_mi = 0 
    hor = 0 
    dez_hor = 0

    while True:
        if seg >= 9:
            dez_seg += 1
            seg = -1
            
        if dez_seg >= 6:
            dez_seg = 0
            mi += 1
            
        if mi >= 10:
            dez_mi += 1
            mi = 0
            
        if dez_mi >= 6:
            hor += 1
            dez_mi = 0
            
        if hor >= 10:
            dez_hor += 1
            hor = 0
            
        if dez_hor >= 6:
            dez_hor = 0
            hor = 0
            dez_mi = 0
            mi = 0
            dez_seg = 0
            seg = 0
                
        seg += 1
        yield f"{dez_hor}{hor}:{dez_mi}{mi}:{dez_seg}{seg}"


x = gen_alg()
while True:
    print(next(x), end="\r")
    time.sleep(1)

