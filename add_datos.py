import customtkinter as ctk
import secrets
from gen_password import GeneratorPassword

class LoginWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Add_datos")
        self.geometry("720x550")

        # Crear instancia del generador
        self.generador = GeneratorPassword()
        
        # Variable para controlar visibilidad de contraseña
        self.password_visible = False

        # TITULO
        titulo = ctk.CTkLabel(
            self,
            text="Añadir datos",
            font=("Arial", 30, "bold")
        )
        titulo.pack(pady=40)

        # Introducir Servicio
        self.introducir_servicio = ctk.CTkEntry(
            self,
            placeholder_text="Servicio",
            width=300,
            height=40
        )
        self.introducir_servicio.pack(pady=10)

        # Introducir Usuario
        self.introducir_usuario = ctk.CTkEntry(
            self,
            placeholder_text="Usuario",
            width=300,
            height=40
        )
        self.introducir_usuario.pack(pady=10)

        # Frame para contraseña, botón ojo y botón generar
        password_frame = ctk.CTkFrame(self, fg_color="transparent")
        password_frame.pack(pady=10)

        # Introducir Contraseña
        self.introducir_password = ctk.CTkEntry(
            password_frame,
            placeholder_text="Contraseña",
            show="*",
            width=160,
            height=40
        )
        self.introducir_password.pack(side="left", padx=(0, 5))

        # Botón Mostrar/Ocultar Contraseña (Ojo)
        self.boton_ojo = ctk.CTkButton(
            password_frame,
            text="👁️",
            fg_color="#6B6B6B",
            hover_color="#4A4A4A",
            width=40,
            height=40,
            command=self.toggle_password_visibility
        )
        self.boton_ojo.pack(side="left", padx=(0, 5))

        # Botón Generar Contraseña
        boton_generar = ctk.CTkButton(
            password_frame,
            text="Generar",
            fg_color="#1E8A2D",
            hover_color="#6B6B6B",
            width=90,
            height=40,
            command=self.generar_contraseña
        )
        boton_generar.pack(side="left")

        # Frame para longitud de contraseña
        longitud_frame = ctk.CTkFrame(self, fg_color="transparent")
        longitud_frame.pack(pady=5)

        # Label para longitud
        label_longitud = ctk.CTkLabel(
            longitud_frame,
            text="Longitud:",
            font=("Arial", 14)
        )
        label_longitud.pack(side="left", padx=(0, 10))

        # Campo de entrada para longitud
        self.longitud_password = ctk.CTkEntry(
            longitud_frame,
            placeholder_text="12",
            width=60,
            height=30
        )
        self.longitud_password.pack(side="left")
        self.longitud_password.insert(0, "12")  # Valor por defecto

        # Label informativo
        info_label = ctk.CTkLabel(
            longitud_frame,
            text="(entre 8 y 64 caracteres)",
            font=("Arial", 11),
            text_color="gray"
        )
        info_label.pack(side="left", padx=(10, 0))

        # Boton guardar datos
        boton_add_datos = ctk.CTkButton(
            self,
            text="Guardar",
            fg_color="#1E8A2D",
            hover_color="#6B6B6B",
            width=300,
            height=40,
            command=self.añadir_datos
        )
        boton_add_datos.pack(pady=20)

        # Boton cancelar (volver al dashboard)
        boton_cancelar = ctk.CTkButton(
            self,
            text="Cancelar",
            fg_color="#1E8A2D",
            hover_color="#6B6B6B",
            border_width=1,
            width=300,
            command=self.cancelar
        )
        boton_cancelar.pack()

    def toggle_password_visibility(self):
        """Alterna entre mostrar y ocultar la contraseña"""
        if self.password_visible:
            # Ocultar contraseña
            self.introducir_password.configure(show="*")
            self.boton_ojo.configure(text="👁️")
            self.password_visible = False
        else:
            # Mostrar contraseña
            self.introducir_password.configure(show="")
            self.boton_ojo.configure(text="👁️‍🗨️")
            self.password_visible = True

    def generar_contraseña(self):
        """Genera una contraseña aleatoria con la longitud especificada"""
        try:
            # Obtener la longitud ingresada
            longitud = int(self.longitud_password.get())
            
            # Validar longitud (mínimo 8, máximo 64)
            if longitud < 8:
                longitud = 8
                self.longitud_password.delete(0, 'end')
                self.longitud_password.insert(0, "8")
                print("⚠️ Longitud mínima: 8 caracteres")
            elif longitud > 64:
                longitud = 64
                self.longitud_password.delete(0, 'end')
                self.longitud_password.insert(0, "64")
                print("⚠️ Longitud máxima: 64 caracteres")
            
            # Generar contraseña usando el método generation
            password = ''.join(secrets.choice(self.generador.alfabeto) for _ in range(longitud))
            
            # Limpiar el campo de contraseña
            self.introducir_password.delete(0, 'end')
            
            # Insertar la nueva contraseña
            self.introducir_password.insert(0, password)
            
            print(f"✅ Contraseña generada ({longitud} caracteres): {password}")
            
            # Evaluar la fortaleza de la contraseña
            self.generador.evaluar_password(password)
            
        except ValueError:
            print("❌ Error: Ingresa un número válido para la longitud")
            self.longitud_password.delete(0, 'end')
            self.longitud_password.insert(0, "12")

    def añadir_datos(self):
        servicio = self.introducir_servicio.get()
        usuario = self.introducir_usuario.get()
        password = self.introducir_password.get()
        
        if servicio and usuario and password:
            print("\n✅ Datos registrados:")
            print(f"  📌 Servicio: {servicio}")
            print(f"  👤 Usuario: {usuario}")
            print(f"  🔑 Contraseña: {password}")
            
            # Evaluar la contraseña guardada
            print(f"\n🔒 Evaluación de seguridad:")
            self.generador.evaluar_password(password)
        else:
            print("❌ Error: Completa todos los campos")

    def cancelar(self):
        print("❌ Cancelado")
        print("↩️ Volviendo al dashboard")
        self.destroy()

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()