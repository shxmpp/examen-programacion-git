import modulo
import os

# Codigo general


def main():
    productos = {
        "P101": ["Cuaernos", "Papeleria", 2490, True],
        "P102": ["Lapiz", "Papeleria", 590, True],
        "P103": ["Botella", "Accesorios", 6990, True],
        "P104": ["Mochila", "Accesorios", 24990, True],
    }
    inventario = {
        "P101": [30, 15],
        "P102": [120, 50],
        "P103": [0, 10],
        "P104": [8, 25],
    }
    while True:
        os.system("cls")
        print(f"""
            ========== MENÚ PRINCIPAL ==========
            1. Stock por categoría
            2. Buscar productos por rango de precio
            3. Actualizar precio
            4. Agregar producto
            5. Eliminar producto
            6. Mostrar productos
            7. Salir
            ===================================""")

        opcion = modulo.leer_opcion()
        if opcion == 1:
            categoria = input("Ingrese una categoria: ")
            modulo.stock_categoria(categoria, productos, inventario)
        elif opcion == 2:
            try:
                minimo = int(input("Precio minimo: "))
                maximo = int(input("precio maximo: "))

                modulo.buscar_precio(minimo, maximo, productos, inventario)

            except:
                print("Debe ingresar numeros")
        elif opcion == 3:
            try:
                codigo = input("codigio: ")

                precio = int(input("Nuevo precio: "))

                if modulo.actualizar_precio(codigo, precio, productos):

                    print("Precio Actualizado")
                else:
                    print("Codigo inexistente")
            except:
                print("Debe ingresar un numero")
        elif opcion == 4:
            while True:
                codigo = input("Codigo: ").upper()

                if modulo.validar_codigo(codigo, productos):
                    break
                print("Codigo invalido.")

            while True:
                nombre = input("nombre: ")

                if modulo.validar_nombre(nombre):
                    break
                print("Nombre Invalido")

            while True:
                categoria = input("Categoria: ")

                if modulo.validar_categoria(categoria):
                    break
                print("Categoria invalida")

            while True:
                try:
                    precio = int(input("Precio: "))

                    if modulo.validar_precio(precio):
                        break
                    print("Precio invalido")
                except:
                    print("Debe ingresar un numero")

            while True:
                disponble = input("Disponible (S/N): ").lower()

                if modulo.validar_disponibles(disponble):
                    disponble = disponble == "S"
                    break

                print("Debe ingresar S o N.")

            while True:
                try:
                    stock = int(input("Stock: "))

                    if modulo.validar_stock(stock):
                        break
                    print("Stock invalido")
                except ValueError:
                    print("Debe ingresar un numero")

            while True:
                try:
                    vendidos = int(input("Vendidos: "))

                    if modulo.validar_vendidos(vendidos):
                        break
                    print("Cantidad invalida")
                except ValueError:
                    print("Debe ingresar un numeo")

            if modulo.agregar_producto(
                codigo,
                nombre,
                categoria,
                precio,
                disponble,
                stock,
                vendidos,
                productos,
                inventario,
            ):
                print("Producto agregado correctamente.")
            else:
                print("El codigo ya existe")

        elif opcion == 5:
            codigo = input("Ingrese el codigo del producto a eliminar: ").upper()

            if modulo.eliminar_producto(codigo, productos, inventario):
                print("Producto eliminado correcataente")
            else:
                print("Codigo inexistente")
        elif opcion == 6:
            modulo.mostrar_productos(productos, inventario)
        elif opcion == 7:
            print("Programa terminado")
            break


if __name__ == "__main__":
    main()
