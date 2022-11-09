# =============================================================================
# Coding Reading Homework 1

# Reganne Russo
# =============================================================================

numbers = [34, 65, 23, 89, 44, 36, 55, 53, 73, 90]

numbers.sort()

del numbers[0]

del numbers[-1]

numerator = sum(numbers)

trim_mean = numerator / len(numbers)

print(f"The trimmed mean of the numbers given is {trim_mean}")
