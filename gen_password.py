import secrets
import string
#falta hacer el generador de contraseñas
pwd_len = 12

letras = string.ascii_letters

digitos = string.digits

caracteres_especiales = string.punctuation

alfabeto = letras,digitos,caracteres_especiales
pwd = ""
for i in range(pwd_len):
    pwd = ''.join(secrets.choice(alfabeto))

print(pwd)