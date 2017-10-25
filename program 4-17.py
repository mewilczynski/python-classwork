#this program averages test scores. It asks the user for the number of students and the number of test scores per student.

#get the number of students.
num_students = int(input('How many students do you have? '))

#get the number of test scores per student
num_test_scores = int(input('How many test scores per student? '))

#determine each student's average test score.
for student in range(num_students):
    #initialize an accumulator for test scores.
    total = 0.0
    #Get student's test scores.
    print('Student number', student + 1)
    print('-----------------')
    for testNum in range(num_test_scores):
        print('Test number', testNum + 1, end='')
        score = float(input(': '))
        #add the score to the accumulator.
        total += score
        average = total / num_test_scores

        #display the average
        print('The average for student number', student + 1, 'is:', average)
        print()
