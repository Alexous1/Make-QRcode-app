from tkinter import *
from tkinter import filedialog
import qrcode
import random
from PIL import Image

class Main():

    def __init__(self):

        # Creation de la fenetre
        self.fenetre = Tk()
        self.fenetre.title("Create a qrcode")
        self.bg = "#25ebf1"
        self.fenetre.geometry('300x275')
        self.fenetre.config(bg=self.bg)
        self.img = 'rien'

        # Creation de la fonction qui va recuperer le lien de la destination du fichier
        def OpenDirectory():
            self.file_path = filedialog.askdirectory()

        # Creation de la fonction qui va creer le QRcode
        def CreateQRcode():
            qr = qrcode.QRCode(
                version=random.randint(1, 10),
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=random.randint(1, 20),
                border=4,
            )
            qr.add_data(self.entree.get())
            qr.make(fit=True)

            self.img = qr.make_image(fill_color="black", back_color="white")
            self.img.save(self.file_path + '/' + self.title.get())

            self.imageLue = Image.open(self.file_path + '/' + self.title.get())

            self.imageLue.show()

        # Creation du premier frame qui contient le lien ainsi que le label pour expliquer
        self.frame_lien = Frame(self.fenetre, bg=self.bg)
        self.frame_lien.pack(pady=10)

        # Creation du deuxième frame qui contient le nom du fichier ainsi que la location du fichier
        self.frame_stop = Frame(self.fenetre, bg=self.bg)
        self.frame_stop.pack(pady=10)

        # Creation du label pour expliquer qu'il faut mettre un lien
        self.explain = Label(self.frame_lien, text='Entrer un lien', bg=self.bg, fg='black')
        self.explain.pack(pady=2.5)

        # Creation d'une entry pour entrer le lien
        self.entree = Entry(self.frame_lien, width=30, relief=GROOVE, bd=0, bg='white', fg='black')
        self.entree.pack()

        # # Creation d'un label expliquer qu'il faut bien mettre son expansion
        self.titleLabel = Label(self.frame_stop, text="donner un nom (avec son extension)", bg=self.bg, fg='black')
        self.titleLabel.pack()

        # Creation d'une entry pour entrer le nom du fichier
        self.title = Entry(self.frame_stop, bd=0, bg='white', fg='black')
        self.title.pack()

        # Creation du boutton pour choisi la location du QRcode
        self.button = Button(self.frame_stop, text="Choisir un endroit", bd=0, command=OpenDirectory)
        self.button.pack(pady=1.5)

        # Creation du bouton pour enregistrer le QRcode
        self.finish = Button(self.frame_stop, text="créer", command=CreateQRcode, bd=0)
        self.finish.pack(pady=20)


        self.fenetre.mainloop()

Main()
