import numpy as np
import matplotlib.pyplot as plt
from oppgave_b_utdelt import formel

#1.0 avstand mellom verdiene
x = (np.arange(-10,10))
y = []
for i in x:
    y.append(formel(i))

plt.plot(x,y)
plt.show()

#0.5 avstand mellom verdiene
x = (np.arange(-10,10,0.5))
y = []
for i in x:
    y.append(formel(i))

plt.plot(x,y)
plt.show()