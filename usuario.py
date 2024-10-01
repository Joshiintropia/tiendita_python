from config import continuar, lista_productos, limpiar_pantalla

#Create
def agregar_productos():
    print("Agregar producto")
    producto = input("Agregar el nombre del producto: ")
    precio = input("Agrega el precio del producto: ")
    if not precio.isdigit():
        print("El precio solo pueden ser números enteros")
        agregar_productos()

    inventario = input("Agregar el inventario del producto: ")
    if not inventario.isdigit():
        print("El inventario solo pueden ser números enteros")
        agregar_productos()

    id = len(lista_productos) + 1

    if(producto != None and int(precio) > 0 and int(inventario) > 0):
        lista_productos.append({"id": id, "nombre_producto": producto, "precio": precio, "inventario": inventario})
    else:
        print("""
            ====================================================================
            Faltan datos, no podemos agregar el producto, intenta de nuevo...
            =====================================================================
            """)

        agregar_productos()


#Read
def listar_productos():
    print("{:<5} {:<15} {:<10} {:<10}".format("ID", "PRODUCTO", "PRECIO", "INVENTARIO"))
    for producto in lista_productos:
        if producto["inventario"] == 0:
            continue
        id, nombre_producto, precio, inventario, *otros = producto.values()
        print("{:<5} {:<15} {:<10} {:<10}".format(id, nombre_producto, precio, inventario))


#Update
def actualizar_producto():
    if(lista_productos == []):
        print("""
            ==================================
            No existen Productos para eliminar
            ==================================
            """)
    elif lista_productos != []:
        listar_productos()
        id = input("Ingresa el id del producto a actualizar: ")
        if id.isdigit():
            id = int(id) - 1
            actualizar_valor = input("Elije la opción a actualizar (Nombre | Precio | Cantidad): ").lower()
            if (id >= 0 and id <= len(lista_productos)):
                match actualizar_valor:
                    case "nombre":
                        nombre_actualizado = input("Ingresa el nombre del producto: ")
                        # print(lista_productos[id])
                        dicc = lista_productos[id]
                        dicc["nombre_producto"] = nombre_actualizado
                        print("""
                            ==============================
                            Producto actualizado con exito
                            ==============================
                            """)
                    case "precio":
                        precio_actualizado = int(input("Ingresa el precio del producto: "))
                        # print(lista_productos[id])
                        dicc = lista_productos[id]
                        dicc["precio"] = precio_actualizado
                        print("""
                            ==============================
                            Producto actualizado con exito
                            ==============================
                            """)
                    case "cantidad":
                        inventario_actualizado = int(input("Ingresa el inventario del producto: "))
                        # print(lista_productos[id])
                        dicc = lista_productos[id]
                        dicc["inventario"] = inventario_actualizado
                        print("""
                            ==============================
                            Producto actualizado con exito
                            ==============================
                            """)
                    case _:
                        print("""
                            ====================
                            ||  Opción incorrecta! ||
                            ====================
                            """)
            else:
                print("""
                    =========================
                    El id ingresado no existe
                    =========================
                    """)
                limpiar_pantalla()
                actualizar_producto()
        else:
            print("""
                =========================
                ||  Opción incorrecta! ||
                =========================
                """)
    else:
        print("El id no existe en la lista")


#Delet
def eliminar_producto():
    if(lista_productos == []):
        print("""
            ==================================
            No existen Productos para eliminar
            ==================================
            """)
    elif lista_productos != []:
        listar_productos()
        id = int(input("Ingresa el id del producto a eliminar: "))
        id -= 1
        print("El id es: ", id)
        if (id >= 0 and id <= len(lista_productos)):
        #     lista_productos.pop(id)
            print("Producto eliminado con exito!")
        else:
            print("""
                =========================
                El id ingresado no existe
                =========================
                """)
            limpiar_pantalla()
            eliminar_producto()
    else:
        print("El id no existe en la lista")


def usuario():
    _ = 0
    while _ != 5:
        limpiar_pantalla()
        print("""
            =====================================
            Elije la opción que quieras realizar
            1) Listar los productos
            2) Agregar un producto
            3) Eliminar un producto
            4) Actualizar producto
            5) Salir
            =====================================
            """)
        _ = input()
        if _.isdigit():
            _ = int(_)
            match _:
                case 1:
                    limpiar_pantalla()
                    listar_productos()
                    continuar()
                case 2:
                    limpiar_pantalla()
                    agregar_productos()
                    # v = input("Presiona cualquier tecla para continuar: ")
                case 3:
                    limpiar_pantalla()
                    eliminar_producto()
                    continuar()
                case 4:
                    limpiar_pantalla()
                    actualizar_producto()
                    continuar()
                case 5:
                    limpiar_pantalla()
                    break
