import tkinter as tk
from tkinter import filedialog as fd
import customtkinter as ctk
import img2pdf as p
from time import sleep

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry("400x300")
app.title("Image to PDF")


def select_call_back():
    
    global files 
    files = fd.askopenfilenames(initialdir='/', title='Select Files')
    if files == "":
        label_1.configure(text = "No Files Selected")
    else:
        label_1.configure(text = "Files Selected")

def convert_call_back():
    
    with open(f"file.pdf", "wb") as f:
        f.write(p.convert(files))

    label_1.configure(text = "Ready to Select Files")

#------------ frame
frame_1 = ctk.CTkFrame(master=app) 
frame_1.pack(pady=20, padx=60, fill="both", expand=True)


# --------------------- labels
label_1 = ctk.CTkLabel(master=frame_1, justify=tk.LEFT, text="Ready to Select Files")
label_1.pack(pady=10, padx=10)


#------------ buttons
select_button = ctk.CTkButton(master=frame_1 ,command=select_call_back, text="Select Images")
select_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

convert_button = ctk.CTkButton(master=frame_1, command=convert_call_back, text="Convert")
convert_button.place(relx=0.75, rely=0.6, anchor=tk.E)


if __name__ == '__main__':
    app.mainloop()