def print_calendar(year, month):
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        days_in_month[1] = 29

    q = 1  
    m = month
    Y = year
    if m < 3:
        m += 12
        Y -= 1
    K = Y % 100
    J = Y // 100
    h = (q + (13*(m+1))//5 + K + K//4 + J//4 + 5*J) % 7
    
    start_day = (h + 5) % 7

    
    print("Mo Tu We Th Fr Sa Su")
    print("   " * start_day, end="")

    for d in range(1, days_in_month[month-1] + 1):
        print(f"{d:2}", end=" ")
        if (d + start_day) % 7 == 0:
            print()


print_calendar(2026, 3)