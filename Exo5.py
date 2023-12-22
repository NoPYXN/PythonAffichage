import tkinter as tk
import json
from tkinter import messagebox

# Fonction pour ajouter un contact à la liste
def ajouter_contact():
    nom = entry_nom.get()
    prenom = entry_prenom.get()
    telephone = entry_telephone.get()
    contact = f"{nom} {prenom} - {telephone}"
    contact_listbox.insert(tk.END, contact)
    popup.destroy()

# Fonction pour afficher la fenêtre pop-up
def afficher_popup():
    global popup, entry_nom, entry_prenom, entry_telephone
    popup = tk.Toplevel(fenetre)
    popup.title("Ajouter un contact")
    
    label_nom = tk.Label(popup, text="Nom:")
    label_nom.pack()
    entry_nom = tk.Entry(popup)
    entry_nom.pack()
    
    label_prenom = tk.Label(popup, text="Prénom:")
    label_prenom.pack()
    entry_prenom = tk.Entry(popup)
    entry_prenom.pack()
    
    label_telephone = tk.Label(popup, text="Téléphone:")
    label_telephone.pack()
    entry_telephone = tk.Entry(popup)
    entry_telephone.pack()
    
    valider_button = tk.Button(popup, text="Valider", command=ajouter_contact)
    valider_button.pack()
    popup.geometry("300x200")

def sauvegarder_en_json():
    selected = contact_listbox.curselection()  # Récupère l'index de l'élément sélectionné
    nom_fichier = nom_liste_entry.get()
    if selected:
        with open(f"{nom_fichier}.json", "w") as f:
            json.dump(contacts, f)
        messagebox.showinfo("Sauvegarde", f"Liste de tâches '{nom_fichier}' enregistrée avec succès.")
        # nom_liste_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Erreur", "Veuillez saisir un nom de liste.")


# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Gestion de contacts")

contacts = []

ajouter_button = tk.Button(fenetre, text="Ajouter un contact", command=afficher_popup, padx=50)
ajouter_button.pack()
ajouter_button.place(x=125, y=25)


contact_listbox = tk.Listbox(fenetre, selectmode=tk.SINGLE, height=40,width=50)
contact_listbox.pack()
contact_listbox.place(x=75, y=75)


supprimer_button = tk.Button(fenetre, text="Supprimer le contact", padx=47)
supprimer_button.pack()
supprimer_button.place(x=125, y=725)

nom_liste_label = tk.Label(fenetre, text="Nom de la liste:")
nom_liste_label.pack()
nom_liste_label.place(x=350, y=380)
nom_liste_entry = tk.Entry(fenetre,width=33)
nom_liste_entry.pack()
nom_liste_entry.place(x=300, y=420)

sauvegarder_button = tk.Button(fenetre, text="Sauvegarder en JSON", command=sauvegarder_en_json, padx=30)
sauvegarder_button.pack()
sauvegarder_button.place(x=125, y=755)

fenetre.geometry("550x1080")
fenetre.mainloop()