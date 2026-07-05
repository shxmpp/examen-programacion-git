def leer_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))

            if 1 <= opcion <= 7:
                return opcion

            print("Debe seleccionar una opcionvalida")

        except:
            print("Debe ingresr un numero.")


def stock_categoria(categoria, productos, inventario):
    total = 0

    for codigo in productos:

        if productos[codigo][1].lower() == categoria.lower():

            total += inventario[codigo][0]

    print("Stock total", total)


def buscar_precio(precio_min, precio_max, productos, inventario):

    lista = []

    for codigo in productos:
        precio = productos[codigo][2]
        stock = inventario[codigo][0]

        if precio_min <= precio <= precio_max and stock > 0:
            lista.append((productos[codigo][0], codigo))
    lista.sort()

    for nombre, codigo in lista:

        print(nombre, "--", codigo)
