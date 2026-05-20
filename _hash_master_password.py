#clase para hacer el hash de la contraseña
#falta gusrdar el hash en la base de datos

import bcrypt

class HashMasterPassword:
    def __init__(self):
        self.input_password = input("Pon la contraseña maestra: ")
    
    def master_password_to_byte(self):
        self.byte = self.input_password.encode('utf-8')
    
    def salt_master_password_in_bytes(self):
        self.salt = bcrypt.gensalt()
    
    def hash_master_password_in_bytes(self):
        self.hash = bcrypt.hashpw(self.byte, self.salt)
    
    def check_master_password(self):
        self.check_user_password = input("Pon otravez tu contraseña: ")
        self.check_byte = self.check_user_password.encode('utf-8')

        self.result = bcrypt.checkpw(self.check_byte, self.hash)

        if self.result == True:
            print("Estas dentro del sistema")
        else:
            print("No entras al sistema")

# prueba = HashMasterPassword()
# prueba.master_password_to_byte()
# prueba.salt_master_password_in_bytes()
# prueba.hash_master_password_in_bytes()
# prueba.check_master_password()
    




