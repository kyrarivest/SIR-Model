# SIR-Model
Runs a simulation of the SIR (Susceptible–Infected–Recovered) model. Also uses Google Flu data and compares it to the predictions of the SIR model.

There are three populations, the susceptibles S(t), the infecteds I(t) and the recovered R(t). The dynamics are given by the system of ordinary differential equations,

- $$\frac{dS}{dt} = -{\beta}SI$$
- $$\frac{dI}{dt} = -{\beta}SI-{\gamma}I$$
- $$\frac{dR}{dt} = -{\gamma}I$$

where β is the rate at which an infected person infects a susceptible and γ is the recovery rate of infected people.
