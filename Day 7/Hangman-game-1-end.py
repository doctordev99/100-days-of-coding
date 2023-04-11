# Bosqish 1 
# Yechim
import random

word_list = ["olma", "daftar", "tuya"]

chosen_word = random.choice(word_list)
taxmin = input("Bir harf taxmin qiling: ").lower()
# lower() funksiyasi yordamida foydalanuvchi kiritgan ma'lumotni 
# bir xil ko'rinishga keltirib olamiz
for harf in chosen_word:
  if harf == taxmin:
    print("True")
  else:
    print("False")
