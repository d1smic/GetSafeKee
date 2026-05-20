import customtkinter as ctk

class addWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Add_datos")
        self.geometry("720x500")

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

        # Frame para contraseña y botón generar
        password_frame = ctk.CTkFrame(self, fg_color="transparent")
        password_frame.pack(pady=10)

        # Introducir Contraseña
        self.introducir_password = ctk.CTkEntry(
            password_frame,
            placeholder_text="Contraseña",
            show="*",
            width=200,
            height=40
        )
        self.introducir_password.pack(side="left", padx=(0, 10))

        # Botón Generar Contraseña
        boton_generar = ctk.CTkButton(
            password_frame,
            text="Generar",
            fg_color="#1E8A2D",
            hover_color="#6B6B6B",
            width=50,
            height=40,
            command=self.generar_contraseña
        )
        boton_generar.pack(side="left")

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
            self,text="Cancelar",
            fg_color="#1E8A2D",
            hover_color="#6B6B6B",
            border_width=1,
            width=300,
            command=self.cancelar
        )
        boton_cancelar.pack()

    def generar_contraseña(self):
        """Genera una contraseña aleatoria"""
        print("Generar contraseña")
        # Aquí tus compañeros implementarán el generador de contraseñas
        # Por ejemplo, pueden usar random, string, etc.

    def añadir_datos(self):
        print("Datos registrados")

    def cancelar(self):
        print("Cancelado")
        print("Volviendo al dashboard")

if __name__ == "__main__":
    app = addWindow()
    app.mainloop()