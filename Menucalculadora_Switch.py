# Mateo Aldair Torres Lara
# Entrada de Datos
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
# Menú de opciones
print ("Menú de opciones""\n""a) Suma""\n""b) Resta""\n""c) Multiplicación""\n""d) División""\n""e) Potencia""\n""f) Modulo""\n""g) Salir")
opcion = input("Ingrese la letra de la opción que desea realizar: ")
# Validamos la opción ingresada
# Realizamos la operación según la opción ingresada
match opcion:
    case "a":
        suma = num1 + num2
        print("El resultado de la suma es: ", suma)
    case "b":
        resta = num1 - num2
        print("El resultado de la resta es: ", resta)	
    case "c":
        multiplicacion = num1 * num2
        print("El resultado de la multiplicación es: ", multiplicacion)
    case "d":
        if num2 != 0:
            division = num1 / num2
            print("El resultado de la división es: ", division)
        else:
            print("No se puede dividir entre cero.")
    case "e":
        potencia = num1 ** num2
        print("El resultado de la potencia es: ", potencia)
    case "f":
        if num2 != 0:
            modulo = num1 % num2
            print("El residuo de la división es: ", modulo)
        else:
            print("No se puede dividir entre cero.")
    case "g":
        print("Saliendo del menú de la calculadora.")
    case default:
        print("La opción ingresada es inválida.")
        exit()