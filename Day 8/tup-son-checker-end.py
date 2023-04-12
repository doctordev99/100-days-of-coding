#Yechim

def tub_checker(raqam):
    for num in range(2, raqam):
        tub_sonmi = True 
        if raqam % num == 0:
            tub_sonmi = False
    if tub_sonmi:
        print("Bu tub son")
    else:
        print("Bu tub son emas")

n = int(input("Bu raqamni tekshir: "))
tub_checker(raqam=n)
