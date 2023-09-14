fecha = input("Introduce fecha en formato dd/mm/aaaa: ")

a = fecha.split('/')
print(a)
b = {'01':'Enero', '02':'Febrero','03':'Marzo'}
print(f"{a[0]} de {b[a[1]]} de {a[2]}")
