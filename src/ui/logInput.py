import customtkinter
from src.ui.passwordInput import PasswordEntry

class logInput(customtkinter.CTk):
    def __init__(self,parent):
        super().__init__()
        self.title("TpProject")
        self.geometry("800x600")
        self.parent = parent
        self.resizable(False, False)
        self.center_window(800, 600)
        for i in range(11):
            self.grid_columnconfigure(i, weight=1)
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.labelLog = customtkinter.CTkLabel(self,
                                               text = "Введите логин",
                                               font=("Helvetica", 42, "bold"),
                                               text_color="#FFFFFF"
                                               )
        self.labelLog.grid(row = 6, column = 5)
        self.entry = customtkinter.CTkEntry(self,
                                            placeholder_text="Type...",
                                            width=320,
                                            font=("Helvetica", 28, "bold"),
                                            text_color="#FFFFFF")
        self.entry.grid(row=7, column=5)

        self.buttonContinue = customtkinter.CTkButton(self,
                                                        text="Continue",
                                                        font=("Helvetica", 24, "bold"),
                                                        text_color="#FFFFFF",
                                                        fg_color="#4D4D4D",
                                                        corner_radius=10,
                                                        width=200,
                                                        height=50,
                                                        command=openpassword)
        self.buttonContinue.grid(row = 15, column = 5)
    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def openpassword(self):
        self.withdraw()
        openPas = PasswordEntry(self)
        openPas.deiconify()

    def on_close(self):
        self.destroy()
        self.quit()