#Bosqich 4
# Yechim

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

game_is_on = True
word_list = ["olma", "daftar", "tuya"]
chosen_word = random.choice(word_list)
harflar_soni = len(chosen_word)

hayot = 6
#Testing code
print(f'Pssst, javob: {chosen_word}.')

#Bo'sh ro'yxat yaratish
display = []
for _ in range(harflar_soni):
    display += "_"

while game_is_on: 
  taxmin = input("Bir harf taxmin qiling: ").lower()
  
  for position in range(harflar_soni):
    harf = chosen_word[position]
    if harf == taxmin:
      display[position] = harf
    
  if taxmin not in chosen_word:
    hayot -= 1
  
  if hayot == 0:
    game_is_on = False
    print("Mag'lub bo'ldingiz")
    
  print(f"{' '.join(display)}")

  if "_" not in display:
      game_is_on = False
      print("G'alaba qozondingiz")
    
  print(stages[hayot])
