import customtkinter as ctk
from PIL import Image

class registPassword(ctk.CTk):
    def __init__(self, parent):
        super().__init__()
        self.title("banyk's branch in prime yea?")
        self.geometry("800x600")
        self.resizable(False, False)
        self.center_window(800, 600)
        self.parent = parent

        # Флаг для состояния отображения пароля
        self.password_visible = False


        # Настройка сетки
        for i in range(11):
            self.grid_columnconfigure(i, weight=1)
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)

        # Метки
        self.label_password = ctk.CTkLabel(self, text="Пароль", font=("Helvetica", 42, "bold"))
        self.label_password.grid(row=5, column=4, columnspan=3)

        self.label_confirmation = ctk.CTkLabel(self, text="Подтверждение пароля", font=("Helvetica", 42, "bold"))
        self.label_confirmation.grid(row=7, column=4, columnspan=3)

        # Поля ввода
        self.entry_password = ctk.CTkEntry(self, placeholder_text="Введите пароль", font=("Helvetica", 28), width=320, show="*")
        self.entry_password.grid(row=6, column=4, columnspan=2, pady=5, sticky="e")

        self.entry_confirmation = ctk.CTkEntry(self, placeholder_text="Подтвердите пароль", font=("Helvetica", 28), width=320, show="*")
        self.entry_confirmation.grid(row=8, column=4, columnspan=2, pady=5, sticky="e")

        # Кнопки-глазки для переключения видимости паролей
        self.toggle_password_button = ctk.CTkButton(self,  command=self.toggle_password_visibility,
                                                    width=40, height=40, text="", fg_color="white")
        self.toggle_password_button.grid(row=6, column=6, sticky="w", padx=5)

        self.toggle_confirmation_button = ctk.CTkButton(self, command=self.toggle_confirmation_visibility,
                                                        width=40, height=40, text="", fg_color="white")
        self.toggle_confirmation_button.grid(row=8, column=6, sticky="w", padx=5)

        # Кнопка регистрации
        self.button_registration = ctk.CTkButton(self, text="Регистрация", font=("Helvetica", 24, "bold"),
                                                 command=self.button_event, fg_color="#4D4D4D",
                                                 text_color="#FFFFFF", corner_radius=10, width=200, height=50)
        self.button_registration.grid(row=12, column=5, pady=20)

        # Метка для вывода результата
        self.label_result = ctk.CTkLabel(self, text="", font=("Helvetica", 18, "italic"))
        self.label_result.grid(row=15, column=4, columnspan=3, pady=10)

        # Обработка закрытия окна
        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def button_event(self):
        # Логика при нажатии на кнопку
        password = self.entry_password.get()
        confirm_password = self.entry_confirmation.get()
        if password and confirm_password:
            if password == confirm_password:
                self.label_result.configure(text="Регистрация выполнена успешно!", text_color="green")
            else:
                self.label_result.configure(text="Пароли не совпадают!", text_color="red")
        else:
            self.label_result.configure(text="Пожалуйста, заполните оба поля.", text_color="orange")

    def toggle_password_visibility(self):
        # Переключение видимости пароля
        if self.password_visible:
            self.entry_password.configure(show="*")
            self.toggle_password_button.configure(fg_color = "blue")
        else:
            self.entry_password.configure(show="")
            self.toggle_password_button.configure(fg_color = "blue")
        self.password_visible = not self.password_visible

    def toggle_confirmation_visibility(self):
        # Переключение видимости подтверждения пароля
        if self.password_visible:
            self.entry_confirmation

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")