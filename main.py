import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("UGM_Calculator")
app.geometry("900x600")
app.minsize(700, 500)

app.mainloop()