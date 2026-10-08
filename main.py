# Array Score Processing Project

# Accept scores from the user
scores = list(map(int, input("Enter scores separated by spaces: ").split()))

# Calculate sum
total = sum(scores)

# Calculate average
average = total / len(scores)

# Find maximum score
maximum = max(scores)

# Find minimum score
minimum = min(scores)

# Display results
print("\n--- Score Results ---")
print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)