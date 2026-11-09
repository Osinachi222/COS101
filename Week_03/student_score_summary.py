number_of_students = int(input("Enter number of students: "))
if number_of_students <= 0:
    print("Enter a number of students.")
    while number_of_students <= 0:
        number_of_students = int(input("Enter number of students: "))
        
else:
    for score in range(1, number_of_students + 1):
        score = float(input(f"Enter score for student {number_of_students}:"))

                
