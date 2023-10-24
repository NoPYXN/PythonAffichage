import tkinter as tk

def Valider():
    nom = champ_Name.get()
    mdp = champ_Password.get()
    email = champ_Email.get()
    if nom and mdp and email:
        print("Nom d'utilisateur:", nom)
        print("Mot de passe:", mdp)
        print("Email:", email)
    else:
        print("Veuillez remplir tous les champs.")
    
fenetre = tk.Tk()
fenetre.title("Ma Premiere interface graphique")

Label_Name = tk.Label(fenetre, text="Nom d'utilisateur")
Label_Name.pack()
champ_Name = tk.Entry(fenetre)
champ_Name.pack()

Label_Password = tk.Label(fenetre, text="Mot de passe")
Label_Password.pack()
champ_Password = tk.Entry(fenetre, show="*")
champ_Password.pack()

Label_Email = tk.Label(fenetre, text="Email")
Label_Email.pack()
champ_Email = tk.Entry(fenetre)
champ_Email.pack()

boutonFinish = tk.Button(fenetre, text="Valider l'inscription",command=Valider)
boutonFinish.pack()

fenetre.geometry("400x300")
fenetre.mainloop()