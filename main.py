from tkinter import *
from tkinter import filedialog
import customtkinter
import qrcode
import random
from PIL import Image

class Main():

    def __init__(self):

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")


        # Creation de la fenetre
        self.root = customtkinter.CTk()
        self.root.title("Create a qrcode")
        self.root.geometry('250x215')
        self.img = 'rien'

        # Create a function to have the destination of the file
        def OpenDirectory():
            self.file_path = filedialog.askdirectory()

        # Create a function to create the QRcode and save it
        def CreateQRcode():
            qr = qrcode.QRCode(
                version=random.randint(1, 10),
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )

            # add the link to the Qrcode
            qr.add_data(self.entree.get())
            qr.make(fit=True)

            # Save the Qrcode to the right destination
            self.img = qr.make_image(fill_color="black", back_color="white")
            self.img.save(self.file_path + '/' + self.title.get())

            self.imageLue = Image.open(self.file_path + '/' + self.title.get())

            self.imageLue.show()

        # Create a label to explain the need a link
        self.explain = customtkinter.CTkLabel(master=self.root, text='Entrer un lien')
        self.explain.pack()

        # Create an entry to have the link of the Qrcode
        self.entree = customtkinter.CTkEntry(master=self.root, width=200)
        self.entree.pack()

        # Create a label to explain it's very important to give the extension of the file with the name of the file
        self.titleLabel = customtkinter.CTkLabel(master=self.root, text="donner un nom (avec son extension)")
        self.titleLabel.pack()

        # Create ann entry to give a name of the Qrcode file
        self.title = customtkinter.CTkEntry(master=self.root)
        self.title.pack()

        # Create a button to choose the destination of the file
        self.button = customtkinter.CTkButton(master=self.root, text="Choisir un endroit", command=OpenDirectory)
        self.button.pack(pady=10)

        # Create a button to create and save the Qrcode
        self.finish = customtkinter.CTkButton(master=self.root, text="créer", command=CreateQRcode)
        self.finish.pack()

        self.root.mainloop()

Main()
