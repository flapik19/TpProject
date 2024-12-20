import customtkinter

class ChooseRoleWindow(customtkinter.CTk):
    def __init__(self, parent):
        super().__init__()
        self.title("Choose Role")
        self.geometry("800x600")
        self.resizable(False, False)
        self.center_window(800, 600)
        self.parent = parent

        for i in range(30):
            self.grid_columnconfigure(i, weight=1)
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)

        self.label = customtkinter.CTkLabel(
            self,
            text="Choose Role",
            font=("Helvetica", 38, "bold"),
            text_color="#BCBCBC"
        )
        self.label.grid(row=7, column=14)

        self.role_var = customtkinter.StringVar(value="None")

        self.radio_student = customtkinter.CTkRadioButton(
            self,
            text="Student",
            font = ("Helvetica", 28, "bold"),
            variable=self.role_var,
            value="Student"
        )
        self.radio_student.grid(row=8, column=14)

        self.radio_directorate = customtkinter.CTkRadioButton(
            self,
            text="Directorate",
            font = ("Helvetica", 28, "bold"),
            variable=self.role_var,
            value="Directorate"
        )
        self.radio_directorate.grid(row=9, column=14)

        self.radio_teacher = customtkinter.CTkRadioButton(
            self,
            text="Teacher",
            font = ("Helvetica", 28, "bold"),
            variable=self.role_var,
            value="Teacher"
        )
        self.radio_teacher.grid(row=10, column=14)

        self.confirm_button = customtkinter.CTkButton(
            self,
            text="Confirm Selection",
            width=200,
            height=50,
            corner_radius=10,
            font = ("Helvetica", 22, "bold"),
            command=self.confirm_selection
        )
        self.confirm_button.grid(row=11, column=14)

    def confirm_selection(self):
        selected_role = self.role_var.get()
        print(f"Selected role: {selected_role}")
        self.destroy()

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def on_close(self):
        self.destroy()
        self.quit()
