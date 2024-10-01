import bcrypt

from config import continuar, lista_usuarios

def encriptar(pwd):
    pwd = pwd.encode()
    sal = bcrypt.gensalt()
    encriptar = bcrypt.hashpw(pwd, sal)
    return encriptar


def comparar_hashes(pwd, hash):

    if bcrypt.checkpw(pwd, hash):
        return True
    else:
        return False
