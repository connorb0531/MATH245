import numpy as np
import matplotlib.pyplot as plt

# constants
NUM_PARTICLES   = 10000       
SCREEN_WIDTH    = 0.02            
NUM_BINS        = 1000        
SLIT_SEPARATION = 1.0e-4         
WAVELENGTH      = 5.0e-7         
SCREEN_DISTANCE = 1.0             

# theory
x_vals = np.linspace(-SCREEN_WIDTH/2, SCREEN_WIDTH/2, NUM_BINS)
theta = x_vals / SCREEN_DISTANCE                 
prob_theo = np.cos(np.pi * SLIT_SEPARATION * theta / WAVELENGTH) **2
prob_theo /= prob_theo.sum()                         

# empirical
empirical_hits = np.random.choice(x_vals, size=NUM_PARTICLES, p=prob_theo)     
hist, edges = np.histogram(empirical_hits,bins=NUM_BINS, range=(x_vals.min(), x_vals.max()), density=False)        
hist = hist / NUM_PARTICLES                           
centers = 0.5 * (edges[:-1] + edges[1:])

# plot
plt.figure(figsize=(10, 5))
plt.plot(x_vals, prob_theo, label="Theoretical", linewidth=2, zorder=0)
plt.step(centers, hist, where="mid", label="Empirical", alpha=0.6)
plt.xlabel("Screen position x  (m)")
plt.ylabel("Probability per bin")
plt.title("Double‑Slit Interference: Empirical vs. Theoretical")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()