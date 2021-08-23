def main():
    #escribe tu código abajo de esta línea
    pesoinicial = float(input("dame el peso inicial: "))
    pesofinal = float(input("dame el peso final: "))
    meses = float(input("dame la cantidad de meses: "))
    bajar = (pesoinicial - pesofinal) / meses
    print('lo que debes bajar por mes es: ' + str(bajar))

main()