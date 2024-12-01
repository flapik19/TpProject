import tkinter
import customtkinter

class logOrRegistWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("TpProject")
        self.geometry("800x600")

        for i in range(10):
            self.grid_columnconfigure(i, weight=1)
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)
        self.label = customtkinter.CTkLabel(
            self,
            text="Вы уже зарегистрированы?",
            font=("Helvetica", 28, "bold"),
            text_color="#BCBCBC"
        )
        self.label.grid(row=8, column=4, columnspan=2)
        self.buttonLog = customtkinter.CTkButton(self,
                                                 text="Войти",
                                                 font=("Helvetica", 16, "bold"),
                                                 text_color="#FFFFFF",
                                                 fg_color="#4D4D4D",
                                                 corner_radius=10,
                                                 width=200,
                                                 height=50
                                                 )
        self.buttonRegist = customtkinter.CTkButton(self,
                                                 text="Регистрация",
                                                 font=("Helvetica", 16, "bold"),
                                                 text_color="#FFFFFF",
                                                 fg_color="#4D4D4D",
                                                 corner_radius=10,
                                                 width=200,
                                                 height=50
                                                 )
        self.buttonLog.grid(row=9, column=4)
        self.buttonRegist.grid(row = 9, column = 5)

    def start(self):
        self.mainloop()
