import numpy as np
import matplotlib.pyplot as plt

print("Wealth Distribution Simulator")
print("Starting with 1000 people, each with 1 unit of wealth")
print("Running 1 million random transactions...")

# Initialize: 1000 people, each with 1 unit of wealth
n_people = 1000
wealth = np.ones(n_people)
initial_wealth = wealth.copy()

# Run transactions
n_transactions = 1_000_000
bet_fraction = 0.05  # Bet 1% of the poorer person's wealth

for i in range(n_transactions):
    # Pick two random people
    a, b = np.random.choice(n_people, 2, replace=False)
    
    # Determine who is poorer (they set the bet size)
    if wealth[a] < wealth[b]:
        poorer, richer = a, b
    else:
        poorer, richer = b, a
    
    # Bet amount is 1% of poorer person's wealth
    bet = wealth[poorer] * bet_fraction
    
    # Coin flip: 50/50 chance who wins
    if np.random.random() < 0.5:
        # Poorer wins
        wealth[poorer] += bet
        wealth[richer] -= bet
    else:
        # Richer wins
        wealth[poorer] -= bet
        wealth[richer] += bet
    
    # Safety check: no negative wealth
    wealth = np.maximum(wealth, 0)

print(f"\n--- Results after {n_transactions:,} transactions ---")
print(f"Total wealth (should be {n_people}): {wealth.sum():.1f}")
print(f"Wealthiest person: {wealth.max():.1f} units")
print(f"Poorest person: {wealth.min():.1f} units")
print(f"Top 1% own: {np.sum(np.sort(wealth)[-10:]) / wealth.sum() * 100:.1f}%")
print(f"Bottom 50% own: {np.sum(np.sort(wealth)[:500]) / wealth.sum() * 100:.1f}%")

# Plot results
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(wealth, bins=50, color='steelblue', edgecolor='black')
plt.xlabel("Wealth")
plt.ylabel("Number of People")
plt.title(f"Wealth Distribution After {n_transactions:,} Trades")
plt.yscale('log')
plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
# Sort wealth and plot on log-log scale
sorted_wealth = np.sort(wealth)[::-1]  # Descending order
rank = np.arange(1, n_people + 1)
plt.loglog(rank, sorted_wealth, 'bo', markersize=3, alpha=0.5)
plt.xlabel("Rank (1 = richest)")
plt.ylabel("Wealth")
plt.title("Rank-Size Plot (Power Law = Straight Line)")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Compare with initial
plt.figure(figsize=(6, 5))
plt.hist(initial_wealth, bins=20, alpha=0.5, label='Initial (all equal)', color='green')
plt.hist(wealth, bins=50, alpha=0.5, label='After trades', color='red')
plt.xlabel("Wealth")
plt.ylabel("Number of People")
plt.title("Initial vs Final Wealth Distribution")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

print("\n✅ Simulation complete!")
print("Notice: Everyone started equal and every bet was fair.")
print("Yet extreme inequality emerged automatically.")
