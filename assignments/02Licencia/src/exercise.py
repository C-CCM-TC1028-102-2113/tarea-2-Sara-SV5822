def main():
    
    edad = int(input("Ingresa tu edad: "))
    # Escribe el código adecuado para completar el programa
    # Para pedir el dato de la idetificación oficial emplea este mensaje:
    # "¿Tienes identificación oficial? (s/n): "
    if edad>=18:
        iden=str(input('¿Tienes identificación oficial? (s/n): '))
        if  iden=='s':
            print('Trámite de licencia concedido')
        elif iden=='n':
            print('No cumples requisitos')

        else:
            print('Respuesta incorrecta')
    
    elif edad<18:
        print('No cumples requisitos')

    else:
        print('Respuesta incorrecta')



if __name__ == '__main__':
    main()
