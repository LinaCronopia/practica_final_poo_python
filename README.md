# Patas Felices — sistema de gestión

Proyecto final grupal desarrollado durante una formación inicial en programación con Python. El objetivo fue aplicar conceptos de programación orientada a objetos mediante una aplicación de consola para gestionar mascotas, clientes, productos, ventas e inventario.

## Funcionalidades

- Registrar perros y gatos.
- Registrar clientes.
- Registrar productos.
- Registrar ventas de uno o más productos.
- Consultar la información cargada.
- Generar alertas para productos con existencias por debajo de un umbral.

## Conceptos aplicados

- Clases y objetos.
- Herencia.
- Encapsulamiento de datos y comportamientos.
- Composición entre objetos.
- Listas y estructuras de control.
- Interfaz interactiva mediante consola.

## Estructura

```text
practica_final_poo_python/
├── clases/
│   ├── __init__.py
│   ├── cliente.py
│   ├── inventario.py
│   ├── mascota.py
│   ├── producto.py
│   └── venta.py
├── .gitignore
├── README.md
└── main.py
```

## Ejecución

Se requiere Python 3 y no es necesario instalar dependencias externas.

```bash
python main.py
```

El programa presenta un menú para cargar y consultar la información durante la ejecución.

## Alcance

Este repositorio conserva un proyecto correspondiente a una etapa inicial de aprendizaje. Los datos se almacenan temporalmente en memoria y se pierden al cerrar el programa. La versión actual no descuenta automáticamente las existencias al registrar una venta.
