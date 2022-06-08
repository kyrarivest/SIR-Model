import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Open the file in the "read" mode
f=open("googleflu.csv","r")
# Read in header line
h=f.readline().split(",")
# Initialize 53 empty lists
s=[]
for i in range(53):
    s.append([])
# Loop over the remaining lines
for l in f:
# Create a list by separating the line at commas
    d=l.split(",")
    for i,val in enumerate(d):
        if val=='' or val.isspace():
            d[i] = np.NaN
        # Store the 53 entries in the line to each relevant list
    for i in range(53):
        if i==0:
            s[i].append(d[i])
        else:
            s[i].append(float(d[i]))

# Close the file
f.close()


#beta (infection rate ), and gamma (recovery rates) are assigned
beta=0.00004
gamma=0.07

# defining derivation function

def deriv(x,t):
    ifc=beta*x[0]*x[1]
    rec=gamma*x[1]
    return np.array([-ifc,ifc-rec,rec])
time=np.linspace(0,50,1000)
xinit=np.array([12500,900,0])
x=odeint(deriv,xinit,time)
plt.figure() # Initiaizes figure

p1,=plt.plot(time,x[:,1])

p3,=plt.plot(s[1][0:52],'-')
plt.legend([p1,p3],["I(t)","Googleflu"])
plt.xlabel('t (Weeks)')
plt.ylabel('Population')
plt.show()
