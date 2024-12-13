# -*- coding: utf-8 -*-
"""
Module qui contient la hiérarchie des classes EntiteAnimee
"""
import pygame
from pygame import Color

class EntiteAnimeeAvecSon:
    """ Un objet représente une entité qui est animée dans une fenêtre Pygame. """
    
    # Attribut statique pour partager les entités et la fenêtre
    entites = []
    f = None  # Surface de la fenêtre

    @staticmethod
    def set_fenetre(fenetre):
        """ Fixer la fenêtre de rendu graphique """
        EntiteAnimeeAvecSon.f = fenetre

    def __init__(self, rectangle, vitesse, fichier_son):
        self.r = rectangle
        self.v = vitesse
        self.son = pygame.mixer.Sound(fichier_son)

    def prochaine_scene(self):
        """ Déplacer selon self.v en diagonale en rebondissant sur les bords de la fenêtre """
        if self.r.x + self.v[0] > EntiteAnimeeAvecSon.f.get_width() - self.r.width or self.r.x + self.v[0] < 0:
            self.v[0] = -self.v[0]  # Inverser la direction en x
        if self.r.y + self.v[1] > EntiteAnimeeAvecSon.f.get_height() - self.r.height or self.r.y + self.v[1] < 0:
            self.v[1] = -self.v[1]  # Inverser la direction en y

        # Mettre à jour les coordonnées
        self.r.x += self.v[0]
        self.r.y += self.v[1]

        # Vérifier les collisions avec les autres entités
        for autre in EntiteAnimeeAvecSon.entites:
            if autre is not self and EntiteAnimeeAvecSon.verifier_collision(self, autre):
                # Inverser les directions pour simuler un rebond
                self.v[0], autre.v[0] = -self.v[0], -autre.v[0]
                self.v[1], autre.v[1] = -self.v[1], -autre.v[1]

    @staticmethod
    def verifier_collision(entite1, entite2):
        """ Vérifie si deux entités se chevauchent """
        return entite1.r.colliderect(entite2.r)

    def touche(self, x, y):
        """ Vérifie si le clic est à l'intérieur de l'entité """
        return self.r.collidepoint(x, y)

    def emettre_son(self):
        """ Joue un son lorsque l'entité est touchée """
        self.son.play()


class EntiteAvecEtat(EntiteAnimeeAvecSon):
    """ Une entité avec différents états d'animation """
    def __init__(self, rectangle, vitesse, fichier_son, nombre_etats):
        super().__init__(rectangle, vitesse, fichier_son)
        self.nombre_etats = nombre_etats
        self.etat_courant = 0

    def prochaine_scene(self):
        """ Passer à l'état suivant dans l'animation """
        self.etat_courant = (self.etat_courant + 1) % self.nombre_etats
        super().prochaine_scene()


class BotAnime(EntiteAnimeeAvecSon):
    """ Un objet représente un Bot qui est animé dans une fenêtre Pygame """

    def dessiner(self):
        """ Dessiner un Bot """
        pygame.draw.ellipse(BotAnime.f, Color('green'), ((self.r.x, self.r.y), (self.r.width, self.r.height / 2)))  # Tête
        pygame.draw.rect(BotAnime.f, Color('black'), ((self.r.x + self.r.width / 4, self.r.y + self.r.height / 8), (self.r.width / 10, self.r.height / 20)))  # Œil gauche
        pygame.draw.rect(BotAnime.f, Color('black'), ((self.r.x + self.r.width * 3 / 4 - self.r.width / 10, self.r.y + self.r.height / 8), (self.r.width / 10, self.r.height / 20)))  # Œil droit
        pygame.draw.line(BotAnime.f, Color('black'), (self.r.x + self.r.width / 4, self.r.y + self.r.height * 3 / 8), (self.r.x + self.r.width * 3 / 4, self.r.y + self.r.height * 3 / 8), 2)  # Bouche
        pygame.draw.rect(BotAnime.f, Color('red'), ((self.r.x, self.r.y + self.r.height / 2), (self.r.width, self.r.height / 2)))  # Corps


class ItiAnimeVolant(EntiteAvecEtat):
    """ Un objet représente un Iti qui vole dans une fenêtre Pygame """

    def dessiner(self):
        """ Dessiner un Iti """
        self.milieux = self.r.x + self.r.width / 2
        self.milieuy = self.r.y + self.r.height / 2

        pygame.draw.ellipse(ItiAnimeVolant.f, Color('pink'), ((self.r.x + self.r.width / 3, self.r.y), (self.r.width / 3, self.r.height / 4)))  # Tête
        pygame.draw.arc(ItiAnimeVolant.f, Color('black'), ((self.milieux - self.r.width / 12, self.r.y + self.r.height / 8), (self.r.width / 6, self.r.height / 14)), 3.1416, 0, 2)  # Sourire
        pygame.draw.ellipse(ItiAnimeVolant.f, Color('black'), ((self.milieux - self.r.width / 8, self.r.y + self.r.height / 12), (self.r.width / 12, self.r.height / 24)))  # Œil gauche
        pygame.draw.ellipse(ItiAnimeVolant.f, Color('black'), ((self.milieux + self.r.width / 8 - self.r.width / 12, self.r.y + self.r.height / 12), (self.r.width / 12, self.r.height / 24)))  # Œil droit
        pygame.draw.line(ItiAnimeVolant.f, Color('black'), (self.milieux, self.r.y + self.r.height / 4), (self.milieux, self.r.y + self.r.height * 3 / 4), 2)  # Corps
        pygame.draw.line(ItiAnimeVolant.f, Color('black'), (self.r.x, self.r.y + self.r.height / 4 + (self.r.height / 4) * self.etat_courant), (self.milieux, self.milieuy), 2)  # Bras gauche
        pygame.draw.line(ItiAnimeVolant.f, Color('black'), (self.r.x + self.r.width, self.r.y + self.r.height / 4 + (self.r.height / 4) * self.etat_courant), (self.milieux, self.milieuy), 2)  # Bras droit
        pygame.draw.line(ItiAnimeVolant.f, Color('black'), (self.r.x, self.r.y + self.r.height), (self.milieux, self.r.y + self.r.height * 3 / 4), 2)  # Jambe gauche
        pygame.draw.line(ItiAnimeVolant.f, Color('black'), (self.r.x + self.r.width, self.r.y + self.r.height), (self.milieux, self.r.y + self.r.height * 3 / 4), 2)  # Jambe droite


class EntiteAnimeeParImages(EntiteAvecEtat):
    """ Une entité animée par une séquence d'images """
    def __init__(self, rectangle, vitesse, fichier_son, nombre_etats, nom_dossier):
        super().__init__(rectangle, vitesse, fichier_son, nombre_etats)
        self.image_animation = [pygame.transform.scale(pygame.image.load(f"{nom_dossier}/{nom_dossier}{i + 1}.gif"), (self.r.width, self.r.height)) for i in range(nombre_etats)]

    def dessiner(self):
        EntiteAnimeeParImages.f.blit(self.image_animation[self.etat_courant], (self.r.x, self.r.y))


class EntiteChangeante(EntiteAnimeeAvecSon):
    """ Une entité qui change de couleur à chaque frame """
    def __init__(self, rectangle, vitesse, fichier_son):
        super().__init__(rectangle, vitesse, fichier_son)
        self.couleur = Color('blue')

    def prochaine_scene(self):
        super().prochaine_scene()
        hsva = self.couleur.hsva
        nouvelle_teinte = (hsva[0] + 30) % 360
        self.couleur.hsva = (nouvelle_teinte, hsva[1], hsva[2], hsva[3])

    def dessiner(self):
        pygame.draw.rect(EntiteAnimeeAvecSon.f, self.couleur, self.r)


class EntiteCirculaire(EntiteAnimeeAvecSon):
    """ Une entité qui suit un chemin circulaire """
    def __init__(self, rectangle, vitesse, fichier_son, rayon):
        super().__init__(rectangle, vitesse, fichier_son)
        self.rayon = rayon
        self.angle = 0

    def prochaine_scene(self):
        # Créer un vecteur unitaire basé sur l'angle actuel
        direction = pygame.math.Vector2(1, 0)  # Le vecteur initial est (1, 0), c'est-à-dire sur l'axe X
        direction.rotate_ip(self.angle)  # Tourner le vecteur de l'angle donné
        # Multiplier par le rayon pour obtenir la position finale
        self.r.x = int(direction.x * self.rayon) + EntiteAnimeeAvecSon.f.get_width() // 2
        self.r.y = int(direction.y * self.rayon) + EntiteAnimeeAvecSon.f.get_height() // 2

        # Incrémenter l'angle pour la prochaine scène
        self.angle = (self.angle + 5) % 360  # Vous pouvez ajuster cette valeur pour changer la vitesse de rotation

    def dessiner(self):
        pygame.draw.circle(EntiteAnimeeAvecSon.f, Color('purple'), (self.r.x, self.r.y), self.r.width // 2)
