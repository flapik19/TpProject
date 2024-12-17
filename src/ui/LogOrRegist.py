import tkinter
import customtkinter
from src.ui.logInput import logInput
from src.ui.RegisterLoginInput import RegisterLoginInput

class logOrRegistWindow(customtkinter.CTk):
    def __init__(self, parent):
        super().__init__()
        self.title("TpProject")
        self.geometry("800x600")
        self.resizable(False,False)
        self.center_window(800, 600)
        self.parent = parent
        self.withdraw()

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

        self.buttonLog = customtkinter.CTkButton(
            self,
            text="Войти",
            font=("Helvetica", 16, "bold"),
            text_color="#FFFFFF",
            fg_color="#4D4D4D",
            corner_radius=10,
            width=200,
            height=50,
            command=self.openLogInput
        )
        self.buttonLog.grid(row=9, column=4)

        self.buttonRegist = customtkinter.CTkButton(
            self,
            text="Регистрация",
            font=("Helvetica", 16, "bold"),
            text_color="#FFFFFF",
            fg_color="#4D4D4D",
            corner_radius=10,
            width=200,
            height=50,
            command = self.openRegisterInput
        )
        self.buttonRegist.grid(row=9, column=5)

        self.protocol("WM_DELETE_WINDOW", self.on_close)


    def openLogInput(self):
        self.withdraw()
        login = logInput(self)
        login.deiconify()

    def openRegisterInput(self):
        self.withdraw()
        regist = RegisterLoginInput(self)
        regist.deiconify()

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def on_close(self):
        self.destroy()
        self.quit()