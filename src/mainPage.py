import customtkinter as ctk
from tkinter import StringVar, IntVar, messagebox

class MainPage(ctk.CTk):
    def __init__(self, user_role):
        super().__init__()

        self.title("Основная страница")
        self.geometry("800x600")
        self.resizable(False, False)
        self.center_window(800, 600)

        self.user_role = user_role  # 'teacher', 'student', 'director'
        self.tasks = [
            {"name": "Сдать лабораторную 1", "completed": False},
            {"name": "Прочитать лекцию по Python", "completed": True},
        ]

        self.init_ui()

    def init_ui(self):
        # Настройка фона окна
        self.configure(bg_color="#4a90e2")  # Голубой фон, как у вас был ранее

        # Заголовок
        self.label_title = ctk.CTkLabel(
            self, text="Список задач", font=("Helvetica", 36, "bold"), text_color="white"
        )
        self.label_title.pack(pady=20)

        # Поле задач в виде таблицы
        self.task_frame = ctk.CTkFrame(self, bg_color="#f5f5f5")
        self.task_frame.pack(pady=10, padx=10, fill="both", expand=True)

        # Заголовки таблицы
        self.render_table_headers()

        # Рендерим задачи по ролям
        if self.user_role == "teacher":
            self.create_teacher_view()
        elif self.user_role == "student":
            self.create_student_view()
        elif self.user_role == "director":
            self.create_director_view()
        else:
            messagebox.showerror("Ошибка", "Неизвестная роль пользователя!")

        # Кнопка выхода
        self.button_exit = ctk.CTkButton(self, text="Выход", command=self.on_close, fg_color="#4a90e2", hover_color="#357ab7")
        self.button_exit.pack(pady=10)


    def add_table_border(self, row, col):
        border = ctk.CTkFrame(self.task_frame, fg_color="#4a90e2", height=1)
        border.grid(row=row + 1, column=col, sticky="we", padx=1, pady=1)

    def create_teacher_view(self):
        # Поле для ввода новой задачи
        self.new_task_var = StringVar()
        self.entry_new_task = ctk.CTkEntry(self, placeholder_text="Введите новую задачу", textvariable=self.new_task_var, fg_color="#ffffff")
        self.entry_new_task.pack(pady=10)

        self.button_add_task = ctk.CTkButton(self, text="Добавить задачу", command=self.add_task, fg_color="#4a90e2", hover_color="#357ab7")
        self.button_add_task.pack(pady=5)

        # Рендер таблицы
        self.render_task_table()

    def render_table_headers(self):
        blue_color = "#357ab7"  # Голубой цвет для заголовков

        # Заголовок "№"
        header_number = ctk.CTkLabel(
            self.task_frame,
            text="№",
            font=("Helvetica", 16, "bold"),
            text_color="white",
            fg_color=blue_color
        )
        header_number.grid(row=0, column=0, sticky="nsew", padx=1, pady=1, ipady=5)

        # Заголовок "Описание задачи"
        header_name = ctk.CTkLabel(
            self.task_frame,
            text="Описание задачи",
            font=("Helvetica", 16, "bold"),
            text_color="white",
            fg_color=blue_color
        )
        header_name.grid(row=0, column=1, sticky="nsew", padx=1, pady=1, ipady=5)

        # Заголовок "Статус"
        header_status = ctk.CTkLabel(
            self.task_frame,
            text="Статус",
            font=("Helvetica", 16, "bold"),
            text_color="white",
            fg_color=blue_color
        )
        header_status.grid(row=0, column=2, sticky="nsew", padx=1, pady=1, ipady=5)

        # Настраиваем веса колонок
        self.task_frame.grid_columnconfigure(0, weight=1)
        self.task_frame.grid_columnconfigure(1, weight=3)
        self.task_frame.grid_columnconfigure(2, weight=2)


    def render_task_table(self, editable=False):
    # Очистка фрейма от предыдущих задач
        for widget in self.task_frame.winfo_children():
            if widget.grid_info()["row"] > 0:  # Удаляем всё кроме заголовков
                widget.destroy()

        light_gray = "#303030"  # Светло-серый цвет
        blue_color = "#357ab7"  # Голубой цвет для заголовков

        # Заполнение таблицы задачами
        for idx, task in enumerate(self.tasks, start=1):
            # Номер задачи
            task_number = ctk.CTkLabel(
                self.task_frame,
                text=str(idx),
                font=("Helvetica", 16),
                text_color="white",
                fg_color=light_gray,  # Светло-серый фон
                corner_radius=0
            )
            task_number.grid(row=idx, column=0, sticky="nsew", padx=1, pady=1, ipady=5)

            # Описание задачи
            task_name = ctk.CTkLabel(
                self.task_frame,
                text=task["name"],
                font=("Helvetica", 16),
                text_color="white",
                fg_color=light_gray  # Светло-серый фон
            )
            task_name.grid(row=idx, column=1, sticky="nsew", padx=1, pady=1, ipady=5)

            # Статус задачи
            if editable:
                status_var = IntVar(value=1 if task["completed"] else 0)
                status_checkbox = ctk.CTkCheckBox(
                    self.task_frame,
                    text="Выполнено",
                    variable=status_var,
                    command=lambda i=idx-1, v=status_var: self.mark_task_complete(i, v),
                    text_color="white",
                    fg_color=light_gray
                )
                status_checkbox.grid(row=idx, column=2, sticky="nsew", padx=1, pady=1, ipady=5)
            else:
                status_text = "Выполнено" if task["completed"] else "Не выполнено"
                task_status = ctk.CTkLabel(
                    self.task_frame,
                    text=status_text,
                    font=("Helvetica", 16),
                    text_color="white",
                    fg_color=light_gray  # Светло-серый фон
                )
                task_status.grid(row=idx, column=2, sticky="nsew", padx=1, pady=1, ipady=5)

        # Настраиваем веса колонок для растяжения
        self.task_frame.grid_columnconfigure(0, weight=1)
        self.task_frame.grid_columnconfigure(1, weight=3)
        self.task_frame.grid_columnconfigure(2, weight=2)




    def create_student_view(self):
        self.render_task_table(editable=True)

    def create_director_view(self):
        self.render_task_table()

    def add_task(self):
        new_task = self.new_task_var.get().strip()
        if new_task:
            self.tasks.append({"name": new_task, "completed": False})
            self.new_task_var.set("")
            self.render_task_table()
        else:
            messagebox.showwarning("Ошибка", "Задача не может быть пустой!")

    def mark_task_complete(self, index, var):
        self.tasks[index]["completed"] = bool(var.get())

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
    role = "director"  # роль student, teacher, director
    app = MainPage(role)
    app.mainloop()
