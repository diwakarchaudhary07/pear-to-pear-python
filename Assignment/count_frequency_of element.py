def count_frequency(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


list = [1, 2, 2, 3, 3, 3]
result = count_frequency(list)

for key, value in result.items():
    print(f"{key} → {value}")































































#      Count Frequency of Elements
# Write a function that counts how many times each element appears in a list.
# Example:
# Copy code

# Input: [1,2,2,3,3,3]
# Output:
# 1 → 1
# 2 → 2
# 3 → 3