import random

def main():
    e = 0
    f = 0
    g = 0
    h = 0
    
    # Getting 4 space-separated names from the user
    names = input("Enter the four players name : ").split()
    # Ensure we have at least 4 names to avoid errors
    while len(names) < 4:
        names += input("Please enter the remaining names: ").split()
    a, b, c, d = names[0], names[1], names[2], names[3]
    
    nums = [1000, 800, 500, 0]
    
    while True:
        # Shuffle the array
        random.shuffle(nums)
        
        if nums[0] == 1000 or nums[0] == 500:
            print(f"{a}: {nums[0]}")
        if nums[1] == 1000 or nums[1] == 500:
            print(f"{b}: {nums[1]}")
        if nums[2] == 1000 or nums[2] == 500:
            print(f"{c}: {nums[2]}")
        if nums[3] == 1000 or nums[3] == 500:
            print(f"{d}: {nums[3]}")

        # 0 index logic
        if nums[0] == 500:
            print(f"{a} tell us who is thief")
            new_guess = input()
            
            if new_guess == b:
                if nums[1] == 0:
                    print("you are right")
                elif nums[1] != 0:
                    print("you are wrong")
                    nums[0] = 0
                    if nums[2] == 0:
                        nums[2] = 500
                    elif nums[3] == 0:
                        nums[3] = 500
            elif new_guess == c:
                if nums[2] == 0:
                    print("you are right")
                elif nums[2] != 0:
                    print("you are wrong")
                    nums[0] = 0
                    if nums[1] == 0:
                        nums[1] = 500
                    elif nums[3] == 0:
                        nums[3] = 500
            elif new_guess == d:
                if nums[3] == 0:
                    print("you are right")
                elif nums[3] != 0:
                    print("you are wrong")
                    nums[0] = 0
                    if nums[1] == 0:
                        nums[1] = 500
                    elif nums[2] == 0:
                        nums[2] = 500
            else:
                print("you entered wrong name")

        # 1 index logic
        elif nums[1] == 500:
            print(f"{b} tell us who is thief")
            new_guess = input()
            
            if new_guess == a:
                if nums[0] == 0:
                    print("you are right")
                elif nums[0] != 0:
                    print("you are wrong")
                    nums[1] = 0
                    if nums[2] == 0:
                        nums[2] = 500
                    elif nums[3] == 0:
                        nums[3] = 500
            elif new_guess == c:
                if nums[2] == 0:
                    print("you are right")
                elif nums[2] != 0:
                    print("you are wrong")
                    nums[1] = 0
                    if nums[0] == 0:
                        nums[0] = 500
                    elif nums[3] == 0:
                        nums[3] = 500
            elif new_guess == d:
                if nums[3] == 0:
                    print("you are right")
                elif nums[3] != 0:
                    print("you are wrong")
                    nums[1] = 0
                    if nums[2] == 0:
                        nums[2] = 500
                    elif nums[0] == 0:
                        nums[0] = 500
            else:
                print("you entered wrong name")

        # 2 index logic
        elif nums[2] == 500:
            print(f"{c} tell us who is thief")
            new_guess = input()
            
            if new_guess == b:
                if nums[1] == 0:
                    print("you are right")
                elif nums[1] != 0:
                    print("you are wrong")
                    nums[2] = 0
                    if nums[0] == 0:
                        nums[0] = 500
                    elif nums[3] == 0:
                        nums[3] = 500
            elif new_guess == a:
                if nums[0] == 0:
                    print("you are right")
                elif nums[0] != 0:
                    print("you are wrong")
                    nums[2] = 0
                    if nums[1] == 0:
                        nums[1] = 500
                    elif nums[3] == 0:
                        nums[3] = 500
            elif new_guess == d:
                if nums[3] == 0:
                    print("you are right")
                elif nums[3] != 0:
                    print("you are wrong")
                    nums[2] = 0
                    if nums[1] == 0:
                        nums[1] = 500
                    elif nums[0] == 0:
                        nums[0] = 500
            else:
                print("you entered wrong name")

        # 3 index logic
        elif nums[3] == 500:
            print(f"{d} tell us who is thief")
            new_guess = input()
            
            if new_guess == b:
                if nums[1] == 0:
                    print("you are right")
                elif nums[1] != 0:
                    print("you are wrong")
                    nums[3] = 0
                    if nums[0] == 0:
                        nums[0] = 500
                    elif nums[2] == 0:
                        nums[2] = 500
            elif new_guess == a:
                if nums[0] == 0:
                    print("you are right")
                elif nums[0] != 0:
                    print("you are wrong")
                    nums[3] = 0
                    if nums[1] == 0:
                        nums[1] = 500
                    elif nums[2] == 0:
                        nums[2] = 500
            elif new_guess == c:
                if nums[2] == 0:
                    print("you are right")
                elif nums[2] != 0:
                    print("you are wrong")
                    nums[3] = 0
                    if nums[1] == 0:
                        nums[1] = 500
                    elif nums[0] == 0:
                        nums[0] = 500
            else:
                print("you entered wrong name")

        # Round results
        print(f"{a}: {nums[0]}\t{b}: {nums[1]}\t{c}: {nums[2]}\t{d}: {nums[3]}")
        e += nums[0]
        f += nums[1]
        g += nums[2]
        h += nums[3]

        if e == f or e == g or e == h or f == g or f == h or g == h:
            print("you have to play 1-2 round because totals are equal")

        choice = input("Do you want to play again? (Y/N): ")
        if choice.upper() != 'Y':
            break

    # Final Totals
    print(f"{a} total = {e}")
    print(f"{b} total = {f}")
    print(f"{c} total = {g}")
    print(f"{d} total = {h}")

    # Ranking System
    if e > f and e > g and e > h:
        print(f"FIRST RANK {a}")
        if f > g and f > h:
            print(f"SECOND RANK {b}")
            if g > h:
                print(f"THIRD RANK {c}\n FOURTH RANK {d}")
            else:
                print(f"THIRD RANK {d}\n FOURTH RANK {c}")
        elif g > f and g > h:
            print(f"SECOND RANK  {c}")
            if f > h:
                print(f"THIRD RANK {b}\n FOURTH RANK {d}")
            else:
                print(f"THIRD RANK {d}\n FOURTH RANK {b}")
        elif h > f and h > g:
            print(f"SECOND RANK {d}")
            if g > f:
                print(f"THIRD RANK {c}\n FOURTH RANK {b}")
            else:
                print(f"THIRD RANK {b}\n FOURTH RANK {c}")

    elif f > e and f > g and f > h:
        print(f"FIRST RANK {b}")
        if e > g and e > h:
            print(f"SECOND RANK {a}")
            if g > h:
                print(f"THIRD RANK {c}\nFOURTH RANK {d}")
            else:
                print(f"THIRD RANK {d}\n FOURTH RANK {c}")
        elif g > e and g > h:
            print(f"SECOND RANK {c}")
            if e > h:
                print(f"THIRD RANK {a}\n FOURTH RANK {d}")
            else:
                print(f"THIRD RANK {d}\n FOURTH RANK {a}")
        elif h > e and h > g:
            print(f"SECOND RANK {d}")
            if g > e:
                print(f"THIRD RANK {c}\n FOURTH RANK {a}")
            else:
                print(f"THIRD RANK {a}\n FOURTH RANK {c}")

    elif g > f and g > e and g > h:
        print(f"FIRST RANK {c}")
        if f > e and f > h:
            print(f"SECOND RANK  {b}")
            if e > h:
                print(f"THIRD RANK {a}\n FOURTH RANK {d}")
            else:
                print(f"THIRD RANK {d}\n FOURTH RANK {a}")
        elif e > f and e > h:
            print(f"SECOND RANK {a}")
            if f > h:
                print(f"THIRD RANK {b}\n FOURTH RANK {d}")
            else:
                print(f"THIRD RANK {d}\n FOURTH RANK {b}")
        elif h > f and h > e:
            print(f"SECOND RANK  {d}")
            if e > f:
                print(f"THIRD RANK {a}\n FOURTH RANK {b}")
            else:
                print(f"THIRD RANK {b}\n FOURTH RANK {a}")

    elif h > f and h > g and h > e:
        print(f"FIRST RANK  {d}")
        if e > f and e > g:
            print(f"SECOND RANK  {a}")
            if g > f:
                print(f"THIRD RANK {c}\n FOURTH RANK {b}")
            else:
                print(f"THIRD RANK {b}\n FOURTH RANK {c}")
        elif f > e and f > g:
            print(f"SECOND RANK  {b}")
            if e > g:
                print(f"THIRD RANK {a}\n FOURTH RANK {c}")
            else:
                print(f"THIRD RANK {c}\n FOURTH RANK {a}")
        elif g > f and g > e:
            print(f"SECOND RANK  {c}")
            if e > f:
                print(f"THIRD RANK {a}\n FOURTH RANK {b}")
            else:
                print(f"THIRD RANK {b}\n FOURTH RANK {a}")
                
    elif e == f or e == g or e == h or f == g or f == h or g == h:
        print("the totals are equal of someone")

if __name__ == "__main__":
    main()