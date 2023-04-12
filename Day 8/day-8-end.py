# Takrorlash:
# salomlash() nomli funksiya yarating.
# Funktsiya ichida 3 ta chop etish operatorini yozing.
# greet() funksiyasiga chaqiring va kodingizni ishga tushiring.

def salomlash():
  print("Salom")
  print("Salom, hayirli kun")
  print("Salom, hayirli tong")

salomlash()

# Lekin biz doim funksiyadan bir xil ma'lumot olmaymiz
# Funksiyaga input kiritish orqali buni amalga oshiramiz

def salomlash(ism):
  print(f"Salom, {ism}")
  print(f"Salom, hayirli kun {ism}")
  print(f"Salom, hayirli tong {ism}")

salomlash("Umid")

# Keling endi funksiyaga bir nechda input kirgizib ko'ramiz

def salomlash(ism, manzil):
  print(f"Salom, {ism}")
  print(f"{manzil}da ob-havo qanday")

salomlash("Umid", "Namangan")

def salomlash(ism, manzil):
  print(f"Salom, {ism}")
  print(f"{manzil}da ob-havo qanday")

# Agar biz argumentlarni kirgizishda ularni o'rnini almashtirsakchi

salomlash("Namangan", "Umid")

# Bunday holatlarni oldini olishda keywordlardan foydalanamiz

salomlash(manzil="Namangan", ism="Umid")
