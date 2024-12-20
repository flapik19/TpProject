import customtkinter
from src.LogOrRegist import logOrRegistWindow

class startWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("TpProject")
        self.geometry("800x600")
        self.resizable(False, False)
        self.center_window(800, 600)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        self.button = customtkinter.CTkButton(
            self,
            text="Tap To Start",
            text_color="#BCBCBC",
            fg_color="#4D4D4D",
            font=("Helvetica", 38, "bold"),
            border_spacing=15,
            corner_radius=50,
            command=self.open_log_or_regist_window
        )
        self.button.grid(row=1, column=1)

        self.protocol("WM_DELETE_WINDOW", self.on_close)

    def center_window(self, width, height):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def open_log_or_regist_window(self):
        self.withdraw()
        log_or_regist = logOrRegistWindow(self)
        log_or_regist.deiconify()

    def on_close(self):
        self.destroy()
        self.quit()
