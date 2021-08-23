def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))

    num1=0
    num2=0
    num3=0

    if x>=y and x>=z:
        num1=x

        if y>=z:
            num2=y
            num3=z
        elif z>=y:
            num2=z
            num3=y
        pass

    elif y>=x and y>=z:
        num1=y

        if x>=z:
            num2=x
            num3=z

        elif z>=x:
            num2=z
            num3=x
        pass

    elif z>=x and z>=y:
        num1=z
        if y>=x:
            num2=y
            num3=x
        elif x>=y:
            num2=x
            num3=y
        pass

    pass

    print(num3)
    print(num2)
    print(num1)
    
    


if __name__ == '__main__':
    main()
