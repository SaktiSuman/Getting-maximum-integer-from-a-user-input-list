student_scores = input("Enter a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
max = 0
for score in student_scores:
    if score > max:
        max = score
print("The maximum score in the class is: ",max)