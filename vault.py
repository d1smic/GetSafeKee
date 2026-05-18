import json
from cripto_password import deserialize_vault
from cripto_password import serialize_vault
from cryptography.exceptions import InvalidTag
from _hash_master_password import HashMasterPassword

#falta encriptar las entradas
#falta refactorizar load() y save()
class Vault:
    def __init__(self):
        self.entradas = []
    def add_entrada(self,service,username,password):

        entrada = {
            "service":service,
            "username":username,
            "password":password
        }
        self.entradas.append(entrada)
    
    def save(self,fichero,master_password):
        data = json.dumps(self.entradas).encode("utf-8")
        self.encrypted_blob =  serialize_vault(data,master_password) #faltaponer aqui la contradeña maestra
        with open(fichero,"wb") as fp:
            fp.write(self.encrypted_blob)
            
    # def encrypt_vault(self,master_password):
    #     data = json.dumps(self.entradas).encode("utf-8")
    #     self.encrypted_blob =  serialize_vault(data,master_password) #faltaponer aqui la contradeña maestra 
    
    # def guardar_vault(self,fichero):
    #     with open(fichero,"wb") as fp:
    #         fp.write(self.encrypted_blob)
    
    def actualizar_password(self,service,new_password):
        for entrada in self.entradas:
            if entrada["service"].lower() == service.lower():
                entrada["password"] = new_password
                return True
        return False
    
    def actualizar_username(self,service,new_username):
        for entrada in self.entradas:
            if entrada["service"].lower() == service.lower():
                entrada["username"] = new_username
                return True
        return False
    
    def actualizar_servicio(self,service,new_service):
        for entrada in self.entradas:
            if entrada["service"].lower() == service.lower():
                entrada["service"] = new_service
                return True
        return False
    
    
    def borrar_entrada(self,service):
        long_original = len(self.entradas)
        self.entradas = [
            entrada for entrada in self.entradas
            if entrada["service"] != service
        ]
        return len(self.entradas) < long_original
    
    
    
    def listar_entradas(self):
        for entrada in self.entradas:
            print(f"""
                    Servicio:{entrada["service"]}
                    Usuario:{entrada["username"]}
                    Password:{entrada["password"]}                
                """)
        return self.entradas
    
    def buscar_servicio(self,service):
        for entrada in self.entradas:
            if entrada["service"].lower() == service.lower():
                return entrada
        return None

    
    
    
    def load(self,fichero,master_password):
        
        with open(fichero,"rb") as fp:
            blob = fp.read()
        try:

            textoplano = deserialize_vault(
                blob,
                master_password
            )
            self.entradas = json.loads(
                textoplano.decode("utf-8")
            )

        except InvalidTag:
            self.entradas = []
            print("Contraseña incorrecta o vault corrupto")
        else:
            print("Vault abierto")





#PRUEBAS

vault = Vault()


vault.add_entrada(
    "gmail",
    "juan@gmail.com",
    "1234A"
)


#contraseña de vaultt.bin es "hola", esto es de prueba

vault.save(
    "vaultt.bin",
    "hola"
)

vault.load(
    "vaultt.bin",
    "hola"
)

#vault.listar_entradas()

# resultado = vault.buscar_servicio("ada")
# if resultado:
#     print(resultado)
# else:
#     print("Servicio no encotrado")

vault.actualizar_username("gmail","prueba@gmail.com")
vault.actualizar_password("gmail","prueba123")
vault.actualizar_servicio("gmail","no")
vault.listar_entradas()
with open("vaultt.bin", "rb") as f:

    print(f.read())