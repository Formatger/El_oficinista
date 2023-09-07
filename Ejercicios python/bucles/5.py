inversion = float(input("Cantidad a invertir en €: "))
interes = float(input("Interes anual en %: "))
duracion = int(input("Cuantos años dura la inversión?: "))

for i in range(duracion):
    beneficio = (inversion * interes)/100
    print(f"En el año {i+1} el beneficio es de {beneficio} euros")
    inversion = inversion + beneficio