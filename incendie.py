######################################
# Groupe BI 2
# Lenny BACKORY
# Andrew BAYISSA
# Joris ANGAMAN
# Martin DIAMANT
# Amel LASSAN
# Thomas TURPIN
# https://github.com/uvsq22004392/projet_incendie




import tkinter as tk 
import random

racine = tk.Tk()



canvas= tk.Canvas(racine, height = 500, width = 250, bg="white")
canvas.grid(column=0)
canvas2= tk.Canvas(racine, height = 500, width = 700, bg="white")
canvas2.grid(column=1, row=0)

bouton1 = tk.Button(racine, text="Génération de terrain aléatoire", font = ("helvetica", "10"))
bouton1.place(x=0, y=100)

bouton2 = tk.Button(racine, text="Sauvegarde du terrain", font=("helvetica", "10"))
bouton2.place(x=0, y=130)

bouton3 = tk.Button(racine, text="Charger un terrain", font = ("helvetica", "10"))
bouton3.place(x=0, y=160)

bouton4 = tk.Button(racine, text="Prochaine étape", font = ("helvetica", "10"))
bouton4.place(x=0, y=200)

bouton5 = tk.Button(racine, text="Démarrer la simulation", font = ("helvetica", "10"))
bouton5.place(x=0, y=230)

bouton6 = tk.Button(racine, text="Stopper la simulation", font = ("helvetica", "10"))
bouton6.place(x=0, y=260)


racine.mainloop