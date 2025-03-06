import customtkinter
lista = ["si","no"]
def oprimir_boton():
    texto = P.get("0.0","end")
    print(texto)
app = customtkinter.CTk()
app.title("Gestion de mascotas")
app.geometry('250x400')
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
label = customtkinter.CTkLabel(app,text="Ingrese el nombre de su mascota")
label.grid(row=0, column=0, padx=0, pady=0, columnspan=2)
P = customtkinter.CTkProgressBar(app,width=150,height=30)
P.grid(row=1, column=0, padx=20, pady=20, columnspan=2)
button = customtkinter.CTkButton(app, text="aceptar", command=oprimir_boton)
button.grid(row=2, column=0, padx=50, pady=0, columnspan=2)
app.mainloop()