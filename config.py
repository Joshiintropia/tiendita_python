import os

lista_productos = [{"id": 1, "nombre_producto": "tamal verde", "precio": 15, "inventario": 3, "cantidad": 0, "pagar": 0},
                    {"id": 2, "nombre_producto": "tamal dulce", "precio": 15, "inventario": 3, "cantidad": 0, "pagar": 0},
                    {"id": 3, "nombre_producto": "tamal rajas", "precio": 15, "inventario": 3, "cantidad": 0, "pagar": 0}]

lista_compras = []

lista_usuarios = []

def limpiar_pantalla():
    os.system("clear")


def continuar():
    _ = input("Presiona cualquier tecla para continuar...")
