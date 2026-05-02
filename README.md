# Wealth Distribution Simulator

Fair, random trades between equal people automatically create extreme inequality.

## How it works

- 1,000 people start with 1 coin each
- Pick two random people
- The poorer person bets 1% of their wealth
- Coin flip decides who wins
- Repeat 1 million times

## The result

Even though:
- Everyone started equal
- Every bet was 50/50
- No one had an advantage

**The top 1% ends up owning 30-50% of all wealth.**

## What the graphs show

- **Histogram:** Most people have very little, a few have a lot
- **Log-log plot:** Straight line = power law (same pattern as stock market crashes)
- **Initial vs final:** Green (equal start) → Red (unequal end)

## How to run

```bash
pip install numpy matplotlib
python wealth_simulation.py
