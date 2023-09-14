d = {'Plátano':1.35, 'Manzana':0.8,'Pera':0.85,'Naranja':0.7}
a = input("Dime una fruta y su peso en kg separado por un _: ")
f = a.split('_')
f2 = float(f[1])

if d[f[0]] in d:
    print('Está fruta no existe')
else:
    precio = (d[f[0]])*f2
    print(precio)
