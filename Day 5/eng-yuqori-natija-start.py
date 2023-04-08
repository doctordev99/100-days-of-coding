talabalar_natijalari = input("Barcha talabalar natijalarini kiriting: ").split()
for n in range(0, len(talabalar_natijalari)):
  talabalar_natijalari[n] = int(talabalar_natijalari[n])

# max() funksiyasi yordamisiz berilgan list ichidagi eng katta sonni aniqlash

eng_yuqori_natija = 0

for natija in talabalar_natijalari:
    if natija > eng_yuqori_natija:
        eng_yuqori_natija = natija

print(eng_yuqori_natija)
