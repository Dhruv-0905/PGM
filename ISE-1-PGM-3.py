# Define the PMF
pmf = {
    0: 0.1,
    1: 0.3,
    2: 0.2,
    3: 0.3,
    4: 0.1
}

# Calculate Expected Value (Mean)
expected_value = sum(x * prob for x, prob in pmf.items())

# Calculate Expected Value of X squared
expected_value_squared = sum((x ** 2) * prob for x, prob in pmf.items())

# Calculate Variance
variance = expected_value_squared - (expected_value ** 2)

# Print Results
print(f"Expected Value (E[X]): {expected_value:.2f}")
print(f"Variance (Var[X]): {variance:.2f}")
