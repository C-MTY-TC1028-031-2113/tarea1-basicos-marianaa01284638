def main():
    #escribe tu código abajo de esta línea
    saldoanterior = float(input("dame el saldo del mes anterior: "))
    ingresos = float(input("dame los ingresos: "))
    egresos = float(input("dame los egresos: "))
    cheques = float(input("dame el numero de cheques: "))
    saldofinal = (saldoanterior + ingresos - egresos - (13 * cheques))
    final = (saldofinal - (saldofinal * 0.075))
    print('el saldo final de la cuenta es: ' + str(final))
    
main()
