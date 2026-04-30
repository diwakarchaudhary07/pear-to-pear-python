n = 123

digits = list(str(n))

# Step 1: find first decreasing element from right
i = len(digits) - 2
while i >= 0 and digits[i] >= digits[i + 1]:
    i -= 1

# Step 2: find just greater element
j = len(digits) - 1
while digits[j] <= digits[i]:
    j -= 1

# Step 3: swap
digits[i], digits[j] = digits[j], digits[i]

# Step 4: reverse right part
digits[i+1:] = reversed(digits[i+1:])

print(int("".join(digits)))