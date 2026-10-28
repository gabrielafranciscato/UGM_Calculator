import customtkinter as ctk

class CalculatorApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        #Window configuration
        self.title("UGM Calculator")
        self.geometry("900x600")
        self.minsize (700,500)

        #Main layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0,weight=1)

        #calculator frame
        self.calculator_frame =ctk.CTkFrame(
            self,
            corner_radius=15
        )
        self.calculator_frame.grid(
            row=0,
            column=0,
            padx=30,
            pady=30,
            sticky="nsew"
        )

        #Application title
        self.title_label = ctk.CTkLabel(
            self.calculator_frame,
            text="UGM_Calculator",
            font=("Arial",28, "bold")
        )
        self.title_label.pack(pady=(25,15))

        #Calculator display
        self.display = ctk.CTkEntry(
            self.calculator_frame,
            width=400,
            height=65,
            font=("Arial", 28),
            justify = "right",
            placeholder_text="0"
        )
        self.display.pack(padx=20, pady=20)