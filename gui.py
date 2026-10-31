import customtkinter as ctk
from calculator import addition, subtraction, multiplication,division
from history import CalculationHistoryManager

class CalculatorApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        #Calculator state

        self.first_number = None
        self.operator = None
        self.current_input = ""

        # Initialize History Manager (Separate from GUI logic)
        self.history_manager = CalculationHistoryManager()

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
        self.display = ctk.CTkLabel(
            self.calculator_frame,
            text="0",
            width=400,
            height=65,
            font=("Arial", 28),
            anchor="e",
            fg_color= ("#F3F3F3", "#343638"),
            corner_radius=8,
            padx=15
        )
        self.display.pack(padx=20, pady=20)

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
                button = ctk.CTkButton(
                    self.buttons_frame,
                    text=button_text,
                    width=85,
                    height=55,
                    font=("Arial", 20),
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
            self.history_manager.record_calculation(expression, result)

            # Display the result
            self.current_input = str(result)
            self.display.configure(text=self.current_input)

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