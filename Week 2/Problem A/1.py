x = []  # Global list to store the combination

def comb(i):
    print("i,", i)
    global x
    print(x)
    options = [0, 1]  # Options for selecting an item: 0 (not selected) and 1 (selected)
    n = len(x)  # Length of the combination
    print(n)
    if i >= n:
        # Base case: If we have assigned all items, print the combination
        print("hello,", x)
    else:
        for option in options:
            x[i] = option  # Assign the current option to the ith item
            comb(i + 1)  # Recursively generate the rest of the combination

# Test with n = 3
n = 3
x = [0] * n  # Initialize the global list x with zeros
comb(0)