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


def actualizar_precio(codigo, nuevo_precio, productos):

    if codigo in productos:

        productos[codigo.upper()][2] = nuevo_precio

        return True

    return False


def agregar_producto(
    codigo,
    nombre,
    categoria,
    precio,
    disponible,
    stock,
    vendidos,
    productos,
    inventario,
):
    if codigo in productos:
        return False

    productos[codigo] = [nombre, categoria, precio, disponible]
    inventario[codigo] = [stock, vendidos]
    return True


def eliminar_producto(codigo, producto, inventario):

    if codigo in producto:
        del producto[codigo]
        del inventario[codigo]

        return True

    return False


# Definimos las funciones de validaciones


def validar_nombre(nombre):
    return nombre.strip() != " "


def validar_categoria(categoria):
    return categoria.strip() != " "


def validar_precio(precio):
    return precio > 0


def validar_stock(stock):
    return stock > 0


def validar_vendidos(vendidos):
    return vendidos > 0


def validar_disponibles(opcion):
    return opcion.lower() in ["S", "N"]
