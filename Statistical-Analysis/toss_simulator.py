import random
import matplotlib.pyplot as plt

"""
The function `toss_simulator` simulates coin tosses and plots the probability of getting heads over
a specified number of trials.

:param trials: The `trials` parameter in the `toss_simulator` function represents the number of
times a coin will be tossed in the simulation. In this case, the function is set to simulate 5000
coin tosses
"""

def toss_simulator(trials):
    head_count = 0
    probability = []
    for i in range(1, trials + 1):
        toss = random.choice([0, 1])
        if toss == 1:
            head_count += 1
        probability.append(head_count / i)
    print("Number of heads:", head_count)
    plt.plot(probability)
    plt.axhline(y=0.5, linestyle='--')
    plt.xlabel("Number of Trials")
    plt.ylabel("Probability of Heads")
    plt.title("Coin Toss Simulation")
    plt.show()
toss_simulator(5000) 