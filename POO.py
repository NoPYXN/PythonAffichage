
from typing import Self


class telephone :
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def affichage(self) :
        print("voilà le nouveau" + Self.marque + Self.modele)


test = telephone("Samsung", "S24 Ultra")
test.affichage