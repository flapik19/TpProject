import customtkinter
import json

class ChooseRoleWindow(customtkinter.CTk):
    def __init__(self, parent):
        super().__init__()
        self.title("Страница выбора роли")
        self.geometry("800x600")
        self.resizable(False, False)
        self.center_window(800, 600)
        self.parent = parent

        # Конфигурация сетки
        for i in range(30):
            self.grid_columnconfigure(i, weight=1)
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)

        # Заголовок
        self.label = customtkinter.CTkLabel(
            self,
            text="Choose Role",
            font=("Helvetica", 28, "bold"),
            text_color="#BCBCBC"
        )
        self.label.grid(row=7, column=14)

        # Переменная для радиокнопок
        self.role_var = customtkinter.StringVar(value="None")

        # Радиокнопка "Student"
        self.radio_student = customtkinter.CTkRadioButton(
            self,
            text="Student",
            variable=self.role_var,
            value="Student"
        )
        self.radio_student.grid(row=8, column=14)

        # Радиокнопка "Directorate"
        self.radio_directorate = customtkinter.CTkRadioButton(
            self,
            text="Directorate",
            variable=self.role_var,
            value="Directorate"
        )
        self.radio_directorate.grid(row=9, column=14)

        # Радиокнопка "Teacher"
        self.radio_teacher = customtkinter.CTkRadioButton(
            self,
            text="Teacher",
            variable=self.role_var,
            value="Teacher"
        )
        self.radio_teacher.grid(row=10, column=14)

        # Кнопка для подтверждения выбора
        self.confirm_button = customtkinter.CTkButton(
            self,
            text="Confirm Selection",
            command=self.confirm_selection
        )
        self.confirm_button.grid(row=11, column=14)

    def confirm_selection(self):
        selected_role = self.role_var.get()
        print(f"Selected role: {selected_role}")
        # Здесь вы можете добавить дальнейшую логику, например, переход к следующему экрану

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def on_close(self):
        self.destroy()
        self.quit()

# Пример вызова окна
if __name__ == "__main__":
    app = ChooseRoleWindow(None)
    app.mainloop()
