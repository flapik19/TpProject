import tkinter
import customtkinter

class mainWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("TpProject")
        self.geometry("800x600")
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.button = customtkinter.CTkButton(self,
                                                text = "Tap To Start",
                                                text_color="#BCBCBC",
                                                fg_color="#4D4D4D",
                                                font=("Arial", 28, "bold"),
                                                border_spacing=15,
                                                corner_radius=50)
        self.button.grid(row = 1, column = 1)
    
    
    def start(self):
        self.mainloop()
