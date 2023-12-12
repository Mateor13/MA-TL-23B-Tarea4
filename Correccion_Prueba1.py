# Mateo Aldair Torres Lara
# Entrada de Datos del cliente
print("*********BIENVENIDOS A CARBONERO*********")
nombre = input("Ingrese su nombre: ")
cedula = input("Ingrese su número de cédula: ")
correo = input ("Ingrese su correo electrónico: ")
# Asignamos el precio y el tipo de hamburguesa
print("Tipos de hamburguesas que servimos:""\n""a) Sencilla: $1.5""\n""b) Doble: $2.5""\n""c) triple: $3.25")
tipoHamb = input("Ingrese la vocal con el tipo de hamburguesa que desea adquirir: ")
if tipoHamb == "a":
    precio = 1.5
    tipo = "sencilla(s)"
elif tipoHamb == "b":
    precio = 2.5
    tipo = "doble(s)"
elif tipoHamb == "c":
    precio = 3.25
    tipo = "triple(s)"
else:
    print("El tipo de hamburguesa ingresado es inválido.")
    exit()
# Validamos la cantidad de hamburguesas
numHamb = int(input("Cuántas hamburguesas desea: "))
if numHamb <= 0:
    print("El número de hamburguesas ingresado es inválido.")
    exit()
else:
    # Imprimimos la cantidad de hamburguesas ordenadas
    print()
    print ("Se ordenarón", numHamb, "hamburguesas", tipo, ".")
# Calculamos el precio total
precioTotal = numHamb * precio
# Validamos el método de pago
print("Métodos de pago por su orden: ""\na) Tarjeta de crédito(con un 5 por ciento de recargo)""\nb) Efectivo(Sin recargos)")
metPago = input("Ingrese la vocal con el método de pago a aplicar: ")
# Asignamos el precio final según el método de pago
if metPago == "a":
    precioFinal = precioTotal * 1.05
    print()
    print("Su método de pago es con tarjeta de crédito, por favor cancele con recarga:", round(precioFinal,2), "dolares.")
elif metPago == "b":
    precioFinal = precioTotal
    print()
    print("Su pago es en efectivo, por favor cancele sin recarga: ", round(precioFinal,2))
else:
    print("No contamos con otro tipo de método de pago")
    exit()
# Imprimimos el agradecimiento y la factura
print( nombre, "muchas gracias por su compra, vuelva pronto""\nLa Factura será enviada a su correo.")