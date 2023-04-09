#Password Generator Project
import random
harflar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
raqamlar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
belgilar = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("PyPassword Generatorga xush kelibsiz!")
n_harflar= int(input("Parolingizda nechta harf boʻlishini xohlaysiz?\n"))
n_belgilar = int(input("Parolingizda nechta belgi boʻlishini xohlaysiz?\n"))
n_raqamlar = int(input("Parolingizda nechta raqam boʻlishini xohlaysiz?\n"))

#Oson Level - Paroldagi belgilar ketma-ketligi o'zgarmagan:
#e.g. 4 harf, 2 belgi, 2 raqam = JduE&!91
parol = ""
#n_harflar = 4
for n in range(1, n_harflar + 1):
  # Bu yerda +1 bo'lishiga sabab, range funksiyasi oxirgi raqamni hisobga olmaydi
  # 1 - 4
  # harf = random.choice(harflar)
  #parol = parol + harf 
  # parol += harf
# print(parol)
# Yozgan kodimizni yana ham ixchamlashtiramiz
  parol += random.choice(harflar)

for n in range(1, n_belgilar + 1):
  parol += random.choice(belgilar)

for n in range(1, n_raqamlar + 1):
  parol += random.choice(raqamlar)
  
print(parol)

#Qiyin Level - Paroldagi belgilar ketma-ketligi o'zgarmagan:
#e.g. 4 ta harf, 2 ta belgi, 2 ta raqam = g^2jk8&P
yangi_parol = []

for n in range(1, n_harflar + 1):
  yangi_parol.append(random.choice(harflar))

for n in range(1, n_belgilar + 1):
  yangi_parol.append(random.choice(belgilar))

for n in range(1, n_raqamlar + 1):
  yangi_parol.append(random.choice(raqamlar))

#shuffle() funksiyadi yordamida listdagi belgilar ketma-ketligini o'zgartiramiz
print(yangi_parol) 
random.shuffle(yangi_parol)
print(yangi_parol)

# Endi yangi parolni consolga tartibli qilib chiqaramiz
parol = ""
for p in yangi_parol:
  parol += p
print(parol)
