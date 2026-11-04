import customtkinter as ctk
from PIL import Image
from pathlib import Path
from calculator import addition, subtraction, multiplication,division, format_result
from history import CalculationHistoryManager


#UGM_Manchester colour palette

COLORS = {
    "primary": "#1D263B",
    "operator": "#254F83",
    "accent": "#16A6C9",
    "background": "#F4F6FA",
    "white": "#FFFFFF",
    "text":"#1D263B",
    "number": "#E8EDF4",
    "action": "#DCE4EF",
}




class CalculatorApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.configure(fg_color=COLORS["background"])

        #Calculator state

        self.first_number = None
        self.operator = None
        self.current_input = ""

        # Initialize History Manager (Separate from GUI logic)
        self.history_manager = CalculationHistoryManager()

        #Window configuration
        self.title("UGM Calculator")
        self.geometry("1100x650")
        self.minsize (1050,600)

        #Main layout
        self.grid_columnconfigure(0, weight=3)
        self.grid_rowconfigure(0,weight=2)
        self.grid_rowconfigure(0, weight=1)


        #calculator frame
        self.calculator_frame =ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color=COLORS["white"]
        )
        self.calculator_frame.grid(
            row=0,
            column=0,
            padx=30,
            pady=30,
            sticky="nsew"
        )

        # University crest
        logo_path = (
            Path(__file__).resolve().parent
            / "assets"
            / "images"
            / "ugm-logo.png"
        )

        logo_image = Image.open(logo_path)

        logo_width = 45
        logo_height = round(
            logo_width * logo_image.height / logo_image.width
        )

        self.ugm_logo = ctk.CTkImage(
            light_image=logo_image,
            dark_image=logo_image,
            size=(logo_width, logo_height)
        )

        # Application header
        self.header_frame = ctk.CTkFrame(
            self.calculator_frame,
            fg_color="transparent"
        )
        self.header_frame.pack(pady=(20, 10))

        # University crest
        self.logo_label = ctk.CTkLabel(
            self.header_frame,
            image=self.ugm_logo,
            text=""
        )
        self.logo_label.pack(side="left", padx=(0, 12))

        # Application title
        self.title_label = ctk.CTkLabel(
        self.header_frame,
        text="UGM Calculator",
        font=("Arial", 28, "bold"),
        text_color=COLORS["primary"]
        )
        self.title_label.pack(side="left")

        #Calculator display
        self.display = ctk.CTkLabel(
            self.calculator_frame,
            text="0",
            width=380,
            height=65,
            font=("Arial", 28),
            anchor="e",
            fg_color=COLORS ["primary"],
            text_color=COLORS["white"],
            corner_radius=10,
            padx=20
        )
        self.display.pack(
            padx=20, 
            pady=(10,15)
        )

        # Caculator buttons frame
        self.buttons_frame = ctk.CTkFrame(
            self.calculator_frame,
            fg_color="transparent"
        )
        self.buttons_frame.pack(padx=20, pady=15)

        # Button layout
        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"]
        ]

        # Create buttons
        for row_index, row in enumerate(buttons):
            for col_index, button_text in enumerate(row):

                # Choose button colours
                if button_text == "=":
                    button_color = COLORS["accent"]
                    text_color = COLORS["white"]

                elif button_text in ("+", "-", "×", "÷"):
                    button_color = COLORS["operator"]
                    text_color = COLORS["white"]

                elif button_text in ("C", "⌫", "(", ")"):
                    button_color = COLORS["action"]
                    text_color = COLORS["text"]

                else:
                    button_color = COLORS["number"]
                    text_color = COLORS["text"]

                button = ctk.CTkButton(
                    self.buttons_frame,
                    text=button_text,
                    width=85,
                    height=55,
                    font=("Arial", 20),
                    fg_color=button_color,
                    text_color=text_color,
                    hover_color=COLORS["accent"],
                    corner_radius=10,
                    command=(
                        lambda value=button_text: self.on_number_click(value)
                    ) if button_text in "0123456789." 
                    else (
                        (lambda value=button_text: self.on_operator_click(value))
                        if button_text in "+-×÷"
                        else self.on_equals_click
                        if button_text == "="
                        else self.on_clear_click
                        if button_text == "C"
                        else self.on_backspace_click
                        if button_text == "⌫"
                        else None
                    )
                )

                button.grid(
                    row=row_index,
                    column=col_index,
                    padx=5,
                    pady=5
                )

        # History panel
        self.history_frame = ctk.CTkFrame (
        self,
        corner_radius= 15,
        fg_color=COLORS["white"]    
        )

        self.history_frame.grid(
            row=0,
            column=1,
            padx=(0,30),
            pady=30,
            sticky= "nsew"
        )

        #History title
        self.history_title = ctk.CTkLabel(
            self.history_frame,
            text="Calculation History",
            font= ("Arial", 22, "bold"),
            text_color=COLORS["primary"]
        )

        self.history_title.pack(pady=(20,10))

        #scrollable history area

        self.history_list = ctk.CTkScrollableFrame(
            self.history_frame,
            width=250,
            height=350,
            fg_color=COLORS["background"],
            corner_radius=10
        )

        self.history_list.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # Clear history button
        self.clear_history_button = ctk.CTkButton(
            self.history_frame,
            text="Clear Hisoty",
            width=180,
            height=40,
            font=("Arial",15),
            command=self.on_clear_history_click
        )

        self.clear_history_button.pack(
            padx=15,
            pady=(5,20)
        )

    def on_number_click(self,number):
        # Prevent multiple decimal points
        if number == "." and "." in self.current_input:
            return

        # Add zero before a leading decimal point
        if number == "." and not self.current_input:
            self.current_input = "0"

        # Add the selected number
        self.current_input += str(number)

        # Update the display
        self.display.configure(text=self.current_input)

    def on_operator_click(self,operator):
        #Check if the user entered a number
        if not self.current_input:
            return

        #Save the first number
        self.first_number = float(self.current_input)

        #Save the selected operator
        self.operator = operator

        # Clear input for the second number
        self.current_input =""

        # Show the selected operator
        self.display.configure(text=operator)

    def on_equals_click(self):
        #Check that both numbers and an operator exists
        if self.first_number is None or not self.current_input or not self.operator:
            return

        second_number = float(self.current_input)
        expression = f"{self.first_number} {self.operator} {second_number}"

        try:
            if self.operator == "+":
                result = addition(self.first_number, second_number)
            elif self.operator == "-":
                result = subtraction(self.first_number, second_number)
            elif self.operator == "×":
                result = multiplication(self.first_number, second_number)
            elif self.operator == "÷":
                result = division(self.first_number, second_number)
            else:
                return

            # Record calculation in history manager (Chronological order + Validation)
            if self.history_manager.record_calculation(expression, result):
                self.update_history_display()

            # Display the result - precision internally but showing one decimal place
            self.current_input = str(result)
            self.display.configure(text=format_result(result))

        except ValueError as error:
            self.display.configure(text=str(error))
            self.current_input = ""

        # Reset the operation
        self.first_number = None
        self.operator = None

    def on_clear_click(self):
        
        self.first_number = None
        self.operator = None
        self.current_input = ""
        self.display.configure(text="0")

    def on_backspace_click(self):
        if self.current_input:
            self.current_input = self.current_input[:-1]
            # Update display or fallback to "0" if input is empty
            display_text = self.current_input if self.current_input else "0"
            self.display.configure(text=display_text)

    def update_history_display(self):
        #Remove existing history items
        for widget in self.history_list.winfo_children():
            widget.destroy()

        #retrieve saved calculations 
        history = self.history_manager.retrieve_history()

        #Display newest calculations first
        for record in reversed(history):
            expression = record ["expression"]
            result = record ["result"]

            history_item=ctk.CTkLabel(
                self.history_list,
                text=f"{expression}={format_result(result)}",
                font=("Arial",15),
                text_color=COLORS["text"],
                anchor="w",
                wraplength=230
            )

            history_item.pack(
                fill="x",
                padx=10,
                pady=5
            )

    def on_clear_history_click(self):
        #Remove all saved calculations
        self.history_manager.clear_history()

        #Refresh the history panel
        self.update_history_display()