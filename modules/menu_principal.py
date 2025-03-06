import customtkinter
def oprimir_boton():
    menuP.destroy()
def editar_mascota():
    pass
def añadir_mascota():
    pass 
def eliminar_mascota():
    pass 
def buscar_mascota():
    pass
def mostrar_mascota():
    pass
def salir():
    pass
menuP = customtkinter.CTk()
menuP.title("Gestion de mascotas")
menuP.geometry("250x400")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
button = customtkinter.CTkButton(menuP, text="Editar mascota", command=editar_mascota)
button.grid(row=1, column=0, padx=50, pady=20, columnspan=2)
boton_2 = customtkinter.CTkButton(menuP,text="Añadir mascota",command=añadir_mascota)
boton_2.grid(row=2,column= 0,padx=50,pady=20, columnspan=2)
boton_3 = customtkinter.CTkButton(menuP,text="Eliminar mascota",command=eliminar_mascota)
boton_3.grid(row=3,column= 0,padx=50,pady=20, columnspan=2)
boton_4 = customtkinter.CTkButton(menuP,text="Buscar mascotas",command=buscar_mascota)
boton_4.grid(row=4,column= 0,padx=50,pady=20, columnspan=2)
boton_5 = customtkinter.CTkButton(menuP,text="Mostrar mascotas",command=mostrar_mascota)
boton_5.grid(row=5,column= 0,padx=50,pady=20, columnspan=2)
boton_5 = customtkinter.CTkButton(menuP,text="Salir",command=salir())
boton_5.grid(row=6,column= 0,padx=50,pady=20, columnspan=2)
menuP.mainloop()