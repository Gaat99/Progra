
print("Transformacion de Unidades....")
print("Ingrese el valor a transformar:")
num= int(input())
print("Ha ingresado el ", num)

print("Escoja en que unidades esta el numero:")
print("1. mm")
print("2. cm")
print("3. m")
print("4. hm")
print("5. km")
opcionMenu=int(input())

if (opcionMenu == 1):
    print("Valor ingresado es",num, "mm")
    print("Valor transformado en... ")
    print("Centimetros: ", num/10, "cm")
    print("Metros: ", num/100, "m")
    print("Hectometros: ", num/100000, "hm")
    print("Kilometross: ", num/1000000, "km")
    
if (opcionMenu == 2):
    print("Valor ingresado es",num, "cm")
    print("Valor transformado en... ")
    print("Milimetros: ", num*10, "cm")
    print("Metros: ", num/100, "m")
    print("Hectometros: ", num/10000, "hm")
    print("Kilometross: ", num/100000, "km")

if (opcionMenu == 3):
    print("Valor ingresado es",num, "m")
    print("Valor transformado en... ")
    print("Milimetros: ", num/1000, "cm")
    print("Centimetros: ", num*100, "m")
    print("Hectometros: ", num/100, "hm")
    print("Kilometross: ", num/1000, "km")

if (opcionMenu == 4):
    print("Valor ingresado es",num, "hm")
    print("Valor transformado en... ")
    print("Centimetros: ", num*10000, "cm")
    print("Milimetros: ", num*100000, "mm")
    print("Metros: ", num*100, "m")
    print("Kilometross: ", num/10, "km")
    
if (opcionMenu == 5):
    print("Valor ingresado es",num, "km")
    print("Valor transformado en... ")
    print("Centimetros: ", num*100000, "cm")
    print("Milimetros: ", num*100000, "mm")
    print("Metros: ", num*100, "m")
    print("Kilometross: ", num/10, "km")
    
else:
    ("Ingrese un valor correcto")
    
