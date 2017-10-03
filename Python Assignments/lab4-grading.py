

grade = input('What grade did you get, in numbers? ')
grade = int(grade)

if grade >= 90:
    print('A')
elif grade >= 80:
    print('B')
elif grade >= 70:
    print('C')
elif grade >= 60:
    print('D')
elif grade < 60:
    print('F')
