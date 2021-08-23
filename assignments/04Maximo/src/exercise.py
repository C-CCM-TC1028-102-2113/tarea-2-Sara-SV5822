def main():
    # Escribe el código adecuado para completar el programa
    num1 = int(input("Ingresa el primer número: "))
    num2 = int(input("Ingresa el segundo número: "))
    num3 = int(input("Ingresa el tercer número: "))

    max=0

    if num1>num2:
        max=num1

    elif num1<num2:
        max=num2
    pass

    if max>num3:
        max=max
    elif max<num3:
        max=num3
    pass

    print(max)

if __name__ == '__main__':
    main()
