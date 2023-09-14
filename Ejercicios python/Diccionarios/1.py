d = {"Euro": '€', "Dollar": "$", "Yen":"Y"}
c = input("Dime la divisa")

if c in d:
    print("esta en el diccionario")
    print(d[c])
else:
    print("No está en el diccionario")
