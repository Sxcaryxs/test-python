hor = 0
min = 0 
seg = 0

while hor < 24:
    while min < 60:
        while seg < 60:

            print(f"reloj {hor:02d}:{min:02d}:{seg:02d}")
            seg += 1

        min += 1  
        seg = 0           

    hor += 1
    min = 0