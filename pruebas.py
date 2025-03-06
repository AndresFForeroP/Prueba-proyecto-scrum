import customtkinter
import time

def oprimirboton(app):
    print("boton oprimido")
    app.destroy()
    time.sleep(2)
    menu_principal()
    
def menu_principal():
    app = customtkinter.CTk()
    app.title("Gestion de mascotas")
    app.geometry('250x400')
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")
    button = customtkinter.CTkButton(app, text="1.Editar mascota", command=lambda:oprimirboton(app))
    button.grid(row=1, column=0, padx=50, pady=20, columnspan=2)
    boton_2 = customtkinter.CTkButton(app,text="2.Añadir mascota",command=lambda:oprimirboton(app))
    boton_2.grid(row=2,column= 0,padx=50,pady=20, columnspan=2)
    boton_3 = customtkinter.CTkButton(app,text="3.Eliminar mascota",command=lambda:oprimirboton(app))
    boton_3.grid(row=3,column= 0,padx=50,pady=20, columnspan=2)
    boton_4 = customtkinter.CTkButton(app,text="4.Buscar mascotas",command=lambda:oprimirboton(app))
    boton_4.grid(row=4,column= 0,padx=50,pady=20, columnspan=2)
    boton_5 = customtkinter.CTkButton(app,text="5.Mostrar mascotas",command=lambda:oprimirboton(app))
    boton_5.grid(row=5,column= 0,padx=50,pady=20, columnspan=2)
    boton_5 = customtkinter.CTkButton(app,text="9.Salir",command=lambda:oprimirboton(app))
    boton_5.grid(row=6,column= 0,padx=50,pady=20, columnspan=2)
    app.mainloop()
menu_principal()
