edad = 18
novia = False

if edad >= 19:
    if novia == True:
        print("Puedes pasar")
    
elif edad < 19 & novia:
    print("muy menor")
    
else:
    print("No puedes")
    
cadena1 = "Hola"
cadena2 = "as123"

mayusc = cadena1.upper()
print(mayusc)

find = cadena1.find("O")
print(find)

fuck = cadena1.index("o")
print(fuck)

nume = cadena2.isnumeric()
print(nume)

coincide =cadena1.count("7")
print(coincide)