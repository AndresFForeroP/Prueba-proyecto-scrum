import customtkinter
import os
import modules.f_json as fj
import random as rd
lista_genero = ["FEMENINO","MASCULINO"]
lista_vacunas = ["Tiene todas las vacunas","Tiene algunas vacunas","No tiene vacunas"]
def oprimir_boton(app,nombre,especie,raza,genero,edad,dieta,residencia,vacunas,DATA):
    nombre = nombre.get("0.0","end")
    nombre = nombre.replace("\n","")
    print(nombre)
    especie = especie.get("0.0","end")
    especie = especie.replace("\n","")
    raza = raza.get("0.0","end")
    raza = raza.replace("\n","")
    genero = genero.get()
    edad = edad.get("0.0","end")
    edad = edad.replace("\n","")
    dieta = dieta.get("0.0","end")
    dieta = dieta.replace("\n","")
    residencia = residencia.get("0.0","end")
    residencia = residencia.replace("\n","")
    vacunas = vacunas.get()
    app.destroy()
    diccionario = fj.leer_json(DATA)
    id = rd.randrange(1,999999)
    if id in diccionario:
        id = rd.randrange(1,99999)
    nueva_mascota = {id:{
        "nombre":nombre,
        "especie":especie,
        "raza":raza,
        "genero":genero,
        "edad":edad,
        "dieta":dieta,
        "residencia":residencia,
        "vacunas":vacunas
    }}
    fj.actualizar_json(DATA,nueva_mascota)
def añadir_mascota(DATA):
    app = customtkinter.CTk()
    app.title("Gestion de mascotas")
    app.geometry('500x820')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    label = customtkinter.CTkLabel(app,text="Ingrese el nombre de su mascota")
    label.grid(row=0, column=0, padx=0, pady=0)
    P = customtkinter.CTkTextbox(app,width=150,height=30)
    P.grid(row=1, column=0, padx=20, pady=20)
    label2 = customtkinter.CTkLabel(app,text="Ingrese la especie de su mascota")
    label2.grid(row=2, column=0, padx=0, pady=0)
    P2 = customtkinter.CTkTextbox(app,width=150,height=30)
    P2.grid(row=3, column=0, padx=20, pady=20)
    label3 = customtkinter.CTkLabel(app,text="Ingrese la raza de su mascota")
    label3.grid(row=4, column=0, padx=0, pady=0)
    P3 = customtkinter.CTkTextbox(app,width=150,height=30)
    P3.grid(row=5, column=0, padx=20, pady=20)
    label4 = customtkinter.CTkLabel(app,text="Ingrese el genero de su mascota")
    label4.grid(row=6, column=0, padx=0, pady=0)
    P4 = customtkinter.CTkOptionMenu(app,width=150,height=30,values=lista_genero)
    P4.grid(row=7, column=0, padx=20, pady=20)
    label5 = customtkinter.CTkLabel(app,text="Ingrese la edad de su mascota")
    label5.grid(row=8, column=0, padx=0, pady=20)
    P5 = customtkinter.CTkTextbox(app,width=150,height=30)
    P5.grid(row=9, column=0, padx=20, pady=20)
    label6 = customtkinter.CTkLabel(app,text="Ingrese nombre de la dieta de su mascota")
    label6.grid(row=0, column=1, padx=20, pady=20)
    P6 = customtkinter.CTkTextbox(app,width=150,height=30)
    P6.grid(row=1, column=1, padx=20, pady=20)
    label7 = customtkinter.CTkLabel(app,text="Ingrese el lugar de residencia de su mascota")
    label7.grid(row=2, column=1, padx=0, pady=20)
    P7 = customtkinter.CTkTextbox(app,width=150,height=30)
    P7.grid(row=3, column=1, padx=20, pady=20)
    label8 = customtkinter.CTkLabel(app,text="Ingrese si su mascota tiene las vacunas")
    label8.grid(row=4, column=1, padx=0, pady=20)
    P8 = customtkinter.CTkOptionMenu(app,width=150,height=30,values=lista_vacunas)
    P8.grid(row=5, column=1, padx=20, pady=20)
    button = customtkinter.CTkButton(app, text="aceptar", command=lambda:oprimir_boton(app,P,P2,P3,P4,P5,P6,P7,P8,DATA))
    button.grid(row=6, column=1, padx=50, pady=0)
    app.mainloop()
def mostrar_mascotas(DATA):
    mascotas = []
    diccionario = fj.leer_json(DATA)
    print("MASCOTAS REGISTRADS")
    for keys in diccionario:
        mascotas.append(diccionario[keys]["nombre"])
    mostrar_mascotas = customtkinter.CTk()
    mostrar_mascotas.title("Nombres de mascotas")
    mostrar_mascotas.geometry("230x200")
    label_nombre = customtkinter.CTkLabel(mostrar_mascotas,text="Elija el nombre de la mascota \nde la cual desea saber sus datos")
    label_nombre.grid(row=0, column=0, padx=20, pady=20)
    seleccion_mascota = customtkinter.CTkOptionMenu(mostrar_mascotas,values=mascotas)
    seleccion_mascota.grid(row=1, column=0, padx=20, pady=20)
    boton_aceptar = customtkinter.CTkButton(mostrar_mascotas,text=("Buscar"),command=lambda:mostrar_mascota_elegida(seleccion_mascota,diccionario,mostrar_mascotas))
    boton_aceptar.grid(row = 2, column =0, padx= 20, pady = 20)
def mostrar_mascota_elegida(mascota,diccionario,menu):
    #menu.destroy()
    mascota = mascota.get()

    print(mascota)