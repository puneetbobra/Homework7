import pandas as pd

scores = pd.read_csv('scores.csv', header=0, index_col = 0)

#Assigning letter grade point based on the score
def assign_point(score):
    """This function assings letter grade point based on the score obtained by the student"""
    if score >= 90:
        point = 4.00
    elif score >= 80:
        point = 3.00
    elif score >= 70:
        point = 2.00
    elif score >= 60:
        point = 1.00
    else: 
        point = 0.00
    
    return point


#calculate GPA of each student and class
#create variables
total_gpa = 0.0
total_rows = len(scores.index)
total_columns = len(scores.columns)
student_gpa = 0.0

#read the student name and score, then assign the letter grade points 
for i in scores.columns:
    print(i, end = ' ')
    total = 0.0
    for j in scores[i]:
        point = assign_point(j)        
        total += point
        student_gpa = total / total_rows
    print(f'{(student_gpa):.3}')
    total_gpa += student_gpa

print(f'The class GPA is: {(total_gpa / total_columns):.3}')

#End