def add_num(lst):
    num = int(input("enter your numbers:"))
    lst.append(num)
    print("f{num} add successful no",lst)


def remove_num(lst):
    num = int(input("enter your numbers:"))
    if num in lst:
        lst.remove(num)
        print("f{num} remove successful no",lst)
    else:
        print("f{num} not found in list ",lst)

    
def show_lst(lst):
    print("current_list=",lst)

def find_largest_no(lst):
    if lst:
        print("largest_no",max(lst))
    else:
        print("list is empty.")

def menu():
    lst=[]
    while True:
        print("\n--- Menu ---")
        print("1. Add number")
        print("2. Remove number")
        print("3. Show list")
        print("4. Find largest number")
        print("5. Exit")


        choice=int(input("enter your choice no:"))

        if choice==1:
             add_num(lst)
        elif choice==2:
            remove_num(lst)
        elif choice==3:
            show_lst(lst)
        elif choice==4:
            find_largest_no(lst)
        elif choice == 5:
            print("Exiting program... Goodbye!")
            break
        else:
            print("envalid choice ! plz try again.")

menu()