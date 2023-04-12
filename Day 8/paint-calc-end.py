#Yechim 

def paint_calc(height, width, cover):
  cans = round(height * width / cover)
  print(f"Siz {cans} ta konserva bankasida rang kerak bo'ladi")

test_h = int(input("Devorning balandligi: "))
test_w = int(input("Devorning eni: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
