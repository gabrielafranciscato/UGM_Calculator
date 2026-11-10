import customtkinter as ctk
from PIL import Image
from pathlib import Path
from calculator import evaluate_expression, format_result
from history import CalculationHistoryManager

# UGM_Manchester colour palette

# UGM Manchester - Navy Blue Theme

COLORS = {
    "primary": "#07162F",
    "operator": "#254F83",
    "accent": "#6FA8E8",
    "background": "#07162F",
    "white": "#FFFFFF",
    "text": "#FFFFFF",
    "number": "#17385F",
    "action": "#10294B",
}


class CalculatorApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.configure(fg_color=COLORS["background"])

        # Calculator state

        self.first_number = None
        self.operator = None
        self.current_input = ""
        self.just_calculated = False

        # Initialize History Manager (Separate from GUI logic)
        self.history_manager = CalculationHistoryManager()

        # Window configuration
        self.title("UGM Calculator")
        self.geometry("1100x650")
        self.minsize(1050, 600)

        # Main layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=3)
        self.grid_columnconfigure(2, weight=2)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = ctk.CTkFrame(
            self, width=180, corner_radius=15, fg_color="#07162F"
        )
        self.sidebar.grid(row=0, column=0, padx=(20, 10), pady=30, sticky="nsew")
        self.sidebar.grid_propagate(False)

        # Sidebar title
        self.sidebar_title = ctk.CTkLabel(
            self.sidebar, text="U G M", font=("Arial", 26, "bold"), text_color="#6FA8E8"
        )
        self.sidebar_title.pack(pady=(35, 40))

       
        # Sidebar navigation buttons
        sidebar_items = [
            ("▦", "Calculator"),
            ("◷", "History"),
            ("?", "Help"),
            ("ⓘ", "About")
        ]

        self.sidebar_buttons = {}

        for icon, item in sidebar_items:
            is_active = item == "Calculator"

            sidebar_button = ctk.CTkButton(
                self.sidebar,
                text=f"{icon}   {item}",
                width=145,
                height=44,
                fg_color="#254F83" if is_active else "transparent",
                hover_color="#17385F",
                text_color="#FFFFFF",
                font=("Arial", 14, "bold" if is_active else "normal"),
                anchor="w",
                corner_radius=10,
                border_width=1 if is_active else 0,
                border_color="#6FA8E8",
                command=lambda section=item: self.show_section(section)
            )
            sidebar_button.pack(padx=15, pady=8)
            self.sidebar_buttons[item] = sidebar_button

         # Help panel
        self.help_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color=COLORS["action"]
        )
        # History panel
        self.history_frame = ctk.CTkFrame(
            self, corner_radius=15, fg_color=COLORS["action"]
        )
        self.history_frame.grid(row=0, column=2, padx=(0, 30), pady=30, sticky="nsew")


        # Help title
        self.help_title = ctk.CTkLabel(
            self.help_frame,
            text="Help Center",
            font=("Arial", 26, "bold"),
            text_color="#FFFFFF"
        )
        self.help_title.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(30, 10)
        )

        # Help description
        self.help_description = ctk.CTkLabel(
            self.help_frame,
            text="Learn how to use your UGM Calculator",
            font=("Arial", 14),
            text_color="#B8CCE5"
        )
        self.help_description.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(0, 25)
        )

        # Help instructions
        help_items = [
            ("+", "Addition"),
            ("−", "Subtraction"),
            ("×", "Multiplication"),
            ("÷", "Division"),
            ("C", "Clear all inputs"),
            ("⌫", "Delete last digit"),
            ("( )", "Group calculations"),
            ("=", "Calculate result")
        ]

        for index, (symbol, description) in enumerate(help_items):
            row = index // 2
            column = index % 2

            help_item = ctk.CTkFrame(
                self.help_frame,
                fg_color="#17385F",
                corner_radius=10
            )
            help_item.grid(
                row=row + 2,
                column=column,
                padx=15,
                pady=8,
                sticky="nsew"
            )

            ctk.CTkLabel(
                help_item,
                text=symbol,
                font=("Arial", 20, "bold"),
                text_color="#6FA8E8"
            ).pack(pady=(10, 3))

            ctk.CTkLabel(
                help_item,
                text=description,
                font=("Arial", 12),
                text_color="#FFFFFF"
            ).pack(pady=(0, 10))

        self.help_frame.grid_columnconfigure((0, 1), weight=1)
                # About panel
        self.about_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color=COLORS["action"]
        )

        # About title
        self.about_title = ctk.CTkLabel(
            self.about_frame,
            text="About UGM Calculator",
            font=("Arial", 26, "bold"),
            text_color="#FFFFFF"
        )
        self.about_title.pack(pady=(40, 20))

        # About description
        self.about_description = ctk.CTkLabel(
            self.about_frame,
            text="A simple and user-friendly calculator application.",
            font=("Arial", 15),
            text_color="#B8CCE5"
        )
        self.about_description.pack(pady=10)

        # Project information
        self.about_information = ctk.CTkLabel(
            self.about_frame,
            text="Developed as part of a Computing Programming project at the University of Greater Manchester.",
            font=("Arial", 14),
            text_color="#FFFFFF"
        )
        self.about_information.pack(pady=10)
                


        # University crest
        logo_path = (
            Path(__file__).resolve().parent / "assets" / "images" / "ugm-logo.png"
        )

        logo_image = Image.open(logo_path)

        logo_width = 45
        logo_height = round(logo_width * logo_image.height / logo_image.width)

        self.ugm_logo = ctk.CTkImage(
            light_image=logo_image,
            dark_image=logo_image,
            size=(logo_width, logo_height),
        )
                # University logo in About
        self.about_logo_image = ctk.CTkImage(
            light_image=logo_image,
            dark_image=logo_image,
            size=(135, round(135 * logo_image.height / logo_image.width))
        )

        self.about_logo = ctk.CTkLabel(
            self.about_frame,
            image=self.about_logo_image,
            text=""
        )
        self.about_logo.pack(pady=(25, 10))
        # Calculator frame
        self.calculator_frame = ctk.CTkFrame(
            self,
            corner_radius=15,
            fg_color=COLORS["action"]
        )
        self.calculator_frame.grid(
            row=0,
            column=1,
            padx=15,
            pady=30,
            sticky="nsew"
        )
        # Application header
        self.header_frame = ctk.CTkFrame(self.calculator_frame, fg_color="transparent")
        self.header_frame.pack(pady=(20, 10))

        # University crest
        self.logo_label = ctk.CTkLabel(self.header_frame, image=self.ugm_logo, text="")
        self.logo_label.pack(side="left", padx=(0, 12))

        # Application title
        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text="UGM Calculator",
            font=("Arial", 28, "bold"),
            text_color="#FFFFFF"
        )
        self.title_label.pack(side="left")

        
        # Calculator display
        self.display = ctk.CTkLabel(
            self.calculator_frame,
            text="0",
            width=380,
            height=65,
            font=("Arial", 28),
            anchor="e",
            fg_color=COLORS["primary"],
            text_color=COLORS["white"],
            corner_radius=10,
            padx=20,
        )
        self.display.pack(padx=20, pady=(10, 15))

        # Calculator buttons frame
        self.buttons_frame = ctk.CTkFrame(self.calculator_frame, fg_color="transparent")
        self.buttons_frame.pack(padx=20, pady=15)

        # Button layout
        buttons = [
            ["C", "⌫", "(", ")"],
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]

        # Create buttons
        for row_index, row in enumerate(buttons):
            for col_index, button_text in enumerate(row):

                # Choose futuristic button colours
                if button_text == "=":
                    button_color = "#2A6FB7"
                    text_color = "#FFFFFF"

                elif button_text in ("+", "-", "×", "÷"):
                    button_color = "#17385F"
                    text_color = "#6FA8E8"

                elif button_text in ("C", "⌫", "(", ")"):
                    button_color = "#10294B"
                    text_color = "#FFFFFF"

                else:
                    button_color = "#17385F"
                    text_color = "#FFFFFF"

                button = ctk.CTkButton(
                    self.buttons_frame,
                    text=button_text,
                    width=85,
                    height=55,
                    font=("Arial", 20, "bold"),
                    fg_color=button_color,
                    text_color=text_color,
                    hover_color=COLORS["accent"],
                    corner_radius=14,
                    border_width=1,
                    border_color=COLORS["accent"],
                    command=(
                        (lambda value=button_text: self.on_number_click(value))
                        if button_text in "0123456789."
                        else (
                            (lambda value=button_text: self.on_operator_click(value))
                            if button_text in "+-×÷"
                            else (
                                self.on_equals_click
                                if button_text == "="
                                else (
                                    self.on_clear_click
                                    if button_text == "C"
                                    else (
                                        self.on_backspace_click
                                        if button_text == "⌫"
                                        else (
                                            (
                                                lambda value=button_text: self.on_parenthesis_click(
                                                    value
                                                )
                                            )
                                            if button_text in ("(", ")")
                                            else None
                                        )
                                    )
                                )
                            )
                        )
                    ),
                )

                button.grid(row=row_index, column=col_index, padx=5, pady=5)

        # Quick Guide button
        self.quick_guide_frame = ctk.CTkFrame(
            self.calculator_frame,
            fg_color="transparent"
        )
        self.quick_guide_frame.pack(
            fill="x",
            padx=20,
            pady=(10, 12)
        )

        # Toggle Quick Guide
        self.guide_visible = False
        self.quick_guide_button = ctk.CTkButton(
            self.quick_guide_frame,
            text="📖  QUICK GUIDE     ▼",
            font=("Arial", 14, "bold"),
            text_color="#6FA8E8",
            fg_color="#10294B",
            hover_color="#17385F",
            corner_radius=12,
            height=42,
            command=self.toggle_quick_guide
        )
        self.quick_guide_button.pack(fill="x")

        # Guide information
        self.guide_content = ctk.CTkFrame(
            self.quick_guide_frame,
            fg_color="#10294B",
            corner_radius=12
        )

        guide_items = [
            ("C", "Clear all inputs"),
            ("⌫", "Delete last digit"),
            ("( )", "Group calculations"),
            ("÷ ×", "Perform operations")
        ]

        for index, (symbol, description) in enumerate(guide_items):
            row = index // 2
            column = index % 2

            guide_item = ctk.CTkFrame(
                self.guide_content,
                fg_color="#17385F",
                corner_radius=8
            )
            guide_item.grid(
                row=row,
                column=column,
                padx=4,
                pady=4,
                sticky="nsew"
            )

            symbol_label = ctk.CTkLabel(
                guide_item,
                text=symbol,
                font=("Arial", 15, "bold"),
                text_color="#6FA8E8"
            )
            symbol_label.pack(anchor="w", padx=8, pady=(5, 0))

            description_label = ctk.CTkLabel(
                guide_item,
                text=description,
                font=("Arial", 10),
                text_color="#FFFFFF"
            )
            description_label.pack(
                anchor="w",
                padx=8,
                pady=(0, 5)
            )

        self.guide_content.grid_columnconfigure((0, 1), weight=1)

        
    
        # History title
        self.history_title = ctk.CTkLabel(
            self.history_frame,
            text="Calculation History",
            font=("Arial", 22, "bold"),
            text_color="#FFFFFF",
        )

        self.history_title.pack(pady=(20, 10))

        # scrollable history area

        self.history_list = ctk.CTkScrollableFrame(
            self.history_frame,
            width=250,
            height=350,
            fg_color=COLORS["background"],
            corner_radius=10,
        )

        self.history_list.pack(fill="both", expand=True, padx=15, pady=10)

        # Clear history button
        self.clear_history_button = ctk.CTkButton(
            self.history_frame,
            text="Clear History",
            width=180,
            height=40,
            font=("Arial", 15),
            fg_color=COLORS["operator"],
            hover_color=COLORS["accent"],
            text_color=COLORS["white"],
            corner_radius=10,
            border_width=1,
            border_color=COLORS["accent"],
            command=self.on_clear_history_click,
        )

        self.clear_history_button.pack(padx=15, pady=(5, 20))

        # Bind keyboard events to the window
        self.bind("<Key>", self.handle_keypress)

    # Map keyboard keys to calculator actions and ignore unsupported keys
    def handle_keypress(self, event):
        key = event.keysym
        char = event.char

        # Number keys and decimal point
        if char in "0123456789.":
            self.on_number_click(char)

        # Arithmetic operators
        elif char == "+":
            self.on_operator_click("+")
        elif char == "-":
            self.on_operator_click("-")
        elif char in ("*", "x", "X"):
            self.on_operator_click("×")
        elif char == "/":
            self.on_operator_click("÷")

        # Handle parentheses keyboard input
        elif char in ("(", ")"):
            self.on_parenthesis_click(char)

        # Functional keys
        elif key in ("Return", "KP_Enter"):
            self.on_equals_click()
        elif key == "BackSpace":
            self.on_backspace_click()
        elif key == "Escape":
            self.on_clear_click()
    def toggle_quick_guide(self):
        if self.guide_visible:
            self.guide_content.pack_forget()
            self.quick_guide_button.configure(
                text="📖  QUICK GUIDE     ▼"
            )
            self.guide_visible = False
        else:
            self.guide_content.pack(
                fill="x",
                pady=(6, 0)
            )
            self.quick_guide_button.configure(
                text="📖  QUICK GUIDE     ▲"
            )
            self.guide_visible = True

    # Add opening or closing parentheses to the current expression
    def on_parenthesis_click(self, parenthesis):
        if self.just_calculated:
            self.current_input = ""
            self.just_calculated = False

        self.current_input += parenthesis
        self.display.configure(text=self.current_input)

    def on_number_click(self, number):
        # If a calculation just finished, typing a number starts a fresh input
        if self.just_calculated:
            self.current_input = ""
            self.just_calculated = False

        # Prevent multiple decimal points
        if number == ".":
            current_number = self.current_input

            for operator in "+-×÷()":
                current_number = current_number.replace(operator, " ")

            current_number = (
                current_number.split()[-1] if current_number.split() else ""
            )

            if "." in current_number:
                return

        # Add zero before a leading decimal point
        if number == "." and not self.current_input:
            self.current_input = "0"

        # Add the selected number
        self.current_input += str(number)

        # Update the display
        self.display.configure(text=self.current_input)

        # Add arithmetic operators to the current expression

    def on_operator_click(self, operator):
        if not self.current_input:
            if operator == "-":
                self.current_input = "-"
            else:
                return

        elif self.current_input[-1] in "+-×÷":
            # Replace the previous operator
            self.current_input = self.current_input[:-1] + operator

        elif self.current_input[-1] == "(":
            # Allow negative numbers inside parentheses
            if operator != "-":
                return
            self.current_input += operator

        else:
            self.current_input += operator

        self.just_calculated = False
        self.display.configure(text=self.current_input)

        # Evaluate the complete expression and save it to history

    def on_equals_click(self):
        if not self.current_input or self.just_calculated:
            return

        expression = self.current_input

        try:
            result = evaluate_expression(expression)

            # Save calculation to history
            if self.history_manager.record_calculation(expression, result):
                self.update_history_display()

            # Display result
            self.current_input = str(result)
            self.display.configure(text=format_result(result))
            self.just_calculated = True

        except ValueError as error:
            self.display.configure(text=str(error))
            self.current_input = ""
            self.just_calculated = False

        # Quick Guide toggle functionality
    def on_clear_click(self):
        self.first_number = None
        self.operator = None
        self.current_input = ""
        self.just_calculated = False
        self.display.configure(text="0")
            # Sidebar navigation
    
    def show_section(self, section):
        # Hide all content panels
        self.calculator_frame.grid_remove()
        self.history_frame.grid_remove()
        self.help_frame.grid_remove()
        self.about_frame.grid_remove()

        # Show selected section
        if section == "Calculator":
            self.calculator_frame.grid()
            self.history_frame.grid_configure(
                row=0, column=2, columnspan=1,
                padx=(0, 30), pady=30, sticky="nsew"
            )

        elif section == "History":
            self.history_frame.grid_configure(
                row=0, column=1, columnspan=2,
                padx=(15, 30), pady=30, sticky="nsew"
            )
            self.history_frame.grid()
        elif section == "Help":
            self.help_frame.grid(
                row=0,
                column=1,
                columnspan=2,
                padx=(15, 30),
                pady=30,
                sticky="nsew"
            )
        elif section == "About":
            self.about_frame.grid(
                row=0,
                column=1,
                columnspan=2,
                padx=(15, 30),
                pady=30,
                sticky="nsew"
            )

        # Update active sidebar button
        for item, button in self.sidebar_buttons.items():
            is_active = item == section
            button.configure(
                fg_color="#254F83" if is_active else "transparent",
                font=("Arial", 14, "bold" if is_active else "normal"),
                border_width=1 if is_active else 0
            )


    
    def toggle_quick_guide(self):
        if self.guide_visible:
            self.guide_content.pack_forget()
            self.quick_guide_button.configure(
                text="📖  QUICK GUIDE     ▼"
            )
            self.guide_visible = False
        else:
            self.guide_content.pack(
                fill="x",
                pady=(6, 0)
            )
            self.quick_guide_button.configure(
                text="📖  QUICK GUIDE     ▲"
            )
            self.guide_visible = True


    def on_backspace_click(self):
        if self.just_calculated:
            return  # Prevent backspacing on the final result
        if self.current_input:
            self.current_input = self.current_input[:-1]
            display_text = self.current_input if self.current_input else "0"
            self.display.configure(text=display_text)

    def update_history_display(self):
    

        # Remove existing history items
        for widget in self.history_list.winfo_children():
            widget.destroy()

        # retrieve saved calculations
        history = self.history_manager.retrieve_history()

        # Display newest calculations first
        for record in reversed(history):
            expression = record["expression"]
            result = record["result"]

            history_item = ctk.CTkLabel(
                self.history_list,
                text=f"{expression}={format_result(result)}",
                font=("Arial", 15),
                text_color=COLORS["text"],
                anchor="w",
                wraplength=230,
            )

            history_item.pack(fill="x", padx=10, pady=5)

    def on_clear_history_click(self):
        # Remove all saved calculations
        self.history_manager.clear_history()

        # Refresh the history panel
        self.update_history_display()
