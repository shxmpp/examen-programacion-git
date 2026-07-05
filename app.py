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
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
        elif opcion == 7:
            print("Programa terminado")
            break
