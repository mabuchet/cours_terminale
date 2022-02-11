"""
Auteur : Marc-Antoine BUCHET
Date : 31/03/2021

BUT :
Tracer la représentation graphique d'un phénomène de battements.
"""

## Imports de bibliothèques :
import numpy as np
import matplotlib.pyplot as plt

## Booléen pour décider de sauvegarder les graphiques ou non :
sauvegarder_grapiques = False

## Paramétrage de pyplot :
plt.rc('font', weight="bold", size=12) # Graduations en gras et en plus gros
N = 1000 # Nombre de points pour les graphiques

## Paramètres physiques :
# Amplitude des deux signaux :
a = 1.5
a_1 = a # u.a.
a_2 = a # u.a.

# Fréquences des deux signaux :
f_1 = 450. # Hz
f_2 = 430. # Hz

# Phases à l'origine des deux signaux sinusoïdaux :
phi_1 = 0. # rad
phi_2 = 0. # rad

# On en déduit les pulsations des deux signaux sinusoïdaux :
omega_1 = 2*np.pi*f_1
omega_2 = 2*np.pi*f_2

# Les périodes :
T_1 = 1/f_1
T_2 = 1/f_2

# Et les fréquences, pulsations, périodes et phases du battement :
# 'p' pour porteuse et 'e' pour enveloppe
f_p = ( f_1 + f_2 ) / 2
f_e = ( f_1 - f_2 ) / 2

omega_p = 2*np.pi*f_p
omega_e = 2*np.pi*f_e

T_p = 1/f_p
T_e = 1/f_e

phi_p = ( phi_1 + phi_2 ) / 2
phi_e = ( phi_1 - phi_2 ) / 2

## Grandeurs à représenter :
# On calcule les abscisses du graphe (ici les dates auxquelles calculer s(t) ) :
t_min = 0
t_max = 1.*T_e # 1. fois la période de l'enveloppe
t = np.linspace(t_min,t_max,N)

# Et les ordonnées :
s_1 = a_1*np.cos(omega_1*t+phi_1)
s_2 = a_2*np.cos(omega_2*t+phi_2)
s = s_1 + s_2
s_bat = 2*a*np.cos(omega_p*t+phi_p)*np.cos(omega_e*t+phi_e)
porteuse = np.cos(omega_p*t+phi_p)
enveloppe_plus = 2*a*np.cos(omega_e*t+phi_e)
#enveloppe_moins = -enveloppe_plus

## Représentations graphiques :
nom_de_la_figure = "battements"
fig = plt.figure(nom_de_la_figure)
plt.plot(t,s,label = "Battement")
plt.plot(t,enveloppe_plus,'r--',label = "Enveloppe")
#plt.plot(t,enveloppe_moins,'r--')
plt.plot(t,porteuse,':',label = "Porteuse")
plt.xlabel('t en s',fontweight = 'bold')
plt.ylabel('s(t) en u.a.',fontweight = 'bold')
plt.grid(True)
plt.legend()
#plt.axis('off') # pour retirer les axes (utilisé pour l'image d'intro du poly)
plt.show()

if sauvegarder_grapiques :
    fig.savefig(nom_de_la_figure+'.pdf')
