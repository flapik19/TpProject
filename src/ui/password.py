import customtkinter as ctk
import tkinter

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("400x240")
app.title("banyk's branch in prime yea?")

label_password = ctk.CTkLabel(app, text="Пароль", fg_color="transparent")
label_password.place(relx=0.2, rely=0.1, anchor=ctk.CENTER)
label_surname = ctk.CTkLabel(app, text="Пароль", fg_color="transparent")
label_surname.place(relx=0.2, rely=0.3, anchor=ctk.CENTER)

entry_name = ctk.CTkEntry(app, placeholder_text="Введите пароль")
entry_name.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)
entry_surname = ctk.CTkEntry(app, placeholder_text="Подтвердите пароль")
entry_surname.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

label_result = ctk.CTkLabel(app, text="turtle", fg_color="transparent")
label_result.place(relx=0.5, rely=0.87, anchor=ctk.CENTER)

def button_event():
    label_result.configure(text=f"NAME : {entry_name.get()}\n SURNAME: {entry_surname.get()}")
button = ctk.CTkButton(app, text="Generate", command=button_event)
button.place(relx=0.5, rely=0.68, anchor=ctk.CENTER)

app.mainloop()