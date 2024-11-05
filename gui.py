from tkinter import *
from tkinter import filedialog
import subprocess
import ttkbootstrap as tb

root = tb.Window(themename = "superhero")

root.title("CN_Antivirus_Project")
root.geometry("1440x900")

file_path = ""
upload_type = "file"

#updating the file path based on user selection of the file
def file_dialog():
    global file_path
    if upload_type == "file":
        file_path = filedialog.askopenfile()
    else:
        file_path = filedialog.askdirectory()
    if file_path:
        file_label.config(text = "Chosen Path: " + file_path)
    else:
        file_label.config(text = "No path selected")
def execute_engine(file_path):
    pass

#function that changes the upload type upon button press
def toggle_upload_type():
    global upload_type
    if upload_type == "file":
        upload_type = "directory"
        toggle_button.config(text = "Switch to File Upload")
    else:
        upload_type = "file"
        toggle_button.config(text = "Switch to Directory Upload")
    
#Main Label
my_label = tb.Label(text = "Antivirus Software", font = ("Helvetica", 40), bootstyle = "default")
my_label.pack(pady = 10)

#switching between single and multiple file uploads
toggle_button = tb.Button(text = "Switch to Diretory Upload", bootstyle = "secondary", command = toggle_upload_type)
toggle_button.pack(pady = 10)

#simply displaying the file path
file_label = tb.Label(text = "", font = ("Helvetica, 40"), bootstyle = "default")
file_label.pack(pady = 10)

#loading the image , to be clicked for file upload
image = PhotoImage(file = "images/upload_image.png")#change this
image_button = tb.Label(image = image)
image_button.pack(pady = 10)

#binding the button functionality for the image, for file upload
image_button.bind("<Button-1>", lambda event: file_dialog)


#calling engine_execute function on button press
my_button = tb.Button(text = "Upload", bootstyle = "primary, outline", command = lambda : execute_engine(file_path))
my_button.config(padding = "40 15")
my_button.pack(pady = 10)




