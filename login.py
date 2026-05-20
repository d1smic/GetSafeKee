import customtkinter as ctk
from tkinter import filedialog


class LoginWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("LOGIN")
        self.geometry("720x500")

        # TITULO
        titulo = ctk.CTkLabel(
            self,
            text="Accede a tus contraseñas",
            font=("Arial", 30, "bold")
        )
        titulo.pack(pady=40)

        # Introducir Archivo
        self.introducir_archivo = ctk.CTkEntry(
            self,
            placeholder_text="../Archivo",
            width=300,
            height=40
        )
        self.introducir_archivo.pack(pady=10)

        boton_archivo = ctk.CTkButton(
            self,
            text="Buscar archivo",
            command=self.seleccionar_archivo,
            fg_color="#1E8A2D",
            hover_color="#6B6B6B",
            width=300
        )
        boton_archivo.pack(pady=5)

        # Introducir Contraseña
        self.introducir_password = ctk.CTkEntry(
            self,
            placeholder_text="Contraseña",
            show="*",
            width=300,
            height=40
        )
        self.introducir_password.pack(pady=10)

        # Boton acceso a archivo
        boton_login = ctk.CTkButton(
            self,
            text="Acceder",
            fg_color="#1E8A2D",
            hover_color="#6B6B6B",
            width=300,
            height=40
        )
        boton_login.pack(pady=20)

        # Boton crear nuevo archivo
        boton_register = ctk.CTkButton(
            self,text="Crear nuevo archivo",
            fg_color="#1E8A2D",
            hover_color="#6B6B6B",
            border_width=1,
            width=300
        )
        boton_register.pack()

    # FUNCION PARA SELECCIONAR ARCHIVO 
    def seleccionar_archivo(self):
        archivo = filedialog.askopenfilename()
        self.introducir_archivo.delete(0, "end")
        self.introducir_archivo.insert(0, archivo)

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()