from config import continuar, limpiar_pantalla, lista_compras, lista_productos
from usuario import agregar_productos, listar_productos

#Create
def agregar_productos_carrito():
    listar_productos()

    id = input("Selecciona el id del producto que quieres agregar al carrito: ")
    if id.isdigit() and int(id) > 0 and int(id) <= len(lista_productos):

        id = int(id) - 1
        producto = lista_productos[id]

        if producto["inventario"] > 0:

            if producto in lista_compras:
                producto["cantidad"] += 1
                print("""
                    =======================
                    || PRODUCTO AGREGADO ||
                    =======================
                    """)
            else:
                producto["cantidad"] = 1
                lista_compras.append(producto)
                print("""
                    =================================
                    || PRODUCTO AGREGADO AL CARRITO ||
                    =================================
                    """)

            producto["inventario"] -= 1

        else:
            print("""
                ===========================
                ||PRODUCTO SIN EXISTENCIAS||
                ===========================
                """)

    else:
        print("""
        =====================================
        ||El ID que ingresaste no es valido||
        =====================================
                """)


#Read
def listar_carrito():

    if lista_compras == []:
        print("""
            ==================================
            No existen Productos en el carrito
            ==================================
            """)
    else:
        #IMPRIMIR PANTALLA EN COLUMNAS
        print("{:<5} {:<30} {:<10} {:<10}".format("Id", "Producto", "Precio", "Cantidad"))
        for producto in lista_compras:
            id, nombre, precio, inventario, cantidad, pagar = producto.values()
            # print(f" {id}   | {nombre}    | {precio}   | {cantidad}")
            print("{:<5} {:<30} {:<10} {:<10}".format(id, nombre, precio, cantidad))


#Update
def comprar_carrito():
    print("{:<15} {:<10} {:<10}".format("Producto", "Precio", "Cantidad"))

    total_pagar = 0
    for producto in lista_compras:
        id, prod, prec, inv, cant, pagar = producto.values()
        pagar = prec*cant
        print("{:<15} {:<10} {:<10}".format(prod, cant, pagar))
        producto["pagar"] = pagar
        total_pagar += pagar

    print(f"""
        ========================
        || TOTAL A PAGAR: ${total_pagar} ||
        ========================
        """)

    lista_compras.clear()


#Delet
def eliminar_producto_carrito():
    if(lista_compras == []):
        print("""
            ==================================
            No existen Productos para eliminar
            ==================================
            """)
    elif lista_compras != []:
        listar_carrito()
        id = input("Ingresa el id del producto a eliminar: ")
        if id.isdigit() and int(id) >= 0 and int(id) <= len(lista_compras):
            id = int(id) - 1
            lista_productos.pop(id)
            print("Producto eliminado con exito!")
            producto = lista_productos[id]
            producto["inventario"] += 1
            producto["cantidad"] -= 1
        else:
            print("""
                =========================
                El id ingresado no existe
                =========================
                """)
            limpiar_pantalla()
            eliminar_producto_carrito()
    else:
        pass


def cliente():
    _ = None
    while _ != 6:
        limpiar_pantalla()
        print("""
            =====================================
            ------------BIENVENIDO-------------
            Elije la opción que quieras realizar
            1) Listar los productos
            2) Agregar producto al carrito
            3) Eliminar un producto del carrito
            4) Ir al carrito
            5) Pagar carrito
            6) Salir
            =====================================
            """)
        _ = input()
        if _.isdigit():
            _ = int(_)
            match _:
                case 1:#Listar productos
                    limpiar_pantalla()
                    listar_productos()
                    continuar()
                case 2:#Agregar producto
                    limpiar_pantalla()
                    agregar_productos_carrito()
                    continuar()
                case 3:#Eliminar producto
                    limpiar_pantalla()
                    eliminar_producto_carrito()
                    continuar()
                case 4:#Listar carrito
                    limpiar_pantalla()
                    listar_carrito()
                    continuar()
                case 5:#Pagar carrito
                    limpiar_pantalla()
                    comprar_carrito()
                    continuar()
                case 6:#Salir
                    limpiar_pantalla()
                    break
                case _:
                    continue
