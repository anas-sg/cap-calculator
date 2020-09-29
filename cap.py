from glob import glob
from argparse import ArgumentParser

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
    if not results:
        return 0
    for grade, credits in results:
        sum_credits += credits
        sum_product += grade_points[grade] * credits
    return sum_product / sum_credits

def read_input(file: str=None) -> list:
    """Read from standard input/CSV into list"""
    results = []
    if not file:
        print("For each module, type grade,MCs (eg. B+,4) and ENTER.\nIf MCs are absent, it will be assumed to be 4.\nPress Ctrl+C when done:")
    else:
        try:
            csv = open(file)
        except OSError:
            raise OSError(f"{file} not found")
    while True:
        try:
            result = csv.readline()[:-1].split(",") if file else input().split(",")            
            if result[0]:
                print(result)
                if len(result) == 2:
                    if result[0].upper() in grade_points:
                        if not result[1]:
                            results.append((result[0].upper(), 4))
                        else:
                            try:
                                if MIN_MC <= int(result[1]) <= MAX_MC:
                                    results.append((result[0].upper(), int(result[1])))
                                else:
                                    print("Invalid MCs. Please enter grade,MCs:")
                            except ValueError:
                                print("Invalid MCs. Please enter grade,MCs:")
                    else:
                        print("Invalid letter grade. Please enter grade,MCs:")
                elif len(result) == 1:
                    if result[0].upper() in grade_points:
                        results.append((result[0].upper(), 4))
                    else:
                        print("Invalid letter grade. Please enter grade,MCs:")
                else:
                    print("Incorrect number of items. Please enter grade,MCs:")                     
            else:
                if file:
                    csv.close()
                    break
        except KeyboardInterrupt:
            break
    return results
        

if __name__ == "__main__":
    my_parser = ArgumentParser(description='Calculate and display the CAP of a student from the grades input.')
    my_parser.version = '1.0'
    my_parser.add_argument('-f', '--file', nargs='?', const='nofile', default=None, help='read grades from CSV file', action='store')
    file_arg = my_parser.parse_args().file
    if not file_arg:                            
        print(f"\rCAP: {round(cap(read_input()), 2)}")
    elif file_arg == 'nofile':
        files = glob("*.csv")
        if not files:
            print("No CSV files found in current directory.")
        elif len(files) == 1:
            response = input(f"{files[0]} found; y/n to proceed: ")
            if response[0].lower() == "y":
                print(f"CAP: {round(cap(read_input(files[0])), 2)}")
            else:
                print("No CSV file provided.")
        else:
            print("Found the following .csv files in current directory:")
            for i, file in enumerate(files):
                print(f"{i}) {file}")
            option = int("Enter index number of file: ")
            if 0 <= option < len(files):
                print(f"CAP: {round(cap(read_input(files[option])), 2)}")
            else:
                raise ValueError("Index is out of range.")
    else:        
        print(f"CAP: {round(cap(read_input(file_arg)), 2)}")
        



# results = [("B+", 6), ("B+", 4), ("A-", 4), ("B-", 2), ("B", 2)]
# print(cap(results))

# results += [("A", 6), ("B", 4), ("B+", 4), ("B", 4)]
# print(cap(results))

# results += [("B-", 4), ("C+", 4), ("A-", 4), ("B-", 4), ("B+", 4)]
# print(cap(results))

# results += [("B-", 4), ("B-", 4), ("B-", 4), ("D", 4), ("D", 4)]
# print(cap(results))