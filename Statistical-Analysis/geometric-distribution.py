import numpy as np 
import matplotlib.pyplot as plt 
p = 0.3
k = np.arange(1,16)
probability = p*(1-p)**(k-1)
plt.bar(k,probability,color='teal',edgecolor='black',alpha=1)
plt.plot(k,probability,color='coral')
plt.title(f'Geometric Distribution')
plt.xlabel('Number of tosses')
plt.ylabel('Probability')
plt.grid()
plt.show()