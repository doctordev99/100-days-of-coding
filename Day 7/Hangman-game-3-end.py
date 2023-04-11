#Bosqich 3
# Yechim

import random

word_list = ["olma", "daftar", "tuya"]
chosen_word = random.choice(word_list)
harflar_soni = len(chosen_word)

#Testing code
print(f'Pssst, javob: {chosen_word}.')

#Bo'sh ro'yxat yaratish
display = []
for _ in range(harflar_soni):
    display += "_"

game_is_on = True
while game_is_on:
  
  taxmin = input("Bir harf taxmin qiling: ").lower()
  for position in range(harflar_soni):
    harf = chosen_word[position]
    if harf == taxmin:
      display[position] = harf
    
  print(display)

  if "_" not in display:
    game_is_on = False
    
print("G'alaba")
