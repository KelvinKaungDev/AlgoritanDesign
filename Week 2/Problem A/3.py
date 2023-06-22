# Modify the program step 3

x = []  # Global list to store the combination
k = 0  # Global variable for the number of 1's in the combination

def comb(i, count_ones):
    global x, k
    options = [0, 1]  # Options for selecting an item: 0 (not selected) and 1 (selected)
    n = len(x)  # Length of the combination

    if i >= n:
        # Base case: If we have assigned all items and count_ones is equal to k, print the combination
        if count_ones == k:
            print(x)
            return 1
        else:
            return 0
    else:
        count = 0
        for option in options:
            x[i] = option  # Assign the current option to the ith item
            count += comb(i + 1, count_ones + option)  # Recursively generate the rest of the combination and sum the results
        return count

# Test with n = 4 and k = 2
n = 3
k = 2
x = [0] * n  # Initialize the global list x with zeros
total_combinations = comb(0, 0)
print("Total combinations with exactly", k, "1's:", total_combinations)
