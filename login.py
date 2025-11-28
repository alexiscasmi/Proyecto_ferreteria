import sqlite3
from tkinter import *
import tkinter as tk 
from tkinter import ttk, messagebox
from container import Container
from PIL import Image, ImageTk
import os

class Login(tk.Frame):
    db_name = "C:/Users/Usuario/vsc.curso/ferretería/database.db"

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.controlador = controlador
        self.widgets()

    def validacion(self, user, pas):
        return len(user) > 0 and len(pas) > 0
    
    def login(self):
        user = self.username.get().strip()
        pas = self.password.get().strip()
        
        print("Usuario ingresado:", user)
        print("Contraseña ingresada:", pas)
        
        if self.validacion(user, pas):
            consulta = "SELECT * FROM usuarios WHERE LOWER(username) = LOWER(?) AND password = ?"
            parametros = (user, pas)
            try:
                with sqlite3.connect(self.db_name) as conn:
                    cursor = conn.cursor()
                    cursor.execute(consulta, parametros)
                    result = cursor.fetchall()
                    print("Resultado de la consulta:", result)
                    
                    if result:
                        self.control1()
                    else:
                        self.username.delete(0, "end")
                        self.password.delete(0, "end")
                        messagebox.showerror(title="Error", message="Usuario y/o contraseña incorrecta")
            except sqlite3.Error as e:
                messagebox.showerror(title="Error", message=f"No se conectó a la base de datos: {e}")
        else:
            messagebox.showerror(title="Error", message="Llene todas las casillas")


    def control1(self):
        self.controlador.show_frame(Container)

    def control2(self):
        self.controlador.show_frame(Registro)

    def widgets(self):
        fondo = tk.Frame(self, bg="#C6D9E3")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)

        ruta_imagen = os.path.join(os.path.dirname(__file__), "imagenes", "fondo.jpg")
        print("Buscando imagen en:", ruta_imagen)
        self.bg_image = Image.open(ruta_imagen)
        self.bg_image = self.bg_image.resize((1100, 650))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label.place(x=0, y=0, width=1100, height=650)

        frame1 = tk.Frame(self, background="#FFFFFF", highlightbackground="black", highlightthickness=1)
        frame1.place(x=350, y=70, width=400, height=560)

        ruta_logo = os.path.join(os.path.dirname(__file__), "imagenes", "logo1.jpg")
        print("Buscando logo en:", ruta_logo)
        self.logo_image = Image.open(ruta_logo)
        self.logo_image = self.logo_image.resize((200, 200))
        self.logo_image = ImageTk.PhotoImage(self.logo_image)
        self.logo_label = ttk.Label(frame1, image=self.logo_image)
        self.logo_label.image = self.logo_image  # Importante para evitar que se borre la referencia
        self.logo_label.place(x=100, y=20)


        user = ttk.Label(frame1, text="Nombre de Usuario", font="arial 16 bold", background="#FFFFFF")
        user.place(x=100, y=250)
        self.username = ttk.Entry(frame1, font="arial 16 bold")
        self.username.place(x=80, y=290, height=40)

        pas = ttk.Label(frame1, text="Contraseña", font="arial 16 bold", background="#FFFFFF")
        pas.place(x=100, y=340)
        self.password = ttk.Entry(frame1, show="*", font="arial 16 bold")
        self.password.place(x=80, y=380, width=240, height=40)

        btn1 = tk.Button(frame1, text="Iniciar", font="arial 16 bold", command=self.login)
        btn1.place(x=80, y=440, width=240, height=40)

        btn2 = tk.Button(frame1, text="Registrar", font="arial 16 bold", command=self.control2)
        btn2.place(x=80, y=500, width=240, height=40)

class Registro(tk.Frame):
    db_name = "C:/Users/Usuario/vsc.curso/ferretería/database.db"

    def __init__(self, padre, controlador):
        super().__init__(padre)
        self.pack()
        self.place(x=0, y=0, width=1100, height=650)
        self.controlador = controlador
        self.widgets()

    def validacion(self, user, pas):
        return len(user) > 0 and len(pas) > 0
    
    def eje_consulta(self, consulta, parametros=()):
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(consulta, parametros)
                conn.commit
        except sqlite3.Error as e:
            messagebox.showerror(title="Error", massage="Error al ejecutar la consulta: {}".format(e))
            
    def registro(self):
        user = self.username.get()
        pas = self.password.get()
        key = self.key.get()
        if self.validacion(user, pas):
            if len(pas) < 6:
                messagebox.showerror(title="Error", message="Contraseña demasiado corta")
                self.username.delete(0, 'end')
                self.password.delete(0, 'end')
            else:
                if key =="1234":
                    consulta = "INSERT INTO usuarios VALUES (?,?,?)"
                    parametros = (None, user, pas)
                    self.eje_consulta(consulta, parametros)
                    self.control1()
                else:
                    messagebox.showerror(title="Registro", message="Error al ingresar el codigo de registro")
        else:
            messagebox.showerror(title="Error", message="Llene sus datos")

    def control1(self):
        self.controlador.show_frame(Container)
    
    def control2(self):
        self.controlador.show_frame(Login)

    def widgets(self):
        fondo = tk.Frame(self, bg="#C6D9E3")
        fondo.pack()
        fondo.place(x=0, y=0, width=1100, height=650)

        ruta_imagen = os.path.join(os.path.dirname(__file__), "imagenes", "fondo.jpg")
        print("Buscando imagen en:", ruta_imagen)
        self.bg_image = Image.open(ruta_imagen)
        self.bg_image = self.bg_image.resize((1100, 650))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = ttk.Label(fondo, image=self.bg_image)
        self.bg_label.place(x=0, y=0, width=1100, height=650)

        frame1 = tk.Frame(self, background="#FFFFFF", highlightbackground="black", highlightthickness=1)
        frame1.place(x=350, y=10, width=400, height=630)

        ruta_imagen = os.path.join(os.path.dirname(__file__), "imagenes", "logo1.jpg")
        print("Buscando imagen en:", ruta_imagen)
        logo_img = Image.open(ruta_imagen)
        logo_img = logo_img.resize((200, 200))
        self.logo_image = ImageTk.PhotoImage(logo_img)  
        self.logo_label = ttk.Label(frame1, image=self.logo_image)
        self.logo_label.image = self.logo_image  
        self.logo_label.place(x=100, y=20)


        user = ttk.Label(frame1, text="Nombre de Usuario", font="arial 16 bold", background="#FFFFFF")
        user.place(x=100, y=250)
        self.username = ttk.Entry(frame1, font="arial 16 bold")
        self.username.place(x=80, y=290, height=40)

        pas = ttk.Label(frame1, text="Contraseña", font="arial 16 bold", background="#FFFFFF")
        pas.place(x=100, y=340)
        self.password = ttk.Entry(frame1, show="*", font="arial 16 bold")
        self.password.place(x=80, y=380, width=240, height=40)

        key = ttk.Label(frame1, text="Codigo de Registro", font="arial 16 bold", background="#FFFFFF" )
        key.place(x=100, y=430)
        self.key = ttk.Entry(frame1, show="*", font="arial 16 bold")
        self.key.place(x=80, y=470, width=240, height=40)

        btn3 = tk.Button(frame1, text="Registrarse", font="arial 16 bold", command=self.registro)
        btn3.place(x=80, y=520, width=240, height=40)

        btn4 = tk.Button(frame1, text="Regresar", font="arial 16 bold", command=self.control2)
        btn4.place(x=80, y=570, width=240, height=40)
 


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ventana de Login")

    # Establecer tamaño y posición: "anchoxalto+x+y"
    root.geometry("1100x650+120+20")

    # Crear y mostrar el frame de login
    login_frame = Login(root, controlador=None)
    login_frame.pack(expand=True, fill="both")

    root.mainloop()