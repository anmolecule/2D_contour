# 2D_contour

The plotcontour script helps in plotting 2D contour maps given continous or discontinous input data.

For example:
You have a sheet containing energy values against Phi and Psi dihedral angle both varying from -180 to 180 at 30 degree interval. 
But some of the energy values are missing. Such discontinous data needs interpolation of missing values. This script automates the process. 

The input csv file should have following format:
|  Phi  |  Psi  |  Energy  |
| ----- | ----- | -------  |
| Phi_1 | Psi_1 |   E_1    |
| Phi_n | Psi_n |   E_n    |

Else, tweak the code before use.
