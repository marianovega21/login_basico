import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
#aca estoy usando la version 3.9.6 de python no uso la version 3.8.5 que uso ppara el machine learning porque en esa no instale el python sql

def menu_opciones():
    #cuadro entero
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x380")
    pantalla.title("bienvenido")

    #reemplazo de plumita sql

    #logotipo

    #cuadro inferior
    Label(text="Welcome to register", bg="#220B29", fg="white", width="300", height="3", font=("Calibri", 15), anchor="n").pack()
    Label(text="").pack()

    #botones de iniciar sesion y registrarse
    Button(text="Start Sesion", height="3", width="30",font=("Calibri", 10), bg="navy", command=
    inicio_sesion).pack()
    Label(text="").pack()
    Button(text="Register", height="3", width="30", font=("Calibri", 10), bg="navy", command=registro).pack()

    pantalla.mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1= Toplevel(pantalla)
    pantalla1.geometry("400x200")
    pantalla1.title("inicio de sesion")
    #aca iria pantalla1.title(logo)
    Label(pantalla1, text="ingrese su usuario y contraseña", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(pantalla1, text="").pack()

    global nombredeusuario_verificacion
    global clavedeusuario_verificacion

    nombredeusuario_verificacion=StringVar()
    clavedeusuario_verificacion=StringVar()

    global nombredeusuario_entrada
    global clavedeusuario_entrada

    Label(pantalla1, text="Usuario").pack()
    nombredeusuario_entrada=Entry(pantalla1, textvariable=nombredeusuario_verificacion)
    nombredeusuario_entrada.pack()

    Label(pantalla1, text="Clave").pack()
    clavedeusuario_entrada=Entry(pantalla1, show="*", textvariable=clavedeusuario_verificacion)
    clavedeusuario_entrada.pack()

    Button(pantalla1, text="Start sesion", command=validacion_datos).pack()

def registro():
    global pantalla2
    pantalla2= Toplevel(pantalla)
    pantalla2.geometry("400x200")
    pantalla2.title("inicio de sesion")

    global nombredeusuario_entry
    global clave_entry

    nombredeusuario_entry=StringVar()
    clave_entry=StringVar()

    Label(pantalla2, text="please ingrese un usuario y contraseña para el registro", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15) )
    Label(pantalla2, text="").pack

    Label(pantalla2, text="Users").pack()
    nombredeusuario_entry=Entry(pantalla2)
    nombredeusuario_entry.pack()
    Label(pantalla2).pack

    Label(pantalla2, text="Pasarrow").pack()
    clave_entry=Entry(pantalla2, show="*")
    clave_entry.pack()
    Label(pantalla2).pack

    Button(pantalla2, text="register your new user", command=insertar_datos).pack()

def insertar_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="basededatos2"
        )

    fcursor=bd.cursor()
    sql="INSERT INTO login (usuario, clave) VALUES ('{0}', '{1}')".format(nombredeusuario_entry.get(), clave_entry.get())
        
    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="register suceff", title="aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="no se registro", title="aviso")
    bd.close()

def validacion_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="basededatos2"
        )

    fcursor=bd.cursor()

    fcursor.execute("SELECT clave FROM login WHERE usuario='"+nombredeusuario_verificacion.get()+"' and clave='"+clavedeusuario_verificacion.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo(title="correcto inicio de sesion", message="usuario y contraseña coinciden")
    else:
        messagebox.showinfo(title="no se puede iniciar sesion", message="jeje pusiste mal la contraseña")
    bd.close()

menu_opciones()