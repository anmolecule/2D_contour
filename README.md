# 2D_contour

The plotcontour script helps in plotting 2D contour maps given continous or discontinous input data.

Usage:
`python plotcontour.py csvfile EnergyHeaderincsv`

For example:
You have a sheet containing energy values against Phi and Psi dihedral angle both varying from -180 to 180 at 30 degree interval. 
But some of the energy values are missing. Such discontinous data needs interpolation of missing values. This script automates the process. 
This script also sort the values internally, so don't worry about the order of the data. 

The input csv file should have following format (Check sample.csv):
|  Phi  |  Psi  |  Energy  |
| ----- | ----- | -------  |
| Phi_1 | Psi_1 |   E_1    |
| Phi_n | Psi_n |   E_n    |

Else, tweak the code before use.

Expected Output:

![alt text](https://github.com/anmolecule/2D_contour/blob/main/contour_Energy.png?raw=true)

## Additional Information

You can utilize creategeoms.inp to generate scan coordinates about two adjacent dihedral. 
If you can modify the script, you can also use it for bond and angle scans.
Once you have individual scan structures, you can create Psi4 input file using template.py
After running QM calculations, you can tabulate your results in form of csv file and use
plotcontour.py for plotting.
