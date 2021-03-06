"""
Auteur : Marc-Antoine BUCHET
Date : 31/03/2021

BUT :
Tracer la représentation graphique d'une sinusoïde : s(t) = a*cos(omega*t + phi)
"""

## Imports de bibliothèques :
import numpy as np
import matplotlib.pyplot as plt

## Paramétrage de pyplot :
plt.rc('font', weight="bold", size=12) # Graduations en gras et en plus gros
N = 1000 # Nombre de points pour les graphiques

## Paramètres physiques :
# Amplitude :
a = 1. # u.a.

## Grandeurs à représenter :
# On calcule les abscisses du graphe (ici les dates auxquelles calculer s(t) ) :

# Et les ordonnées :

## Représentation graphique :
