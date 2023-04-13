programming_dictionary = {
  "Bug": "Dasturning kutilganidek ishlashiga to'sqinlik qiladigan dasturdagi xato.", 
  "Function": "Siz osongina qayta-qayta murojaat qilishingiz mumkin bo'lgan kod qismi."
}

# Lug'atdagi biror qiymatni ko'rish:
print(programming_dictionary["Bug"])

# Lug'aga yangi kalit so'z va qiymatlar qo'shish:
programming_dictionary["Loop"] = "Loop ma'lum bir shart qondirilgunga qadar biror narsani qayta-qayta takrorlashni anglatadi"
print(programming_dictionary)

# Bo'sh lug'at yaratish
emty_dictionary = {}

# Lug'atdagi ma'lumotlarni o'chirish
programming_dictionary = {}
print(programming_dictionary)

# Qiymatni o'zgartirish
programming_dictionary["Bug"] = "Ma'lum bir hasharot turi."
print(programming_dictionary)

# For loop bilan ishlash
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
  
