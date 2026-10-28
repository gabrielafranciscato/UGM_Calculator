
import customtkinter as ctk
from gui import CalculatorApp

# Configure the application appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def main():
    app = CalculatorApp()
    app.mainloop()


if __name__ == "__main__":
    main()
