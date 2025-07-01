import matplotlib.pyplot as plt

# Step 1: Set the list of numbers
numbers = list(range(1, 11))  # 1 to 10

# Step 2: Dictionary to store sum vs number of distinct pairs
sum_counts = {i: 0 for i in range(1, 21)}  # sum from 1 to 20

# Step 3: Find all distinct pairs (a < b) and count their sums
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        a, b = numbers[i], numbers[j]
        s = a + b
        if s <= 20:
            sum_counts[s] += 1

# Step 4: Extract data for plotting
sums = list(sum_counts.keys())
counts = list(sum_counts.values())

# Step 5: Plotting the pyramid
plt.figure(figsize=(10, 5))
plt.plot(sums, counts, marker='o', linestyle='-', color='blue')
plt.fill_between(sums, counts, color='skyblue', alpha=0.4)
plt.title("Sum vs Number of Distinct Pairs (from 1 to 10)")
plt.xlabel("Sum")
plt.ylabel("Number of Distinct Pairs")
plt.xticks(range(1, 21))
plt.yticks(range(0, max(counts)+1))
plt.grid(True)
plt.tight_layout()
plt.show()
