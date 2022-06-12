# SIR-Model
Runs a simulation of the SIR (Susceptible–Infected–Recovered) model. Also uses Google Flu data and compares it to the predictions of the SIR model.

There are three populations, the susceptibles S(t), the infecteds I(t) and the recovered R(t). The dynamics are given by the system of ordinary differential equations,

$$\frac{dS}{dt} = -{\beta}SI$$
$$\frac{dI}{dt} = -{\beta}SI-{\gamma}I$$
$$\frac{dR}{dt} = -{\gamma}I$$

where β is the rate at which an infected person infects a susceptible and γ is the recovery rate of infected people.

### Deriv Function
The deriv function encodes the SIR model dynamics. For a given input array x with three elements corresponding to S, I, and R, the function calculates dS/dt, dI/dt, and dR/dt. The odeint function takes three arguments: the time array that provides a list of timepoints at which to calculate the solution, the xinit array that provides the initial values of the three variables, and a reference to the deriv function.


### Google flu Data
It is aggregated on a weekly basis. The matrix has 53 columns listed by state, with the columns corresponding to Date, United States, Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, District of Columbia, Florida, . . . , Wisconsin, Wyoming. Hence the first column is the “Date”, the second column is the United States, and Massachusetts is column
number 24. This program attempts to fit the model to this data.
