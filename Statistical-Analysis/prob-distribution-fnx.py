import matplotlib.pyplot as plt 
x = [0,1,2,3]
probability = [0.125,0.375,0.375,0.125]
plt.bar(x,probability,color='teal')
plt.xticks(x,['0 Head','1 Head','2 Heads','3 Heads'])
plt.title('Probability Distribution')
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.show()