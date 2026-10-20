import tkinter as tk

def clear_display():
    """Clear the entire display."""
    display.delete(0, tk.END)

def backspace():
    """Remove the last character from the display."""
    current_text = display.get()
    if current_text:  # Only delete if there's something
        display.delete(len(current_text)-1, tk.END)

# Create main application window
root = tk.Tk()
root.title("Backspace & Clear GUI")
root.geometry("300x150")  # Width x Height
root.resizable(False, False)

# Entry widget for display
display = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
display.pack(fill="both", padx=10, pady=10, ipady=5)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(padx=10, pady=10)

# Clear button
clear_btn = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 14),
    width=10,
    height=2,
    command=clear_display
)
clear_btn.grid(row=0, column=0, padx=5, pady=5)

# Backspace button
backspace_btn = tk.Button(
    button_frame,
    text="Backspace",
    font=("Arial", 14),
    width=10,
    height=2,
    command=backspace
)
backspace_btn.grid(row=0, column=1, padx=5, pady=5)

# Start the GUI event loop
root.mainloop()
