import customtkinter as ctk
from src.mainPage import MainPage

class loginPassword(ctk.CTk):
    def __init__(self,parent):
        super().__init__()  
        self.title("Страница входа")
        self.geometry("800x600")
        self.resizable(False, False)
        self.center_window(800, 600)
        self.parent = parent

        self.password_visible = False

        # Настройка сетки
        for i in range(30):
            self.grid_columnconfigure(i, weight=1)
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)

        # Метка "Введите пароль"
        self.label_password = ctk.CTkLabel(self, text="Enter password",
                                            font=("Helvetica", 38, "bold"))
        self.label_password.grid(row=5, column=15)

        # Поле для ввода пароля
        self.entry_password = ctk.CTkEntry(self, placeholder_text="Enter password", font=("Helvetica", 28), width=240, show="*")
        self.entry_password.grid(row=6, column=15)

        # Кнопка-глаз для переключения видимости пароля
        self.toggle_password_button = ctk.CTkButton(self,  command=self.toggle_password_visibility,
                                                    width=40, height=40, text="", fg_color="white")
        self.toggle_password_button.grid(row=7, column=15)

        # Кнопка "Вход"
        self.button_login = ctk.CTkButton(self, text="Log in", font=("Helvetica", 22, "bold"),
                                          command=self.login_event, fg_color="#4D4D4D",
                                          text_color="#FFFFFF", corner_radius=10, width=200, height=50)
        self.button_login.grid(row=8, column=15)


        # Обработка закрытия окна
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def login_event(self):
        self.withdraw()
        openMain = MainPage(self)
        openMain.deiconify()

    def toggle_password_visibility(self):
        if self.password_visible:
            self.entry_password.configure(show="*")
            self.toggle_password_button.configure(image=self.eye_closed_icon)
        else:
            self.entry_password.configure(show="")
            self.toggle_password_button.configure(image=self.eye_open_icon)
        self.password_visible = not self.password_visible

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def on_close(self):
        self.destroy()
        self.quit()
