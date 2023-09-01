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

        # Creation de la fonction qui va recuperer le lien de la destination du fichier
        def OpenDirectory():
            self.file_path = filedialog.askdirectory()

        # Creation de la fonction qui va creer le QRcode
        def CreateQRcode():
            qr = qrcode.QRCode(
                version=random.randint(1, 10),
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )


            qr.add_data(self.entree.get())
            qr.make(fit=True)

            self.img = qr.make_image(fill_color="black", back_color="white")
            self.img.save(self.file_path + '/' + self.title.get())

            self.imageLue = Image.open(self.file_path + '/' + self.title.get())

            self.imageLue.show()

        # Creation du label pour expliquer qu'il faut mettre un lien
        self.explain = customtkinter.CTkLabel(master=self.root, text='Entrer un lien')
        self.explain.pack()

        # Creation d'une entry pour entrer le lien
        self.entree = customtkinter.CTkEntry(master=self.root, width=200)
        self.entree.pack()

        # # Creation d'un label expliquer qu'il faut bien mettre son expansion
        self.titleLabel = customtkinter.CTkLabel(master=self.root, text="donner un nom (avec son extension)")
        self.titleLabel.pack()

        # Creation d'une entry pour entrer le nom du fichier
        self.title = customtkinter.CTkEntry(master=self.root)
        self.title.pack()

        # Creation du boutton pour choisi la location du QRcode
        self.button = customtkinter.CTkButton(master=self.root, text="Choisir un endroit", command=OpenDirectory)
        self.button.pack(pady=10)

        # Creation du bouton pour enregistrer le QRcode
        self.finish = customtkinter.CTkButton(master=self.root, text="créer", command=CreateQRcode)
        self.finish.pack()

        self.root.mainloop()

Main()
