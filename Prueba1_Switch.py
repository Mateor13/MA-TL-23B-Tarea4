#Mateo Aldair Torres Lara
#Entrada de Datos del cliente
print("****************Bienvenido a Carbonero****************")
nombre = input("Ingrese su nombre: ")
cedula = int(input("Ingrese su numero de cedula: "))
correo = input("Ingrese su correo electronico: ")
# Asignamos el precio y el tipo de hamburguesa
print("Tipos de hamburguesas que servimos:""\n""a) Sencilla: $1.5""\n""b) Doble: $2.5""\n""c) Triple: $3.25")
tipoHamb = input("Ingrese la vocal con el tipo de hamburguesa que desea adquirir: ")
match tipoHamb:
    case "a":
        precio = 1.5
        tipo = "sencilla(s)"
    case "b":
        precio = 2.5
        tipo = "doble(s)"
    case "c":
        precio = 3.25
        tipo = "triple(s)"
    case default:
        print("El tipo de hamburguesa ingresado es inválido.")
        exit()
# Validamos la cantidad de hamburguesas
print()
numHamb = int(input("Cuántas hamburguesas desea: "))
if numHamb <= 0:
    print("El número de hamburguesas ingresado es inválido.")
    exit()
else:
    # Imprimimos la cantidad de hamburguesas ordenadas
    print ("Se ordenarón", numHamb, "hamburguesas", tipo, ".")
    print()
# Calculamos el precio total
precioTotal = numHamb * precio
print("Métodos de pago por su orden: ""\na) Tarjeta de crédito(con un 5 por ciento de recargo)""\nb) Efectivo(Sin recargos)")
metPago = input("Ingrese la vocal con el método de pago a aplicar: ")
# Validamos el método de pago
# Asignamos el precio final según el método de pago
match metPago:
    case "a":
        precioFinal = precioTotal * 1.05
        print()
        print("Su método de pago es con tarjeta de crédito, por favor cancele con recarga:", round(precioFinal,2), "dolares.")
    case "b":
        precioFinal = precioTotal
        print()
        print("Su pago es en efectivo, por favor cancele sin recarga: ", round(precioFinal,2))
    case default:
        print("No contamos con otro tipo de método de pago")
        exit()
# Imprimimos el agradecimiento y la factura
print()
print("Muchas gracias ",nombre," por su compra, vuelva pronto""\nLa Factura será enviada a su correo: ",correo,".")