# Yechim

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Shifrlash uchun encode so'zini kiriting, shifrni ochish uchun decode so'zinini kiriting:\n")
text = input("Matnni kiriting:\n").lower()
shift = int(input("Shift raqam kiriting:\n"))

#TODO-1: Kirish sifatida “matn” va “shift”ni qabul qiluvchi “encrypt” funksiyasini yarating.
def encrypt(plain_text, shift_amount):
  new_word = ""
  for letter in text:
		#new_word = "" for loop ichidan tashqariga oldik
    index_number = alphabet.index(letter)
    new_index_number = index_number + shift
    new_word += alphabet[new_index_number]
  print(f"Shifrlangan habar: {new_word}")

    #TODO-2: "encrypt" funksiyasi ichida "text" ning har bir harfini alifboda siljish miqdori bo'yicha oldinga siljiting va shifrlangan matnni chop eting.
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "Shifrlangan matn: mjqqt"

    ##HINT: Ro'yxatdagi element indeksini qanday olish mumkin:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: Agar siz "zahar" so'zini kodlashga harakat qilsangiz nima bo'ladi?🐛

#TODO-3: Shifrlash funksiyasini chaqiring va foydalanuvchi ma'lumotlarini kiriting. Siz kodni sinab ko'rishingiz va xabarni shifrlashingiz kerak. 
encrypt(plain_text = text, shift_amount = shift)
