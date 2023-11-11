# Initialize an empty list 't' to store user-input numbers
t = []

# Collect user input for nine numbers and add them to the list 't'
for i in range(0, 9):
    n = float(input("Type the number: "))
    t.append(n)

# Initialize variables to calculate the maximum sum and its starting index
s = t[0] + t[1] + t[2] + t[3]
u = 0

# Iterate through subarrays of four consecutive numbers and find the one with the maximum sum
for i in range(1, 6):
    # Calculate the sum of the current subarray of four consecutive numbers
    k = t[i] + t[i + 1] + t[i + 2] + t[i + 3]
    
    # Check if the current sum 'k' is greater than the current maximum sum 's'
    if k > s:
        # If so, update the maximum sum 's' and its starting index 'u'
        s = k
        u = i

# Print the result, indicating the subarray with the maximum sum and the sum itself
print("The maximum sum is [", t[u], ",", t[u + 1], ",", t[u + 2], ",", t[u + 3], "] with a sum of", s)
