# Yechim
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Shifrlash uchun encode so'zini kiriting, shifrni ochish uchun decode so'zinini kiriting:\n")
text = input("Matnni kiriting:\n").lower()
shift = int(input("Shift raqam kiriting:\n"))

def encrypt(plain_text, shift_amount):
  shifr_text = ""
  for letter in plain_text:
    index_number = alphabet.index(letter)
    new_index_number = index_number + shift
    shifr_text += alphabet[new_index_number]
  print(f"Shifrlangan habar: {shifr_text}")

#TODO-1: "text" va "shift" ni input sifatida qabul qiladigan "decrypt" deb nomlangan boshqa funksiya yarating.
def decrypt(shifr_text, shift_amount):
  plain_text = ""
  for letter in shifr_text:
    index_number = alphabet.index(letter)
    new_index_number = index_number - shift
    plain_text += alphabet[new_index_number]
  print(f"Shifrlangan habar: {plain_text}")
  
  
  #TODO-2: “decrypt” funksiyasi ichida “text”ning har bir harfini alifbodagi *orqaga* siljish miqdori bo‘yicha siljiting va shifrlangan matnni chop eting.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: "direction" o'zgaruvchisini tekshirish orqali foydalanuvchi xabarni shifrlamoqchimi  yoki yo'qligini tekshiring. Keyin ushbu "direction" o'zgaruvchisiga asoslangan to'g'ri funktsiyani chaqiring.
if direction == "encode":
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  decrypt(shifr_text=text, shift_amount=shift)
else:
  print("Qaytadan urinib ko'ring")
