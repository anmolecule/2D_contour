__author__ = "Anmol Kumar"
__date__   = "02/09/2021"
__modified__ = "21/09/2022"

# Usage: python plotcontour.py csvfile HeaderContainingEnergy
# Aim: Take Phi and Psi data distributed in a range -180 to 180
#      Sort the data
#      Generate 2D grid -180 to 180; stepsize 30.
#      Get data to plot.
#      Interpolate the data on the generated grid.
#      Plot the contour using matplotlib.

import os,sys
import pandas as pd
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.tri as tri
from scipy.interpolate import griddata
plt.style.use('seaborn-white')

def getxyzcontour(df,xch='Phi',ych='Psi',zch=None):
    df_sorted=df.sort_values(by=['Phi','Psi'])
    df_sorted=df_sorted.reset_index()
    df_sorted=df_sorted.drop(columns=['index'])
    x=df_sorted['Phi'].to_numpy() 
    y=df_sorted['Psi'].to_numpy() 
    z=df_sorted[sys.argv[2]].to_numpy()
    xi = np.linspace(-180, 180, 30)   # xi stepsize = 12 degrees
    yi = np.linspace(-180, 180, 30)   # yi stepsize = 12 degrees
    XI,YI=np.meshgrid(xi,yi)
    zi = griddata((x, y), z, (XI,YI), method='cubic')
    return (xi,yi,zi)
 
def plotxyzcontour(xi,yi,zi,zch=None):
    fig, axs = plt.subplots(figsize=(8,8),dpi=600)
    cp = axs.contour(xi, yi, zi, levels=15, linewidths=0.5, colors='k')
    cntur = axs.contourf(xi, yi, zi, levels=15, cmap="RdBu")
    fig.colorbar(cntur, ax=axs)
    #axs.clabel(cp, inline=True, fontsize=10)
    axs.set(xlim=(-180, 180), ylim=(-180, 180))
    axs.set_xticks(np.arange(-180,181,30))
    axs.set_yticks(np.arange(-180,181,30))
    axs.set_aspect('equal', adjustable='box')
    plt.title('Contour Plot for '+zch) #(%d points, %d grid points)' %
    plt.tight_layout()
    mzch=zch.replace('/', '')
    plt.savefig("contour_"+mzch+".png",dpi=600)
    #plt.show()
    print ("Successfully saved contour in contour_%s.png"%(mzch))


if __name__ == "__main__":
    filename=sys.argv[1]
    df=pd.read_csv(filename)
    zch=sys.argv[2]
    print ("Assuming your csv file column headers contain Phi and Psi")
    xi,yi,zi=getxyzcontour(df,xch='Phi',ych='Psi',zch=zch)
    plotxyzcontour(xi,yi,zi,zch=zch)
    sys.exit()
