#Yechim 
import math 
def paint_calc(height, width, cover):
  yuza = height * width
  cans = math.ceil(yuza / cover)
  print(f"Siz {cans} ta konserva bankasida rang kerak bo'ladi")
# Bu yerda biz round funksiyasini ishlatmadin, sabab round 5,4 ni 5 qilib yaxsltlashid, ceil() metodida bu 6 bo'ladi

test_h = int(input("Devorning balandligi: "))
test_w = int(input("Devorning eni: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
