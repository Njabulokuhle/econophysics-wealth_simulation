import time
import numpy as np

start = time.time()
wealth = np.ones(1000)
for i in range(1_000_000):
    a, b = np.random.choice(1000, 2, replace=False)
    bet = min(wealth[a], wealth[b]) * 0.01
    if np.random.random() < 0.5:
        wealth[a] += bet
        wealth[b] -= bet
    else:
        wealth[a] -= bet
        wealth[b] += bet
end = time.time()

print(f"1 million trades took {end-start:.2f} seconds")