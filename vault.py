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
    
    def validar_entrada(self,service,username,password):
        if not service.strip():
            return False
        
        if not username.strip():
            return False
        
        if not password.strip():
            return False
        return True
    
    def existe_servico(self,service):
        return(self.buscar_servicio(service) is not None)


    def add_entrada(self,service,username,password):
        if not self.validar_entrada(service,username,password):
            return False
        
        entrada = {
            "service":service,
            "username":username,
            "password":password
        }
        self.entradas.append(entrada)
        return True
    

                
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
        if self.existe_servico(new_service):
            return False
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
    
    
    
    def listar_entradas(self): #borrar el print en la version final
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

    def save(self,fichero,master_password):
        try: 
            data = json.dumps(self.entradas).encode("utf-8")
            self.encrypted_blob =  serialize_vault(data,master_password) #faltaponer aqui la contradeña maestra
            with open(fichero,"wb") as fp:
                fp.write(self.encrypted_blob)
            return True
        
        except PermissionError as e:
            return False
            
        except OSError as e:
            return False

    
    
    def load(self,fichero,master_password):
        try:
            with open(fichero,"rb") as fp:
                blob = fp.read()
            
            if not blob:
                self.entradas = []
                return False

            textoplano = deserialize_vault(
                blob,
                master_password
            )
            entradas = json.loads(
                textoplano.decode("utf-8")
            )

            for entrada in entradas:
                if ("service" not in entrada or "username" not in entrada or "password" not in entrada):
                    return False 
            self.entradas = entradas
            return True

        except FileNotFoundError :
            self.entradas = []
            return False
    
        except InvalidTag:
            self.entradas = []
            return False
        except json.JSONDecodeError:
            self.entradas = []
            return False
        except OSError:
            self.entradas = []
            return False
        
    def lock(self):
        self.entradas = []
        return True



#PRUEBAS

vault = Vault()


# vault.add_entrada(
#     "gmail",
#     "juan@gmail.com",
#     "1234A"
# )


# #contraseña de vaultt.bin es "hola", esto es de prueba

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

vault.add_entrada(
    "github",
    "juan@gmail.com",
    "1234A"
)
# vault.actualizar_username("gmail","prueba@gmail.com")
# vault.actualizar_password("gmail","prueba123")
# vault.actualizar_servicio("gmail","mama")




vault.listar_entradas()
