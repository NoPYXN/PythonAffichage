import tkinter as tk

def evaluer():
    try:
        expression = champ_calcul.get()
        resultat = eval(expression)
        champ_resultat.delete(0, tk.END)
        champ_resultat.insert(tk.END, str(resultat))
    except Exception as e:
        champ_resultat.delete(0, tk.END)
        champ_resultat.insert(tk.END, "Erreur")

fenetre = tk.Tk()
fenetre.title("Calculatrice")

champ_calcul = tk.Entry(fenetre)
champ_calcul.pack()

boutons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

for i in range(4):
    ligne = tk.Frame(fenetre)
    ligne.pack(side=tk.TOP)
    for j in range(4):
        bouton = boutons[i * 4 + j]
        tk.Button(ligne, text=bouton, command=lambda b=bouton: champ_calcul.insert(tk.END, b)).pack(side=tk.LEFT)

evaluer_button = tk.Button(fenetre, text="Évaluer", command=evaluer)
evaluer_button.pack()

champ_resultat = tk.Entry(fenetre)
champ_resultat.pack()

fenetre.geometry("400x300")
fenetre.mainloop()
