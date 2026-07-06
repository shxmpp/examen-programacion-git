# 🛒 Sistema de Gestión de Productos en Python

# 📖 Descripción

Este proyecto corresponde al desarrollo de un **Sistema de Gestión de Productos** realizado en **Python**, utilizando programación modular.

El sistema permite administrar la información de productos e inventario mediante el uso de:

✅ Diccionarios

✅ Funciones

✅ Validaciones

✅ Menú interactivo

✅ Manejo de excepciones

Todo el proyecto fue desarrollado siguiendo las buenas prácticas de programación, evitando el uso de variables globales y separando la lógica del programa en módulos independientes.

---

# 📂 Estructura del Proyecto

```
📁 Proyecto
│
├── 📄 app.py
└── 📄 modulo.py
```

---

# ⚙️ Tecnologías Utilizadas

| Tecnología | Descripción |
|------------|-------------|
| 🐍 Python | Lenguaje principal |
| 💻 Visual Studio Code | Entorno de desarrollo |
| 📚 Programación Modular | Separación de funciones |
| 📂 Diccionarios | Almacenamiento de datos |
| ⚠️ Try-Except | Manejo de errores |

---

# 📌 Funcionamiento General

El sistema inicia mostrando un menú interactivo.

```
=============================
      MENÚ PRINCIPAL
=============================

1️⃣ Stock por categoría

2️⃣ Buscar productos por precio

3️⃣ Actualizar precio

4️⃣ Agregar producto

5️⃣ Eliminar producto

6️⃣ Mostrar productos

7️⃣ Salir
```

Cada opción ejecuta una función ubicada en **modulo.py**.

---

# 🗂️ Organización del Código

## 📄 app.py

Es el archivo principal del proyecto.

Se encarga de:

- ✅ Crear los diccionarios
- ✅ Mostrar el menú
- ✅ Solicitar datos al usuario
- ✅ Llamar a las funciones
- ✅ Mostrar mensajes en pantalla

---

## 📄 modulo.py

Contiene toda la lógica del programa.

Entre las funciones desarrolladas se encuentran:

```
✔ leer_opcion()

✔ stock_categoria()

✔ buscar_precio()

✔ buscar_codigo()

✔ actualizar_precio()

✔ validar_codigo()

✔ validar_nombre()

✔ validar_categoria()

✔ validar_precio()

✔ validar_disponible()

✔ validar_stock()

✔ validar_vendidos()

✔ agregar_producto()

✔ eliminar_producto()

✔ mostrar_productos()
```

---

# 🗃️ Diccionario Productos

Cada producto almacena cuatro datos.

| Índice | Campo |
|---------|--------|
| 📝 0 | Nombre |
| 📁 1 | Categoría |
| 💲 2 | Precio |
| ✔️ 3 | Disponible |

Ejemplo

```python
productos = {

"P101":["Cuaderno","Papelería",2490,True],

"P102":["Lápiz","Papelería",590,True]

}
```

---

# 📦 Diccionario Inventario

Cada producto posee información relacionada con su inventario.

| Índice | Campo |
|---------|--------|
| 📦 0 | Stock |
| 📈 1 | Vendidos |

Ejemplo

```python
inventario = {

"P101":[30,15],

"P102":[120,50]

}
```

---

# 🚀 Funciones del Sistema

## 1️⃣ Stock por categoría

Calcula el stock total perteneciente a una categoría determinada.

✔ Búsqueda sin distinguir mayúsculas o minúsculas.

---

## 2️⃣ Buscar productos por precio

Permite ingresar un precio mínimo y máximo.

Posteriormente muestra todos los productos que:

- ✔ Están dentro del rango.
- ✔ Poseen stock.
- ✔ Se ordenan alfabéticamente.

---

## 3️⃣ Actualizar precio

Permite modificar el precio de un producto existente.

Si el código no existe, el sistema informa el error.

---

## 4️⃣ Agregar producto

Solicita:

- Código
- Nombre
- Categoría
- Precio
- Disponibilidad
- Stock
- Cantidad vendida

Todos los datos son validados antes de agregarlos.

---

## 5️⃣ Eliminar producto

Elimina el producto de ambos diccionarios.

```
productos

inventario
```

Esto mantiene la integridad de la información.

---

## 6️⃣ Mostrar productos

Recorre ambos diccionarios mostrando:

```
Código

Nombre

Categoría

Precio

Disponible

Stock

Vendidos
```

---

# 🛡️ Validaciones Implementadas

El proyecto incorpora validaciones para:

✅ Código

✅ Nombre

✅ Categoría

✅ Precio

✅ Disponibilidad

✅ Stock

✅ Cantidad vendida

Cada función retorna únicamente **True** o **False**, dejando la interacción con el usuario al archivo principal.

---

# 🧠 Conceptos Aplicados

- 🐍 Python
- 📚 Programación Modular
- 📦 Diccionarios
- 📋 Listas
- 🔁 Ciclos While
- 🔄 Ciclos For
- 🔀 Condicionales
- 📥 Entrada de datos
- 📤 Salida de datos
- ⚠️ Manejo de excepciones
- ✔️ Validación de datos
- 🧩 Funciones
- 📌 Parámetros
- 🔙 Retorno de funciones

---

# 🎯 Objetivos Alcanzados

✔ Aplicación de programación modular.

✔ Organización del código en funciones.

✔ Eliminación del uso de variables globales.

✔ Implementación de estructuras de datos.

✔ Desarrollo de un sistema completo de administración de productos.

✔ Uso de manejo de excepciones para mejorar la robustez del programa.

---

# 📸 Vista General del Proyecto

```
           Usuario
               │
               ▼
         📄 app.py
               │
               ▼
      Solicita información
               │
               ▼
       📄 modulo.py
               │
      ┌────────┴────────┐
      ▼                 ▼
Productos         Inventario
      │                 │
      └────────┬────────┘
               ▼
      Resultado en pantalla
```

---

# 👨‍💻 Autor

**Daniel Miranda**

Proyecto desarrollado para la asignatura **Fundamentos de Programación (FPY1101)** utilizando Python y Visual Studio Code.

⭐ Si este proyecto te resulta útil, no olvides darle una estrella al repositorio.
