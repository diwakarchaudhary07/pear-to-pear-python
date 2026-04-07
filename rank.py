# 4 integer input lena
a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))
d = int(input("Number 4: "))

# Rank nikalne ke liye if-else conditions
# a ke liye rank
if (a >= b and a >= c and a >= d):
    rank_a = 1
elif (a <= b and a <= c and a <= d):
    rank_a = 4
elif ( (a >= b and a >= c) or (a >= b and a >= d) or (a >= c and a >= d) ):
    rank_a = 2
else:
    rank_a = 3

# b ke liye rank
if (b >= a and b >= c and b >= d):
    rank_b = 1
elif (b <= a and b <= c and b <= d):
    rank_b = 4
elif ( (b >= a and b >= c) or (b >= a and b >= d) or (b >= c and b >= d) ):
    rank_b = 2
else:
    rank_b = 3

# c ke liye rank
if (c >= a and c >= b and c >= d):
    rank_c = 1
elif (c <= a and c <= b and c <= d):
    rank_c = 4
elif ( (c >= a and c >= b) or (c >= a and c >= d) or (c >= b and c >= d) ):
    rank_c = 2
else:
    rank_c = 3

# d ke liye rank
if (d >= a and d >= b and d >= c):
    rank_d = 1
elif (d <= a and d <= b and d <= c):
    rank_d = 4
elif ( (d >= a and d >= b) or (d >= a and d >= c) or (d >= b and d >= c) ):
    rank_d = 2
else:
    rank_d = 3

# Output
print("\ninput_num Number Rank")
print("  number 1="   ,a,     "\t", rank_a)
print("  number 2="   ,b,     "\t", rank_b)
print("  number 3="   ,c,     "\t", rank_c)
print("  number 4="   ,d,     "\t", rank_d)
