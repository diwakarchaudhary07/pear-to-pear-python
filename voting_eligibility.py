# Voting Eligibility Checker


def check_voting_eligibility():
    age = int(input("Enter your age: "))
    residence = input("enter your residence :")

    if age >= 18 and residence == "indian":
        print("yes ! you are voter.")
    else:
        print("soory ! you are not eligible for vote.")



check_voting_eligibility()
