"""
Auteur : Marc-Antoine BUCHET
Date : 31/03/2021

BUT :
Tracer la représentation graphique d'une sinusoïde : s(t) = a*cos(omega*t + phi)
"""

# Imports de bibliothèques :
import numpy as np
import matplotlib.pyplot as plt

#==============================================================================
## Paramétrage de pyplot :
#==============================================================================
# Graduations en gras et en plus gros :
font = {'family' : 'sans',
        'weight' : 'bold',
        'size'   : 12}
plt.rc('font', **font)

# Activation du mode interactif :
plt.ion()


#==============================================================================
## Paramètres numériques :
#==============================================================================
# Nombre de points pour les graphiques :
N = 1000

#==============================================================================
## Paramètres physiques :
#==============================================================================
# Amplitude :
a = 1. # u.a

# Fréquence :
f = 1. # Hz

# Phase à l'origine :
phi = 0. # rad

# On en déduit la pulsation :
omega = 2*np.pi*f

# Et la période :
T = 1/f

#==============================================================================
## Grandeurs à représenter :
#==============================================================================
# On calcule les abscisses du graphe (ici les dates auxquelles calculer s(t) ) :
t_min = -1.*T # En nombre de périodes, c'est le plus pertinent
t_max = 2.*T
t = np.linspace(t_min,t_max,N)

# Et les ordonnées :
s = a*np.cos(omega*t+phi)

#==============================================================================
## Représentation graphique :
#==============================================================================
nom_de_la_figure = "sinusoide"
fig = plt.figure(nom_de_la_figure)
plt.plot(t,s)
plt.xlabel('t en s',fontweight = 'bold')
plt.ylabel('s(t) en u.a.',fontweight = 'bold')
plt.grid()
plt.tight_layout()
fig.savefig(nom_de_la_figure+'.pdf')
