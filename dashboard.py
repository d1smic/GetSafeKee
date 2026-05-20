import customtkinter as ctk
from tkinter import ttk

class Dashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Dashboard")
        self.geometry("1000x600")
        
        # Variable para controlar si las contraseñas están visibles
        self.passwords_visible = False

        # Título
        title = ctk.CTkLabel(
            self,
            text="Gestor de Contraseñas",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=20)

        # Barra búsqueda
        self.search_entry = ctk.CTkEntry(
            self,
            placeholder_text="Buscar...",
            width=300
        )
        self.search_entry.pack(pady=10)

        # Tabla
        columns = ("Servicio", "Usuario", "Contraseña")

        self.table = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            height=15,
            selectmode='browse'  # Permite selección individual
        )

        for col in columns:
            self.table.heading(col, text=col)
            self.table.column(col, width=250)

        self.table.pack(pady=20)
        
        # Binding para seleccionar campo individual al hacer clic
        self.table.bind('<Button-1>', self.on_cell_click)

        # Datos de ejemplo
        self.table.insert("", "end", values=("Gmail", "juan@gmail.com", "******"))
        self.table.insert("", "end", values=("GitHub", "juan123", "******"))

        # Botones
        buttons_frame = ctk.CTkFrame(self)
        buttons_frame.pack(pady=20)

        # Introducir datos (sitio,usuario,passwd)
        boton_añadir = ctk.CTkButton(
            buttons_frame,
            text="Añadir",
            command=self.añadir_password,
            fg_color="#1E8A2D",
            hover_color="#6B6B6B"
        )
        boton_añadir.grid(row=0, column=0, padx=10)

        # Editar datos (sitio,usuario,passwd)
        boton_editar = ctk.CTkButton(
            buttons_frame,
            text="Editar",
            command=self.editar_password,
            fg_color="#1E8A2D",
            hover_color="#6B6B6B"
        )
        boton_editar.grid(row=0, column=1, padx=10)

        # Borrar datos (sitio,usuario,passwd)
        boton_borrar = ctk.CTkButton(
            buttons_frame,
            text="Eliminar",
            command=self.borrar_password,
            fg_color="#1E8A2D",
            hover_color="#6B6B6B"
        )
        boton_borrar.grid(row=0, column=2, padx=10)

        # Mostrar/ocultar las contraseñas
        boton_mostrar = ctk.CTkButton(
            buttons_frame,
            text="Mostrar/Ocultar",
            command=self.mostrar_passwords,
            fg_color="#1E8A2D",
            hover_color="#6B6B6B"
        )
        boton_mostrar.grid(row=0, column=3, padx=10)

    def añadir_password(self):
        print("Añadir")

    def editar_password(self):
        print("Editar")

    def borrar_password(self):
        print("Eliminar")
    
    def mostrar_passwords(self):
        """Alterna entre mostrar y ocultar contraseñas"""
        print("Mostrar/Ocultar contraseñas")
        # Aquí tus compañeros implementarán la lógica para mostrar/ocultar
        # Por ahora solo imprime el mensaje
    
    #Detecta qué celda específica fue clickeada
    def on_cell_click(self, event):
        """Detecta qué celda específica fue clickeada"""
        region = self.table.identify_region(event.x, event.y)
        if region == "cell":
            column = self.table.identify_column(event.x)
            row = self.table.identify_row(event.y)
            
            # Obtener el índice de la columna (ej: '#1', '#2', '#3')
            col_index = int(column.replace('#', '')) - 1
            col_names = ["Servicio", "Usuario", "Contraseña"]
            
            if row:
                # Obtener el valor de la celda
                item = self.table.item(row)
                cell_value = item['values'][col_index]
                print(f"Seleccionado: {col_names[col_index]} = {cell_value}")
                # Aquí tus compañeros pueden implementar lógica adicional
                # como copiar automáticamente el valor al portapapeles


if __name__ == "__main__":
    app = Dashboard()
    app.mainloop()