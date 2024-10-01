from cliente import limpiar_pantalla
from config import lista_usuarios, continuar
from encriptacion import encriptar, comparar_hashes

def saludo_crear():
    print("""
        **************************
                    HOLA
        Vamos a crearte un usuario
        ***************************
        """)

def saludo_usuario():
    print("""
        *************************
                BIENVENIDO
        INGRESA TUS CREDENCIALES
        *************************
         """)


def crear_usuario():
    saludo_crear()
    nom_usuario = input("Ingresa nombre de usuario: ").lower()

    if nom_usuario != None and len(nom_usuario) > 4:
        pass_usuario = input("Ingresa la contraseña: ")

        if pass_usuario != '' and len(pass_usuario) > 6:
            pass_usuario = encriptar(pass_usuario)

            usuario = {
                "username": nom_usuario,
                "password": pass_usuario
            }

            lista_usuarios.append(usuario)

            print("""
                =============================
                || USUARIO CREADO CON EXITO ||
                ==============================
                """)
        else:
            print("Debes ingresar una contraseña mayor a 6 caracteres")
    else:
        print("Debes ingresar por lo menos 4 caracteres")


def login():

    if lista_usuarios != []:
        saludo_usuario()
        usuario = input("Ingresa tu usuario: ").lower()

        for usuario_lista in lista_usuarios:
            nom, pwd = usuario_lista.values()

            if usuario == nom:
                limpiar_pantalla()
                print(f"""
                ====================
                Bienvenido {usuario.capitalize()}
                ====================
                    """)

                contraseña = input("Ingresa tu contraseña: ").encode()

                if comparar_hashes(contraseña, pwd):
                    return True
                else:
                    print("""
            ===========================
            || Contraseña Incorrecta ||
            ===========================
                        """)
                    continuar()
                    return False
            else:
                print("""
            ===========================
            || USUARIO NO ENCONTRADO ||
            ===========================
                    """)

        continuar()

    else:
        print("""
            =============================
            || AUN NO EXISTEN USUARIOS ||
            =============================
            """)
        continuar()
