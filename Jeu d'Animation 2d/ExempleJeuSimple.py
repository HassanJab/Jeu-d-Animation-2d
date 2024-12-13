# -*- coding: utf-8 -*-
"""
Exemple de jeu : programme principal
"""
import EntiteDuJeu
import pygame
from pygame import Color

pygame.init()  # Initialiser les modules de Pygame
LARGEUR_FENETRE = 400
HAUTEUR_FENETRE = 600
fenetre = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))  # Ouvrir la fenêtre
EntiteDuJeu.EntiteAnimeeAvecSon.set_fenetre(fenetre)  # Associer la fenêtre au module
pygame.display.set_caption("Exemple de jeu avec module EntiteDuJeu")

horloge = pygame.time.Clock()  # Pour contrôler la fréquence des scènes

# Création de la liste des entités du jeu
liste_entite = [
    EntiteDuJeu.BotAnime(pygame.Rect((10, 100), (40, 80)), [3, 3], "Son2.wav"),
    EntiteDuJeu.BotAnime(pygame.Rect((200, 200), (50, 100)), [0, 2], "Son2.wav"),
    EntiteDuJeu.ItiAnimeVolant(pygame.Rect((200, 50), (50, 100)), [3, 0], "Son3.wav", 3),
    EntiteDuJeu.EntiteAnimeeParImages(pygame.Rect((50, 100), (100, 100)), [5, 5], "Son4.wav", 9, "coq"),
    EntiteDuJeu.EntiteChangeante(pygame.Rect((150, 150), (50, 50)), [2, 4], "Son5.wav"),
    EntiteDuJeu.EntiteCirculaire(pygame.Rect((250, 250), (30, 30)), [0, 0], "Son5.wav", 120)
]

# Lier la liste des entités au module EntiteDuJeu
EntiteDuJeu.EntiteAnimeeAvecSon.entites = liste_entite

# Boucle d'animation
fin = False
while not fin:
    event = pygame.event.poll()  # Chercher le prochain évènement à traiter
    if event.type == pygame.QUIT:  # Utilisateur a cliqué sur la fermeture de fenêtre ?
        fin = True  # Fin de la boucle du jeu
    else:
        if event.type == pygame.MOUSEBUTTONUP:  # Utilisateur a cliqué dans la fenêtre ?
            x, y = event.pos  # Position de la souris
            for une_entite in liste_entite[:]:  # Copie pour éviter les modifications pendant l'itération
                if une_entite.touche(x, y):
                    une_entite.emettre_son()
                    liste_entite.remove(une_entite)

        # Mise à jour de toutes les entités
        for une_entite in liste_entite:
            une_entite.prochaine_scene()

        # Dessiner toutes les entités
        fenetre.fill(Color('white'))  # Dessiner le fond de la surface de dessin
        for une_entite in liste_entite:
            une_entite.dessiner()

        pygame.display.flip()  # Mettre à jour la fenêtre graphique
        horloge.tick(60)  # Pour animer avec 60 images par seconde

pygame.quit()  # Terminer pygame
