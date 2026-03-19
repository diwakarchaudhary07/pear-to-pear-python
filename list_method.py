# Python list methods demo

lst = [10, 5, 8]

lst.append(15)       # [10, 5, 8, 15]
lst.insert(1, 20)    # [10, 20, 5, 8, 15]
lst.extend([25, 30]) # [10, 20, 5, 8, 15, 25, 30]
lst.remove(5)        # [10, 20, 8, 15, 25, 30]
lst.pop()            # removes last → [10, 20, 8, 15, 25]
lst.sort()           # [8, 10, 15, 20, 25]
lst.reverse()        # [25, 20, 15, 10, 8]

print(lst)