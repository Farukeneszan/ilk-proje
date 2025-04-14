import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"




def sifreOlusturucu():
    sifre = ""
    for i in range(8):
        sifre += random.choice(karakterler)
    return sifre


