palabra = input("Introduce una palabra: ")

palabra = list(palabra)
print(palabra)
cont_a=int()
cont_e=int()
cont_i=int()
cont_o=int()
cont_u=int()
for i in palabra:
    if i == "a":
        cont_a += 1
    if i == "e":
        cont_e += 1
    if i == "i":
        cont_i += 1
    if i == "o":
        cont_o += 1
    if i == "u":
        cont_u += 1

print(f"A aparece {cont_a} veces")
print(f"E aparece {cont_e} veces")
print(f"I aparece {cont_i} veces")
print(f"O aparece {cont_o} veces")
print(f"U aparece {cont_u} veces")

        
