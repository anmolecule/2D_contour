# Author: Anmol Kumar
# Date: 02/09/2021

# Usage: python plotcontour_A.py csvfile HeaderContainingEnergy

import os,sys
import pandas as pd
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from scipy.interpolate import griddata
plt.style.use('seaborn-white')

filename=sys.argv[1]
df=pd.read_csv(filename) 
df_sorted=df.sort_values(by=['Phi','Psi'])
df_sorted=df_sorted.reset_index()
df_sorted=df_sorted.drop(columns=['index'])
x=df_sorted['Phi'].to_numpy() 
y=df_sorted['Psi'].to_numpy() 
z=df_sorted[sys.argv[2]].to_numpy()
xi = np.linspace(-180, 180, 25)
yi = np.linspace(-180, 180, 25)
XI,YI=np.meshgrid(xi,yi)

fig, axs = plt.subplots(figsize=(8,8),dpi=300)
zi = griddata((x, y), z, (XI,YI), method='cubic')
axs.contour(xi, yi, zi, levels=13, linewidths=0.5, colors='k')
cntur = axs.contourf(xi, yi, zi, levels=13, cmap="RdBu_r")
fig.colorbar(cntur, ax=axs)
axs.set(xlim=(-180, 180), ylim=(-180, 120))
axs.set_xticks(np.arange(-180,181,30))
axs.set_yticks(np.arange(-180,121,30))
axs.set_aspect('equal', adjustable='box')
plt.title('Contour Plot for '+sys.argv[2]) #(%d points, %d grid points)' %
plt.tight_layout()
nk=sys.argv[2].replace('/', '')
print (nk)
plt.savefig("testcontour_"+nk+".png",dpi=600)
#plt.show()

sys.exit()
