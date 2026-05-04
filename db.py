import mysql.connector
from mysql.connector import errorcode

class ServicioMySQL:
    def __init__(self):
        self.config_servidor = {
            'user':'',
            'password':'',
            'host':'localhost',
            'port':'33060'
        }
        self.config_app = self.config_servidor.copy()
        self.config_app['database'] = 'GetSafeKee'

        self._crear_database_si_no_existe()
        self._crear_tabla_si_no_existe()

    def _conectar_al_servidor(self):
        return mysql.connector.connect(**self.config_servidor)
    
    def _conectar_a_db(self):
        return mysql.connector.connect(**self.config_app)

    def _crear_database_si_no_existe(self):
        conn = self._conectar_a_db()
        cursor = conn.cursor()
        cursor.execute("""
                        CREATE DATABASE IF NOT EXISTS getsafekee
                       """)
        conn.commit()
        cursor.close()
        conn.close()
        
    def _crear_tabla_si_no_existe(self):
        conn = self._conectar_a_db()
        cursor = conn.cursor()
        cursor.execute("""  

                        poner aqui las tablas necesarias para el proyecto  

                    """)
        conn.commit()
        cursor.close()
        conn.close()
    
    def cargar_todo(self):
        conn = self._conectar_a_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("aqui van los selects de las tabalas para verlas")
        resultados = cursor.fetchall()
        for r in resultados:
            r['completada'] = bool(r['completada'])
        cursor.close()
        conn.close
        return resultados
        
    