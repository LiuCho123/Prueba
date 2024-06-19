pedidos = []

def registroPedido(pedidos):
    
    nombre = input("Ingrese su nombre y apellido: ")
    direccion = input("Ingrese su dirección: ")
    sector = input("Ingrese su sector: ")
    while True:

        print("PAQUETES: ")
        print("----------------------------")
        print("1. Pequeño")
        print("2. Mediano")
        print("3. Grande")
        print("4. Finalizar")
        print("----------------------------")

        menuPaquete = int(input("Escoja el tamaño del paquete y su cantidad: "))

        contPequeño = 0
        contMediano = 0
        contGrande = 0

        if menuPaquete == 1:
            contPequeño = contPequeño + 1

        if menuPaquete == 2:
            contMediano = contMediano + 1

        if menuPaquete == 3:
            contGrande = + contGrande + 1

        if menuPaquete == 4:
            pedido = {"Nombre y apellido": nombre,
                "Dirección": direccion,
                "Sector": sector,
                "Caja Pequeña": contPequeño, "Caja Mediana": contMediano, "Caja Grande": contGrande}
            print("Pedido realizado con éxito: \n", pedido)
            break

    pedidos.append(pedido)
    
def listarPedido(pedidos):
    for pedido in pedidos:
        print(pedido)

def hojaDeRuta(pedidos):
    with open("pedidos.txt", "w") as archivo:
        for pedido in pedidos:
            archivo.writelines("Nombre y apellido")
            archivo.writelines("Dirección")
            archivo.writelines("Sector")
            archivo.writelines("Caja Pequeña")
            archivo.writelines("Caja Mediana")
            archivo.writelines("Caja Grande")

while True:
    print("Bienvenido a PaquExpress")
    print("----------------------------")
    print("¿Que desea hacer?")
    print("1. Registrar pedido")
    print("2. Listar todos los pedidos")
    print("3. Imprimir hoja de ruta")
    print("4. Salir del programa")
    print("----------------------------")

    menu = int(input("Seleccione una opción: "))

    if menu == 1:
        registroPedido(pedidos)

    if menu == 2:
        listarPedido(pedidos)

    if menu == 3:
        hojaDeRuta(pedidos)
        
    if menu == 4:
        print("                 Saliendo del programa...")
        break
