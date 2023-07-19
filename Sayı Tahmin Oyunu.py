from random import randint
print("SAYI TAHMİN OYUNU")
c=5
b=randint(0,100)
while c>0:
    k=input("0-100 arasında bir sayı tuşlayın: ")
    try:
        k = int(k)
    except:
        print("LÜTFEN SADECE SAYI TUŞLAYINIZ")
        continue
    if k>b:
        print("Daha küçük bir sayı girin")
        c=c-1
        print("Kalan canınız :",c)
        continue
    elif k<b:
        print("Daha büyük bir sayı girin")
        c = c - 1
        print("Kalan canınız :", c)
        continue
    else:
        print("KAZANDINIZ")
        break
if c==0:
    print("KAYBETTİNİZ")
    print("BİLGİSAYARIN SEÇTİĞİ SAYI :",b)