def main():
def display_title():
        print("Welcome to the Grade Calculator")
    print("")
def get_letterGrade(averageEarned):

    if averageEarned >= 92 and averageEarned <= 100:
        return "A"
    elif averageEarned >= 88 and averageEarned < 92:
        return "B+"
    elif averageEarned >= 82 and averageEarned < 88:
        return "B"
    elif averageEarned >= 78 and averageEarned < 82:
        return "C"
    elif averageEarned >= 70 and averageEarned < 78:
        return "C+"
    elif averageEarned >= 60 and averageEarned < 68:
        return "D"
    else:
        return

    def get_totalPoints():


try:
        studentScore = float(input("Enter the total score(0-1000) : "))
except:
        print("You must enter integer value >=0 and <=1000. Try Again")
        print("")
        continue

if 1000 < studentScore or 0 > studentScore:
            print ("You must enter integer value >=0 and <=1000. Try Again")
            print ("")
            continue

            return studentScore

xif __name__ == "__main__":
    main()









