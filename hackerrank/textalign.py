# rjust, ljust,center , LOGO

thick=5
c= 'H'

for i in range(thick):
    print((c*i).rjust(thick-1)+c+(c*i).ljust(thick-1))

for i in range(thick+1):
    print((c*thick).center(thick*2)+(c*thick).center(thick*6))
    
for i in range(thick):
    print((c*thick*5).center(thick*6))

for i in range(thick+1):
    print((c*thick).center(thick*2)+(c*thick).center(thick*6))

for i in range(thick):
    print(((c*(thick-i-1)).rjust(thick)+c+(c*(thick-i-1)).ljust(thick)).rjust(thick*6))