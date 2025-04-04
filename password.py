import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("Şifreniz kaç karakterden oluşsun:   "))

sifre = ""

for i in range(uzunluk):
    sifre = random.choice(karakterler) + sifre
print(sifre)


