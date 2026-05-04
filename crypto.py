# pip install cryptography argon2-cffi
import os

from argon2.low_level import hash_secret_raw, Type 
def genera_sal() -> bytes:
    return os.urandom(16)

def derivar_clave(password: str, salt: bytes) -> bytes: #define el formato y complica al atacante
    return hash_secret_raw(
        secret=password.encode("utf-8"), 
        salt=salt, 
        time_cost=3, 
        memory_cost=65536, 
        parallelism=4,
        hash_len=32, 
        type=Type.ID
    )