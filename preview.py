#Data Structures and Algorithms in python
#Goodrich book

#Preview of python program

print('Welcome to the GPA calculator')
print('Please enter all your letter grades. one per line')
print('Enter a blank line to designate the end')

#map from letter grade to point value
points= { 'A+' : 4.0, 'A':4.0, 'A-' :3.67, 'B+' :3.33, 'B' :3.0, 'B-':2.67, 'C+':2.33, 'C' :2.0, 'C-' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}

num_courses = 0
total_points = 0

#boolean value which defines if process is done or not
done = False

#while the process is still going:
while not done:
    grade = input()  #read line from user
    if grade == '':  #empty line was entered
        done = True  #end process
    elif grade not in points:   #unrecognized grade entered
        print('Unknown grade {0} being ignored'.format(grade))
    else:
        num_courses+=1 #num_courses
        total_points+= points[grade] #sum of each point corresponding to the grade
    if num_courses > 0:   #avoid division by zero
        print('Your GPA is {0: .2}'.format(total_points/num_courses))
