asi = {'Mates':6,'Física':4,'Química':5}
total = 0
for credito in asi:
    print(f"{credito} tiene {asi[credito]} créditos")
    total += asi[credito]

print(f"El total de créditos es: {total}")