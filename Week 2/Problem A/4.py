# question no 5

x = []  # Global list to store the combination

def comb(i):
    global x
    options = [0, 1, 2]  # Options for selecting an item: 0, 1, or 2
    n = len(x)  # Length of the combination

    if i >= n:
        # Base case: If we have assigned all items, print the combination
        print(x)
        return 1
    else:
        count = 0
        for option in options:
            x[i] = option  # Assign the current option to the ith item
            count += comb(i + 1)  # Recursively generate the rest of the combination and sum the results
        return count

# Test with n = 4
n = 4
x = [0] * n  # Initialize the global list x with zeros
total_combinations = comb(0)
print("Total combinations:", total_combinations)
