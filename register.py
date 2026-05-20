import customtkinter as ctk
from tkinter import filedialog

class RegisterWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("REGISTER")
        self.geometry("700x500")

        title = ctk.CTkLabel(
            self,
            text="Crear nuevo archivo",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=30)

        #
        self.introducir_archivo = ctk.CTkEntry(
            self,
            placeholder_text="../Archivo",
            width=300,
            height=40
        )
        self.introducir_archivo.pack(pady=10)

        boton_archivo = ctk.CTkButton(
            self,
            text="Seleccionar directorio",
            command=self.seleccionar_archivo,
            fg_color="#1E8A2D",
            hover_color="#6B6B6B",
            width=300
        )
        boton_archivo.pack(pady=5)

        #
        self.password_entry = ctk.CTkEntry(
            self,
            placeholder_text="Contraseña",
            show="*",
            width=300,
            height=40
        )
        self.password_entry.pack(pady=10)

        #
        register_btn = ctk.CTkButton(
            self,
            text="Crear archivo",
            fg_color="#1E8A2D",
            hover_color="#6B6B6B",
            width=300,
            height=40
        )
        register_btn.pack(pady=20)

    # FUNCION PARA SELECCIONAR ARCHIVO 
    def seleccionar_archivo(self):
        archivo = filedialog.askopenfilename()
        self.introducir_archivo.delete(0, "end")
        self.introducir_archivo.insert(0, archivo)

if __name__ == "__main__":
    app = RegisterWindow()
    app.mainloop()