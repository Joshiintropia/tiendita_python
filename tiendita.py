from autentificacion import crear_usuario, login
from config import limpiar_pantalla, lista_usuarios, continuar
from usuario import usuario
from cliente import cliente

def saludar():
    print("""
    ====================================
    BIENVENIDOS A LA TIENDITA DEL JOCHUA
    ====================================
    """)

def menu():
    user = input("""
        Selecciona como deseas ingresar:
            1) Usuario
            2) Cliente
            3) Crear usuario
            4) Salir
        """)
    return user

def main():

    while True:
        limpiar_pantalla()
        saludar()
        user = int(menu())
        match user:
            case 1:
                limpiar_pantalla()
                if login():
                    usuario()
            case 2:
                cliente()
            case 3:
                limpiar_pantalla()
                crear_usuario()
                continuar()
            case 4:
                limpiar_pantalla()
                break
            case _:
                print("Opción invalida")
                continuar()

if __name__=='__main__':
    main()
