grade_points = {
    "A+": 5,
    "A": 5,
    "A-":  4.5,
    "B+":  4,
    "B":   3.5,
    "B-":  3,
    "C+":  2.5,
    "C":   2,
    "D+":  1.5,
    "D":   1,
    "F":   0
}
MIN_SEMESTERS, MAX_SEMESTERS = 1, 10
MIN_MC, MAX_MC = 1, 20
sum_credits = sum_product = 0

def cap(results: list) -> float:
    """Return CAP based on list of grades"""
    global sum_credits, sum_product
    for grade, credits in results:
        sum_credits += credits
        sum_product += grade_points[grade] * credits
    return sum_product / sum_credits

if __name__ == "__main__":
    while True:
        try:
            semesters = int(input("Enter number of semesters: "))
        except ValueError:
            print(f"Please enter a valid number of semesters in the range {MIN_SEMESTERS}~{MAX_SEMESTERS}")
        else:
            if MIN_SEMESTERS <= semesters <= MAX_SEMESTERS:
                break
            else:
                print(f"Please enter a valid number of semesters in the range {MIN_SEMESTERS}~{MAX_SEMESTERS}")

    results = [[] for i in range(semesters)]
    for i in range(semesters):
        print(f"\nReading module grades for semester {i+1}...\nFor each module, type grade,MCs and press Enter. For eg.:\nB+,4\nIf MCs are omitted, it is assumed to be 4 MCs. Press Ctrl+C when done.")
        while True:
            try:
                result = input().split(',')
            except KeyboardInterrupt:
                break
            else:
                if result:
                    if len(result) == 2:
                        if result[0].upper() in grade_points:
                            try:
                                if MIN_MC <= int(result[1]) <= MAX_MC:
                                    results[i].append((result[0].upper(), int(result[1])))
                                else:
                                    print("Invalid MCs. Please enter a valid result in the form of grade,MCs:")
                            except ValueError:
                                print("Invalid MCs. Please enter a valid result in the form of grade,MCs:")
                        else:
                            print("Invalid grade. Please enter a valid result in the form of grade,MCs:")
                    elif len(result) == 1:
                        if result[0].upper() in grade_points:
                            results[i].append((result[0].upper(), 4))
                        else:
                            print("Invalid grade. Please enter a valid result in the form of grade,MCs:")
                    else:
                        print("Incorrect number of items. Please enter a valid result in the form of grade,MCs:")
                             
                else:
                    print("Empty input. Please enter a valid result in the form of grade,MCs:")
        print(f"CAP for semester {i+1}: {round(cap(results[i]), 2)}")



# results = [("B+", 6), ("B+", 4), ("A-", 4), ("B-", 2), ("B", 2)]
# print(cap(results))

# results += [("A", 6), ("B", 4), ("B+", 4), ("B", 4)]
# print(cap(results))

# results += [("B-", 4), ("C+", 4), ("A-", 4), ("B-", 4), ("B+", 4)]
# print(cap(results))

# results += [("B-", 4), ("B-", 4), ("B-", 4), ("D", 4), ("D", 4)]
# print(cap(results))