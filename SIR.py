#Import nessecary packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

beta=0.0000333#define the beta coefficient from the dynamical system
gamma=0.059 #define the gamma coefficient from the dynamical system

#This function solves the set of DEs for any given point in time and any given population of susceptible, infectious, recovered people
def deriv(x,t):
  ifc=beta*x[0]*x[1] #calculate the number of infectious people (BSI in the equations)
  rec=gamma*x[1] #calcualte the number of recovered people (yI in the equation)
  return np.array([-ifc,ifc-rec,rec]) #return -BSI, BSI-yI, yI (basically returning all parts of the system you need for any point in time)

time=np.linspace(1,500,52) #define the timescale in which you are studying the system
xinit=np.array([2000,1000,0]) #Define the population of which you are studying (initally 100 susceptible, 1 infected, 0 recovered)
x=odeint(deriv,xinit,time) #use the function defined above to solve the differential equations


plt.figure() #create a blank plot
p0,=plt.plot(time,x[:,0]) #plot S(t) suceptible population
p1,=plt.plot(time,x[:,1]) #plot I(t) infectious population
p2,=plt.plot(time,x[:,2]) #plot R(t) recovered population
plt.legend([p0,p1,p2],["S(t)","I(t)","R(t)"]) #create the plot legend
plt.yticks(np.arange(0, 8000, 1000))
plt.xlabel('t (Weeks)') #add the x axis label
plt.ylabel('Population') #add the y axix label
plt.show() #show the plot ont he screen
