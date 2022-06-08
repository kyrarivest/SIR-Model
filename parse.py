import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Open the file in the "read" mode
f=open("googleflu.csv","r")

# Read in header line
h=f.readline().split(",")
print(len(h))

my_data = np.genfromtxt('googleflu.csv', delimiter=',')
my_data = np.transpose(np.nan_to_num(my_data))
#print(my_data)

# Close the file
f.close()
plt.figure()
p3,=plt.plot(my_data[1][0:52],'-')
plt.legend([p3],["Data"])
plt.xlabel('t (Weeks)')
plt.ylabel('Population')
plt.show()
