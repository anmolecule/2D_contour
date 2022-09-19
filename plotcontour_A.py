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

def getxyz(filename):
    base=os.path.basename(filename)
    tbase=base.split('-')[0].lower()
    es=df.columns.tolist()
    l=df.index.tolist()
    lt=list(map(lambda x:x.split(".")[0],l))
    x=[]
    y=[]
    ed={}
    for i in es:
        ed[i]=[]
    count1=0 
    count2=0 
    for i in range(-180,181,30):
        for j in range(-180,181,30):
#    for i in range(-180,181,60):
#        for j in range(-180,181,60):
            isign="M" if i < 0 else ""
            jsign="M" if j < 0 else ""
            #isign="-" if i < 0 else ""
            #jsign="-" if j < 0 else ""
            name=tbase+"_"+isign+str(abs(i))+"_"+jsign+str(abs(j))
            count1+=1 
            if name in lt: #ist(map(lambda x:x.split("."),l)):
               index=lt.index(name)
               x.append(i)
               y.append(j)
               for k in es:
                   ed[k].append(df[k].iloc[index])
               count2+=1 
               print (i,j)
    print (count1,count2)
    return (x,y,ed) 

x=df_sorted['Phi'].to_numpy() #phi=df['Phi'].to_list()
y=df_sorted['Psi'].to_numpy() #phi=df['Phi'].to_list()
z=df_sorted[sys.argv[2]].to_numpy()
#xi = np.linspace(-180, 180, 25)
#yi = np.linspace(-180, 180, 25)
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
#x,y,ed=getxyz(sys.argv[1])
#base=os.path.basename(sys.argv[1])
#tbase=base.split('-')[0].lower()
#x=np.array(x)
#y=np.array(y)
#fig, axs = plt.subplots(len(list(ed.keys())),1,figsize=(8,27)) #,dpi=300)
#xi = np.linspace(-180, 180, 25)
#yi = np.linspace(-180, 180, 25)
xi = np.linspace(-180, 180, 13)
yi = np.linspace(-180, 180, 13)
XI,YI=np.meshgrid(xi,yi)

for i,k in enumerate(list(ed.keys())):
   fig, axs = plt.subplots(figsize=(8,8)) #,dpi=300)
   z=np.array(ed[k])
   zi = griddata((x, y), z, (XI,YI), method='cubic')
   axs.contour(xi, yi, zi, levels=13, linewidths=0.5, colors='k')
   cntur = axs.contourf(xi, yi, zi, levels=13, cmap="RdBu_r")
   fig.colorbar(cntur, ax=axs)
   axs.set(xlim=(-180, 180), ylim=(-180, 120))
   axs.set_xticks(np.arange(-180,181,30))
   axs.set_yticks(np.arange(-180,121,30))
   axs.set_aspect('equal', adjustable='box')
   plt.title('Contour Plot for '+k) #(%d points, %d grid points)' %
   plt.tight_layout()
   nk=k.replace('/', '')
   print (nk)
   plt.savefig(tbase+"_contour_"+nk+".png",dpi=300)
   plt.show()
