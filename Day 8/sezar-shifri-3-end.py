
#Yechim

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Shifrlash uchun encode so'zini kiriting, shifrni ochish uchun decode so'zinini kiriting:\n")
text = input("Matnni kiriting:\n").lower()
shift = int(input("Shift raqam kiriting:\n"))

#TODO-1: Encrypt() va decrypt() funksiyalarini Caesar() deb nomlangan yagona funktsiyaga birlashtiring.

def caesar(user_text, shift_amount, direction):
  word = ""
  if direction == "decode":
      shift_amount *= -1 
  for letter in user_text:
    position = alphabet.index(letter) 
    new_position = position + shift_amount
    word += alphabet[new_position]
  print(f"Shifrlangan soz': {word}")
      

#TODO-2: "text", "shift" va "direction" qiymatlaridan kiritib, Caesar() funktsiyasini chaqiring.
caesar(user_text = text, shift_amount = shift, direction = direction)
