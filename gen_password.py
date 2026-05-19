import secrets
import string
#falta hacer el generador de contraseñas
pwd_len = 12

letras = string.ascii_letters

digitos = string.digits

caracteres_especiales = string.punctuation

alfabeto = letras,digitos,caracteres_especiales

class GeneratorPassword:
    def __init__(self):
        self.letras = string.ascii_letters
        self.digitos = string.digits
        self.caracteres_especiales = string.punctuation
        self.alfabeto = self.letras + self.digitos + self.caracteres_especiales
    def generation(self,longitud):

        print( ''.join(secrets.choice(self.alfabeto) for _ in range(longitud)))
    
    def evaluar_password(self,clave):
        longitud = len(clave)
        puntaje = 0
        if any(c.islower() for c in clave):
            puntaje += 1

        if any(c.isupper() for c in clave):
            puntaje += 1

        if any(c.isdigit() for c in clave):
            puntaje += 1

        if any(c in string.punctuation for c in clave):
            puntaje += 1

        if longitud >= 12:
            puntaje += 1
        
        niveles = ["Muy débil", "Débil", "Aceptable", "Fuerte", "Muy fuerte"]
        print(niveles[puntaje - 1] if puntaje > 0 else "Muy débil", puntaje)
        print(clave)

gen = GeneratorPassword()

gen.generation(12)
gen.evaluar_password('8h)"^sE":%Y;')