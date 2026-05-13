import json
from cripto_password import deserialize_vault
from cripto_password import serialize_vault
from cryptography.exceptions import InvalidTag
from _hash_master_password import HashMasterPassword

#falta encriptar las entradas
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
    
    def encrypt_vault(self,master_password):
        data = json.dumps(self.entradas).encode("utf-8")
        self.encrypted_blob =  serialize_vault(data,master_password) #faltaponer aqui la contradeña maestra 
    
    def guardar_vault(self,fichero):
        with open(fichero,"wb") as fp:
            fp.write(self.encrypted_blob)
    
    def borrar_entrada(self,service): #por acabar esta funvion
        self.entradas = [
            entrada for entrada in self.entradas
            if entrada["service"] != service
        ]
    
    def listar_entradas(self):
        for entrada in self.entradas:
            print(f"""
                    Servicio:{entrada["service"]}
                    Usuario:{entrada["username"]}
                    Password:{entrada["password"]}                
                """)
    
    def buscar_listado(self,service): #no busca bien, arreglar la fiuncion
        for entrada in self.entradas:
            if entrada["service"] == service:
                return entrada
        return None

    def cargar_vault(self,fichero,master_password):
        
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



vault = Vault()


# vault.add_entrada(
#     "gmail",
#     "juan@gmail.com",
#     "1234A"
# )



vault.cargar_vault(
    "vaultt.bin",
    "hola"
)

vault.listar_entradas()
vault.buscar_listado("service")

#print(vault.entradas)
