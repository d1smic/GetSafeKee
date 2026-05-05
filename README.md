# 🔐 Password Manager - Proyecto DAW1

## 📌 Descripción

Proyecto de un gestor de contraseñas desarrollado en Python con programación orientada a objetos.

El objetivo es crear una aplicación de escritorio con interfaz gráfica capaz de:

- Gestionar contraseñas de forma segura
- Cifrar información sensible
- Almacenar datos en MySQL
- Detectar contraseñas filtradas en leaks
- Enviar notificaciones por correo
- Aplicar buenas prácticas de seguridad y arquitectura

---

# 🎯 Objetivos del Proyecto

## Funcionalidades principales

- Registro e inicio de sesión
- Gestión de contraseñas
- CRUD completo
- Interfaz gráfica con Tkinter
- Cifrado de contraseñas almacenadas
- Hash seguro de la contraseña maestra
- Base de datos MySQL
- Verificación de contraseñas comprometidas mediante API
- Notificaciones por correo electrónico

---

# 🛠 Tecnologías utilizadas

| Tecnología | Uso |
|---|---|
| Python | Lenguaje principal |
| Tkinter | Interfaz gráfica |
| MySQL | Base de datos |
| bcrypt | Hash de contraseñas |
| cryptography (Fernet) | Cifrado |
| requests | Consumo de APIs |
| smtplib | Envío de correos |
| dotenv | Variables de entorno |

---

# 📂 Estructura del Proyecto

```text
password_manager/
│
├── main.py
│
├── config/
│   └── db_config.py
│
├── database/
│   └── connection.py
│
├── models/
│   ├── usuario.py
│   └── password_entry.py
│
├── services/
│   ├── auth_service.py
│   ├── encryption_service.py
│   ├── leak_checker_service.py
│   ├── email_service.py
│   └── password_service.py
│
├── ui/
│   ├── login_window.py
│   ├── register_window.py
│   ├── dashboard_window.py
│   └── add_password_window.py
│
├── utils/
│   └── validators.py
│
├── requirements.txt
│
└── README.md
```

---

# 🧱 Arquitectura del Proyecto

El proyecto seguirá una arquitectura por capas para separar responsabilidades.

```text
Interfaz gráfica (Tkinter)
        ↓
Servicios (Lógica de negocio)
        ↓
Modelos
        ↓
Base de datos (MySQL)
```

---

# 🗄 Diseño de Base de Datos

## Tabla: usuarios

```sql
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password_hash VARCHAR(255),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Tabla: passwords

```sql
CREATE TABLE passwords (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    sitio VARCHAR(100),
    username VARCHAR(100),
    password_encrypted TEXT,
    notas TEXT,
    fecha_modificacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
```

---

# 🔒 Seguridad

## Hash de contraseña maestra

La contraseña de acceso del usuario NO se almacenará en texto plano.

Se utilizará:

- bcrypt

### Flujo

```text
Contraseña del usuario
        ↓
Hash bcrypt
        ↓
Guardar en MySQL
```

---

## Cifrado de contraseñas almacenadas

Las contraseñas guardadas dentro del gestor se cifrarán usando:

- cryptography
- Fernet

### Flujo

```text
Contraseña original
        ↓
Cifrado Fernet
        ↓
Guardar en base de datos
```

---

# 🌐 API de filtraciones de datos

Se utilizará la API gratuita de Have I Been Pwned.

## Funcionalidad

Comprobar si una contraseña ha aparecido en filtraciones de datos conocidas.

### Objetivo

Avisar al usuario cuando una contraseña sea insegura.

### Método utilizado

- SHA1
- k-Anonymity

Esto evita enviar la contraseña completa a la API.

---

# 📧 Sistema de Correos

## Funcionalidades

- Aviso de cambio de contraseña
- Aviso de nuevo inicio de sesión
- Confirmación de registro

## Opciones

### Opción básica

- SMTP de Gmail

### Opción avanzada

- SendGrid
- Mailgun

---

# 🖥 Interfaz Gráfica

## Ventanas principales

### Login

- Email
- Contraseña
- Botón iniciar sesión
- Acceso a registro

---

### Registro

- Nombre
- Email
- Contraseña

---

### Dashboard

- Lista de contraseñas
- Añadir contraseña
- Editar contraseña
- Eliminar contraseña
- Copiar contraseña
- Buscar registros

---

# 📚 Programación Orientada a Objetos

## Clases principales

| Clase | Responsabilidad |
|---|---|
| Usuario | Datos del usuario |
| PasswordEntry | Contraseña almacenada |
| DatabaseManager | Gestión MySQL |
| AuthService | Login y registro |
| EncryptionService | Cifrado |
| LeakCheckerService | API de leaks |
| EmailService | Correos |
| PasswordService | CRUD de contraseñas |

---

# 🚀 Roadmap de Desarrollo

# FASE 1 — Base del proyecto

- Crear estructura de carpetas
- Configurar MySQL
- Conexión a base de datos
- CRUD básico

---

# FASE 2 — Interfaz gráfica

- Ventana login
- Ventana registro
- Dashboard principal

---

# FASE 3 — Seguridad

- Implementar bcrypt
- Implementar cifrado Fernet

---

# FASE 4 — API leaks

- Conectar API
- Validar contraseñas filtradas

---

# FASE 5 — Correos

- Envío de emails automáticos
- Alertas de seguridad

---

# FASE 6 — Extras

- Generador de contraseñas
- Indicador de seguridad
- Copiar al portapapeles
- Exportar backup cifrado

---

# 🔮 Mejoras Futuras

## Posibles mejoras

- Autenticación 2FA
- FIDO2
- Reconocimiento facial
- Sincronización cloud
- Aplicación móvil
- Tema oscuro
- Generador avanzado de contraseñas

---

# ⚠ Dificultades del Proyecto

| Característica | Dificultad |
|---|---|
| CRUD MySQL | 🟢 |
| Tkinter | 🟢 |
| bcrypt | 🟡 |
| Cifrado Fernet | 🟡 |
| APIs | 🟡 |
| FIDO2 | 🔴 |

---

# 📖 Conceptos Aprendidos

- Programación orientada a objetos
- Arquitectura por capas
- Seguridad informática básica
- Hash y cifrado
- APIs REST
- Gestión de bases de datos
- Interfaces gráficas
- Buenas prácticas en Python

---

# 👨‍💻 Autor

Proyecto desarrollado como práctica de aprendizaje para DAW1.
