import tkinter as tk
from tkinter import Text, Scrollbar, RIGHT, Y, BOTH, END

class Informacion(tk.Frame):
    def __init__(self, padre):
        super().__init__(padre, bg="#C6D9E3")
        self.pack(expand=True, fill="both")
        self.widgets()

    def widgets(self):
        # Scrollbar
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Área de texto con scroll
        texto_info = Text(self, wrap="word", font=("sans", 12), yscrollcommand=scrollbar.set, bg="#F4F9FB")
        texto_info.pack(expand=True, fill=BOTH)
        scrollbar.config(command=texto_info.yview)

        contenido = """
💼 SISTEMA DE GESTIÓN DE VENDEDORES – FERRETERÍA "FerreMax"

🧾 INFORMACIÓN GENERAL DEL PROYECTO
Nombre del Proyecto: Sistema de Gestión de Vendedores
Área Aplicativa: Ferretería y materiales de construcción
Lenguaje de Programación: Python
Interfaz Gráfica: Tkinter
Base de Datos: SQLite3
Objetivo Principal: Automatizar y simplificar el proceso de registro, consulta y modificación de vendedores para mejorar la organización interna y la eficiencia comercial de la ferretería.

🛠️ DESCRIPCIÓN DEL SISTEMA
Este sistema ha sido diseñado como una solución digital integral para la gestión de vendedores dentro de una ferretería. A través de una interfaz gráfica amigable y moderna, los usuarios pueden ingresar, consultar y modificar los datos personales y de contacto de los vendedores de manera rápida y segura.

🎨 DISEÑO E INTERFAZ
El sistema cuenta con una interfaz estética y funcional, destacando el uso de colores suaves como el azul pastel (#C6D9E3) que aportan profesionalismo y comodidad visual. Se han implementado fuentes sans en estilo negrita y tamaño grande para mejorar la lectura.

⚙️ FUNCIONALIDADES CLAVE
• Ingreso de vendedores con validación de campos.
• Modificación de datos con edición en ventana emergente.
• Visualización clara de registros en tabla.
• Interacción intuitiva con botones, etiquetas y alertas informativas.

🎯 BENEFICIOS DEL SISTEMA
• Evita errores en el registro manual.
• Centraliza los datos de vendedores.
• Facilita el acceso y modificación de la información.
• Mejora el control interno y la toma de decisiones.
• Escalable a nuevos módulos como ventas, productos, reportes, etc.

"""
        texto_info.insert(END, contenido)
        texto_info.config(state="disabled")