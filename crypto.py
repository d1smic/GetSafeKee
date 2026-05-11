import os
import struct
from argon2.low_level import hash_secret_raw, Type
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag


VERSION = 1

def genera_sal() -> bytes:
    return os.urandom(16) # pide bytes random al SO
     # 16 bytes = 128 bits, casi imposible de coincidir
     # Para q dos vaults con la misma contraseña tengan claves distintas


def derivar_clave(password: str, salt: bytes) -> bytes:
    return hash_secret_raw(
        secret=password.encode("utf-8"),  # str → bytes
        salt=salt,
        time_cost=3,        # nº de iteraciones
        memory_cost=65536,  # RAM usada 64MB (dificulta ataques con GPU)
        parallelism=4,      
        hash_len=32,        # 32 bytes = clave AES-256
        type=Type.ID        # variante más segura de Argon2
    ) # Pasa de contraseña '1234' a 32 bytes random que AES usa como clave
      # Es lento para los atacantes
 

def encrypt(data: bytes, key: bytes) -> bytes:
    nonce = os.urandom(12)   # num de un solo uso (96 bits)               
    aesgcm = AESGCM(key)
    ciphertext = aesgcm.encrypt(nonce, data, None)  # cifra y añade tag de autenticación
    return nonce + ciphertext  # guardamos el nonce delante para poder recuperarlo al descifrar
    # garantiza que cifrar lo mismo dos veces da resultados distintos


def decrypt(blob: bytes, key: bytes) -> bytes:
    nonce      = blob[:12]   # los primeros 12 bytes son el nonce que pusimos antes
    ciphertext = blob[12:]   # el resto es el mensaje cifrado + tag
    aesgcm = AESGCM(key)
    # Si la clave es incorrecta o alguien modificó el archivo → lanza InvalidTag
    return aesgcm.decrypt(nonce, ciphertext, None)


def serialize_vault(plaintext: bytes, password: str) -> bytes:
    # Layout final: [ 4B versión | 16B sal | 12B nonce | ciphertext | 16B tag ]
    salt      = genera_sal()
    key       = derivar_clave(password, salt)
    encrypted = encrypt(plaintext, key)

    version_bytes = struct.pack(">I", VERSION)  # entero → 4 bytes binarios
    return version_bytes + salt + encrypted


def deserialize_vault(blob: bytes, password: str) -> bytes:
    version   = struct.unpack(">I", blob[:4])[0]  # por ahora no lo usamos, pero lo guardamos
    salt      = blob[4:20]   # bytes 4 al 19 → la sal
    encrypted = blob[20:]    # todo lo demás → datos cifrados

    key = derivar_clave(password, salt)
    return decrypt(encrypted, key)  # lanza InvalidTag si la contraseña es incorrecta
    # Extraemos cada trozo según el layout definido arriba



# if __name__ == "__main__":
#     datos    = b'{"entries": []}'
#     password = "MiContraseñaTest123!"

#     # Cifrar y descifrar debe devolver lo mismo
#     blob      = serialize_vault(datos, password)
#     resultado = deserialize_vault(blob, password)
#     assert resultado == datos, "ERROR: el descifrado no coincide"

#     # 2. Contraseña incorrecta debe lanzar InvalidTag
#     try:
#         deserialize_vault(blob, "ContraseñaMal")
#         assert False, "ERROR: debería haber fallado"
#     except InvalidTag:
#         pass  # correcto

#     # 3. Dos cifrados del mismo dato deben ser distintos (nonce aleatorio)
#     blob2 = serialize_vault(datos, password)
#     assert blob != blob2, "ERROR: el nonce no es aleatorio"

#     print("✓ crypto.py correcto, puedes continuar")