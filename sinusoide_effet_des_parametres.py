"""
Auteur : Marc-Antoine BUCHET
Date : 31/03/2021

BUT :
Tracer la représentation graphique d'une sinusoïde et voir l'effet des
différents paramètres sur le signal.
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
# Référence :
a_ref = 1. # u.a, amplitude
f_ref = 1. # Hz, fréquence
phi_ref = 0. # rad, phase à l'origine
omega_ref = 2*np.pi*f_ref # pulsation
T_ref = 1/f_ref # période

# Signal étudié :
a = 1. # u.a, amplitude
f = 1. # Hz, fréquence
phi = 0. # rad, phase à l'origine
omega = 2*np.pi*f # pulsation
T = 1/f # période


#==============================================================================
## Grandeurs à représenter :
#==============================================================================
# On calcule les abscisses du graphe (ici les dates auxquelles calculer s(t) ) :
t_min = -1.*T_ref # En nombre de périodes, c'est le plus pertinent
t_max = 2.*T_ref
t = np.linspace(t_min,t_max,N)

# Et les ordonnées :
s_ref = a_ref*np.cos(omega_ref*t+phi_ref)
s = a*np.cos(omega*t+phi)


#==============================================================================
## Représentation graphique :
#==============================================================================
nom_de_la_figure = "sinusoide_effet_des_parametres"
fig = plt.figure(nom_de_la_figure)
plt.plot(t,s,label = "Signal")
plt.plot(t,s_ref,'--',label = "Référence")
plt.xlabel('t en s',fontweight = 'bold')
plt.ylabel('s(t) en u.a.',fontweight = 'bold')
plt.grid()
plt.legend()
plt.tight_layout()
fig.savefig(nom_de_la_figure+'.pdf')
