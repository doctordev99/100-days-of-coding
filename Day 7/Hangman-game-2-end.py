#Bosqich 2

import random

word_list = ["olma", "daftar", "tuya"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, javob: {chosen_word}.')
taxmin = input("Bir harf taxmin qiling: ").lower()
display = []

# for n in chosen_word:
#   display.append("_")
  
# Bu yerda biz boshqa yo'l bilan ham kodni yozishimiz mumkin
# append() metodi o'rniga += ishlatish ham mumkin
for _ in range(len(chosen_word)):
  display += "_"

# harf_location = 0
# for harf in chosen_word:
#   if harf == taxmin:
#     display[harf_location] = harf
#   else:
#     harf_location += 1

# Yuqoridagi kodni boshqa versiyada yozib ko'ramiz
# len(chosen_word) ni bitta o'zgaruvchiga biriktiramiz
harf_soni = len(chosen_word)
for position in range(harf_soni):
  harf = chosen_word[position]
  if harf == taxmin:
    display[position] = harf
  
print(display)
