import customtkinter
import modules.Funcion_añadir_mascota as am
def editar_mascota(app):
    app.destroy()
def añadir_mascota(app,DATA):
    app.destroy()
    am.añadir_mascota(DATA)
def eliminar_mascota(app):
    app.destroy()
def buscar_mascota(app):
    app.destroy()
def mostrar_mascota(app,DATA):
    app.destroy()
    am.mostrar_mascotas(DATA)
def salir(app):
    app.destroy()
def menu_principal(DATA):
    app = customtkinter.CTk()
    app.title("Gestion de mascotas")
    app.geometry('250x400')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    button = customtkinter.CTkButton(app, text="1.Añadir mascota", command=lambda:añadir_mascota(app,DATA))
    button.grid(row=1, column=0, padx=50, pady=20, columnspan=2)
    boton_2 = customtkinter.CTkButton(app,text="2.Editar mascota",command=lambda:editar_mascota(app))
    boton_2.grid(row=2,column= 0,padx=50,pady=20, columnspan=2)
    boton_3 = customtkinter.CTkButton(app,text="3.Eliminar mascota",command=lambda:eliminar_mascota(app))
    boton_3.grid(row=3,column= 0,padx=50,pady=20, columnspan=2)
    boton_4 = customtkinter.CTkButton(app,text="4.Buscar mascotas",command=lambda:buscar_mascota(app))
    boton_4.grid(row=4,column= 0,padx=50,pady=20, columnspan=2)
    boton_5 = customtkinter.CTkButton(app,text="5.Mostrar mascotas",command=lambda:mostrar_mascota(app,DATA))
    boton_5.grid(row=5,column= 0,padx=50,pady=20, columnspan=2)
    boton_5 = customtkinter.CTkButton(app,text="9.Salir",command=lambda:salir(app))
    boton_5.grid(row=6,column= 0,padx=50,pady=20, columnspan=2)
    app.mainloop()