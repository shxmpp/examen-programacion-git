import modulo as me
import os

# Codigo general


def main():
    productos = {
        "P101": ["Cuaernos", "Papeleria", 2490, True],
        "P102": ["Lapiz", "Papeleria", 590, True],
        "P103": ["Botella", "Accesorios", 6990, True],
        "P104": ["Mochila", "Accesorios", 24990, True],
    }
    inventrio = {
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
            ===================================
            \n Elija opcion: """)
