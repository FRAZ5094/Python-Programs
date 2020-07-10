import pandas as pd
import matplotlib.pyplot as plt

Primes=pd.read_csv("PrimeGenerator.csv",header=0)

plt.plot(Primes["Prime Number"],Primes["Time"])
plt.show()