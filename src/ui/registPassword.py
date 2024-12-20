import customtkinter as ctk
from src.ui.chooseRole import ChooseRoleWindow

class registPassword(ctk.CTk):
    def __init__(self, parent):
        super().__init__()
        self.title("Enter Password")
        self.geometry("800x600")
        self.resizable(False, False)
        self.center_window(800, 600)
        self.parent = parent

        self.password_visible = False

        for i in range(11):
            self.grid_columnconfigure(i, weight=1)
        for i in range(20):
            self.grid_rowconfigure(i, weight=1)

        self.label_password = ctk.CTkLabel(self, text="Password", font=("Helvetica", 38, "bold"))
        self.label_password.grid(row=5, column=4, columnspan=3)

        self.entry_password = ctk.CTkEntry(
            self,
            placeholder_text="Enter password",
            font=("Helvetica", 28),
            width=320,
            show="*")
        self.entry_password.grid(row=7, column=4, columnspan=2, pady=5, sticky="e")

        self.toggle_password_button = ctk.CTkButton(self,
                                                    command=self.toggle_password_visibility,
                                                    width=40, height=40, text="👁", fg_color="white")
        self.toggle_password_button.grid(row=7, column=6, sticky="w", padx=5)

        self.button_registration = ctk.CTkButton(self, text="Continue", font=("Helvetica", 22, "bold"),
                                                 command=self.ButtonEvent, fg_color="#4D4D4D",
                                                 text_color="#FFFFFF", corner_radius=10, width=200, height=50)
        self.button_registration.grid(row=13, column=5, pady=20)

        self.label_result = ctk.CTkLabel(self, text="", font=("Helvetica", 18, "italic"))
        self.label_result.grid(row=16, column=4, columnspan=3, pady=10)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def toggle_password_visibility(self):
        if self.password_visible:
            self.entry_password.configure(show="*")
        else:
            self.entry_password.configure(show="")
        self.password_visible = not self.password_visible

    def ButtonEvent(self):
        self.withdraw()
        openRole = ChooseRoleWindow(self)
        openRole.deiconify()

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def on_close(self):
        self.destroy()
        self.quit()
