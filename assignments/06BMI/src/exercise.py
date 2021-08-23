def main():
    # Escribe el código adecuado para completar el programa
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))

    if peso>0 and altura>0:

        indi= peso/(altura**2)

        if indi<20:
            print('PESO BAJO')
        elif 20<=indi<25:
            print('NORMAL')
        elif 25<=indi<30:
            print('SOBREPESO')
        elif 30<=indi<40:
            print('OBESIDAD')
        elif indi>=40:
            print('OBESIDAD MORBIDA')

    
    else:
        print('Revisa tus datos, alguno de ellos es erróneo.')

    pass

if __name__ == '__main__':
    main()
