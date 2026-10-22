import tkinter as tk
import customtkinter


# Appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
#Window test example no edits made yet
app = customtkinter.CTk()

#Title and size of the window
app.title("UGM Calculator")
app.geometry("450x500")

#Buttons
button = customtkinter.CTkButton(master=app, text="+")
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
app.mainloop()