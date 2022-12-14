import os,sys
import pandas as pd
import numpy as np

def getxyz(filename):
    base=os.path.basename(filename)
    tbase=base.split('-')[0].lower()
    df=pd.read_csv(filename,index_col=0)
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

x,y,ed=getxyz(sys.argv[1])
base=os.path.basename(sys.argv[1])
tbase=base.split('-')[0].lower()
x=np.array(x)
y=np.array(y)
for i,k in enumerate(list(ed.keys())):
   fig, axs = plt.subplots(figsize=(8,8)) #,dpi=300)
   z=np.array(ed[k])
