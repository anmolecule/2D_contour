__author__ = "Anmol Kumar"
__date__   = "02/09/2021"
__modified__ = "21/09/2022"

# Usage: python plotcontour.py csvfile
# Assumes the header names in csv file are Phi Psi and Energy
# Usage: python plotcontour.py csvfile col1name col2name col3name
# Aim: Take Phi and Psi data distributed in a range -180 to 180
#      Sort the data
#      Generate 2D grid -180 to 180; stepsize 12 degrees.
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

def getxyzcontour(df,xch='Phi',ych='Psi',zch='Energy'):
    df_sorted=df.sort_values(by=[xch,ych])
    df_sorted=df_sorted.reset_index()
    df_sorted=df_sorted.drop(columns=['index'])
    x=df_sorted[xch].to_numpy() 
    y=df_sorted[ych].to_numpy() 
    z=df_sorted[zch].to_numpy()
    xi = np.linspace(-180, 180, 30)   # xi stepsize = 12 degrees
    yi = np.linspace(-180, 180, 30)   # yi stepsize = 12 degrees
    XI,YI=np.meshgrid(xi,yi)
    zi = griddata((x, y), z, (XI,YI), method='cubic')
    return (xi,yi,zi)
 
def plotxyzcontour(xi,yi,zi,zch='Energy'):
    fig, axs = plt.subplots(figsize=(8,8),dpi=600)
    cp = axs.contour(xi, yi, zi, levels=15, linewidths=0.5, colors='k')
    cntur = axs.contourf(xi, yi, zi, levels=15, cmap="RdBu")
    fig.colorbar(cntur, ax=axs)
    #axs.clabel(cp, inline=True, fontsize=10)
    axs.set(xlim=(-180, 180), ylim=(-180, 180))
    axs.set_xticks(np.arange(-180,181,30))
    axs.set_yticks(np.arange(-180,181,30))
    axs.set_aspect('equal', adjustable='box')
    plt.title('Contour Plot for '+zch) 
    plt.tight_layout()
    mzch=zch.replace('/', '')
    plt.savefig("contour_"+mzch+".png",dpi=600)
    #plt.show()
    print ("Successfully saved contour in contour_%s.png"%(mzch))

def usage():
    print ("Usage: python plotcontour.py csvfile")
    print ("Assumes the column names are Phi Psi and Energy")
    print ("Usage: python plotcontour.py csvfile col1name col2name col3name")
    
if __name__ == "__main__":
    if len(sys.argv)==5:
        filename=sys.argv[1]
        xcol=sys.argv[2] 
        ycol=sys.argv[3]
        zcol=sys.argv[4]
    elif len(sys.argv)==2:
        filename=sys.argv[1]
        xcol='Phi' 
        ycol='Psi'
        zcol='Energy'
    else:
        usage()
        sys.exit()
        
    df=pd.read_csv(filename)
    print ("Assuming your csv file contains column headers as %s %s and %s\n"%(xcol,ycol,zcol))
    xi,yi,zi=getxyzcontour(df,xch=xcol,ych=ycol,zch=zcol)
    plotxyzcontour(xi,yi,zi,zch=zcol)
    sys.exit()
