"""
Crie o algoritmo para o cronômetro. Depois de criado,
implemente com tkinter.

Quando segundo for maior do que 9, dezena de segundo
recebe 1 e segundo reseta
s

Quando dezena de segundo for maior do que 59,
minuto recebe 1 e dezena de segundo reseta
ds

Quando minuto for maior do que 9, dezena de minuto
recebe 1 e minuto reseta
m

Quando dezena de minuto for maior do que 59,
hora recebe 1 e dezena de minuto reseta
dm

Quando hora for maior do que 9, dezena de hora
recebe 1 e hora reseta
h

Quando dezena de hora for maior do que 59,
o cronômetro para para.
dh

import time


def c():
    seg = 0
    dez_seg = 0
    
    mi = 0
    dez_mi = 0
    
    hor = 0
    dez_hor = 0
    
    while dez_hor < 100:
        print(f"{dez_hor}{hor}:{dez_mi}{mi}:{dez_seg}{seg}", end="\r")
        
        if seg > 9:
            seg = 0
            dez_seg = 1
        
        if dez_seg >= 60:
            mi = 1
            dez_seg = 0
        
        seg += 1
        time.sleep(1)

c()
"""

