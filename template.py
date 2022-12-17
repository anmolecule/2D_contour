import os,sys
#print ("Usage: Takes in pdb or xyz file format. Prints out Psi4 input.")

f=open(sys.argv[1],'r')
fr=f.readlines()
coor=''
if sys.argv[1].split('.')[-1]=='pdb':
    for line in fr:
        if line.startswith("ATOM"):
           field=line.split()
           coor=coor+" ".join([field[2],field[5],field[6],field[7],"\n"])

elif sys.argv[1].split('.')[-1]=='xyz':
    for line in fr[2:]:
        field=line.split()
        if len(field)!=4: continue
        coor=coor+" ".join([field[0],field[1],field[2],field[3],"\n"])

temp="""
molecule {
%s
}

set basis 6-31+G(d)

set optking {
  frozen_dihedral = ("
    5 7 9 15 
    7 9 15 17 
  ")
}
optimize('mp2')
"""
print (temp%(coor))

 #   5 7 9 24 
 #   7 9 24 26 
