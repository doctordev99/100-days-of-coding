# Yechim

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    
    #TODO-3: Agar foydalanuvchi raqam/belgi/bo'sh joy kiritsa nima bo'ladi?
      #Matn kodlanganda/dekodlanganda raqam/belgi/boʻshliqni saqlash uchun kodni tuzat olasizmi?
      #masalan, start_text = "3 da uchrashamiz"
      #end_text = "3 • •  • • • • "
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
      
  print(f"Mana {cipher_direction}langan natija: {end_text}")

#TODO-1: Dastur boshlanganda logotipni art.py dan import qiling va chop eting.
from art import logo
print(logo)
#TODO-4: Siz foydalanuvchidan shifrlash dasturini qayta ishga tushirishni xohlaysizmi, deb so'rash yo'lini aniqlay olasizmi?
#masalan, Agar yana xabar jo'natsangiz, “ha” deb yozing. Aks holda "yo'q" deb yozing.
#Agar ular "ha" deb yozsa, ulardan yana yo'nalish/matn/shiftni so'rang va caesar() funksiyasini qayta chaqiring?
#Maslahat: Agar foydalanuvchi “ha” deb yozsa, dasturni bajarishda davom etadigan while tsiklini yaratib koʻring.
should_end = False
while not should_end:  
  direction = input("Shifrlash uchun encode so'zini kiriting, shifrni ochish uchun decode so'zinini kiriting:\n")
  text = input("Matnni kiriting:\n").lower()
  shift = int(input("Shift raqam kiriting:\n"))
  
  #TODO-2: Agar foydalanuvchi alifbodagi harflar sonidan kattaroq raqam kiritsa-chi?
  #Dasturni ishga tushirib, 45  raqamini kiritib ko'ring.
  #Ba'zi kod qo'shing, shunda foydalanuvchi  26 dan kattaroq kiritsa ham dastur ishlashda davom etadi.
  #Maslahat: Modulni (%) qanday ishlatishingiz haqida o'ylab ko'ring.
  shift = shift % 26
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Agar yana xabar jo'natsangiz, ha deb yozing. Aks holda yo\'q deb yozing.\n")
  if result == "yo'q":
    should_end = True
    print("Xayr")
