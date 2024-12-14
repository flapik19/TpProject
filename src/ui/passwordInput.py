import customtkinter as ctk
from PIL import Image

class PasswordEntry(ctk.CTk):
    def __init__(self,parent):
        super().__init__()
        self.title("Страница входа")
        self.geometry("800x600")
        self.resizable(False, False)
        self.center_window(800, 600)
        self.parent = parent

        self.password_visible = False

        self.eye_open_icon = ctk.CTkImage(Image.open("eye_open.png"), size=(24, 24))
        self.eye_closed_icon = ctk.CTkImage(Image.open("eye_closed.png"), size=(24, 24))

        # Настройка сетки
        for i in range(11):
            self.grid_columnconfigure(i, weight=1)
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)

        self.label_password = ctk.CTkLabel(self, text="Введите пароль", font=("Helvetica", 42, "bold"))
        self.label_password.grid(row=5, column=4, columnspan=3, pady=20)

        self.entry_password = ctk.CTkEntry(self, placeholder_text="Введите пароль", font=("Helvetica", 28), width=320, show="*")
        self.entry_password.grid(row=6, column=4, columnspan=2, pady=5, sticky="e")

        #для переключения видимости пароля
        self.toggle_password_button = ctk.CTkButton(self, image=self.eye_closed_icon, command=self.toggle_password_visibility,
                                                    width=40, height=40, text="", fg_color="transparent")
        self.toggle_password_button.grid(row=6, column=6, sticky="w", padx=5)

        self.button_login = ctk.CTkButton(self, text="Вход", font=("Helvetica", 24, "bold"),
                                          command=self.login_event, fg_color="#4D4D4D",
                                          text_color="#FFFFFF", corner_radius=10, width=200, height=50)
        self.button_login.grid(row=8, column=5, pady=20)

        self.label_result = ctk.CTkLabel(self, text="", font=("Helvetica", 18, "italic"))
        self.label_result.grid(row=10, column=4, columnspan=3, pady=10)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def login_event(self):
        # Логика при нажатии на кнопку "Вход"
        password = self.entry_password.get()
        if password:
            self.label_result.configure(text="Вход выполнен успешно!", text_color="green")
        else:
            self.label_result.configure(text="Пожалуйста, введите пароль.", text_color="red")

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

# Запуск приложения
if __name__ == "__main__":
    app = PasswordEntry()
    app.mainloop()
