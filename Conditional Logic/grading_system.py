# This program is for finding grading system ..

print('Type Your name: ')
name = input()

print('Type your marks: ')
marks = int(input())
grade = ''

if marks >= 80:
    grade = 'A+'

elif marks >= 70:
    grade = 'A'

elif marks >= 60:
    grade = 'A-'

elif marks >= 50:
    grade = 'B'

elif marks >= 40:
    grade = 'C'

elif marks >= 33:
    grade = 'D'

else:
    grade = 'F'

print("Hi "+name+", you got "+grade)
print('Thank You\n')
