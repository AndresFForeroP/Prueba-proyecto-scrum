import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
boton = False
def oprimir_boton():
    boton = True

def menu_principal():
    menuP = customtkinter.CTk()
    menuP.title("Gestion de mascotas")
    menuP.geometry("250x400")
    button = customtkinter.CTkButton(menuP, text="Editar mascota", command=oprimir_boton)
    button.grid(row=1, column=0, padx=50, pady=20, columnspan=2)
    boton_2 = customtkinter.CTkButton(menuP,text="Añadir mascota",command=oprimir_boton)
    boton_2.grid(row=2,column= 0,padx=50,pady=20, columnspan=2)
    boton_3 = customtkinter.CTkButton(menuP,text="Eliminar mascota",command=oprimir_boton)
    boton_3.grid(row=3,column= 0,padx=50,pady=20, columnspan=2)
    boton_4 = customtkinter.CTkButton(menuP,text="Buscar mascotas",command=oprimir_boton)
    boton_4.grid(row=4,column= 0,padx=50,pady=20, columnspan=2)
    boton_5 = customtkinter.CTkButton(menuP,text="Mostrar mascotas",command=oprimir_boton)
    boton_5.grid(row=5,column= 0,padx=50,pady=20, columnspan=2)
    boton_5 = customtkinter.CTkButton(menuP,text="Salir",command=oprimir_boton)
    boton_5.grid(row=6,column= 0,padx=50,pady=20, columnspan=2)
    menuP.mainloop()
menu_principal()
print (boton)
if boton == True:
    print("oprimido")