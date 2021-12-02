# ages = [10, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# def get_user_age():
#     user_age = int(input('Please enter your age: '))
#     return user_age

# def is_valid_age(user_age):
#     found = False
#     for age in ages:
#         if user_age == age:
#             found = True
#             break
#     return found

# def run():
#     print('Age registered? : {}'.format(is_valid_age(get_user_age())))

# if __name__ == '__main__':
#     run()

# grades = [
#     ('Prince', 'A'), 
#     ('Abena', 'A'), 
#     ('Collins', 'B'), 
#     ('Julius', 'C'), 
#     ('Mills', 'F')
# ]

# def display_student_grades(student_grades):
#     sg = student_grades
#     for student_data in sg:
#         student_name, grade = student_data

#         print('Student | Grade\n--------------- \n{}\t| {}'.format(student_name, grade))

# display_student_grades(grades)

# points={'A+':4.0, 'A':4.0, 'A-':3.67, 'B+' :3.33,
#         'B' :3.0, 'B-' :2.67, 'C+' :2.33, 'C' :2.0,
#         'C' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0
#     }


# def compute_gpa(grades, points):
#     num_of_courses = 0
#     total_points = 0
#     for grade in grades:
#         if grade in points:
#             num_of_courses += 1
#             total_points += points[grade]
#     return total_points / num_of_courses



# my_grades = ['A+', 'B+', 'A', 'A-', 'B-', 'A+', 'A+', 'C', 'B+', 'A+']
# my_gpa = compute_gpa(my_grades, points)
# print(my_gpa)

# try:
#     with open('characters.txt', 'a', encoding='utf16') as char_file:
#         char_file.write('Character number | Character(Symbol)\n')
#         for i in range(60000):
#             char = chr(i)
#             if char == '\ud800':
#                 break
#             char_file.write('\t{}\t\t\t {}\n'.format(i, char)) #unicode_char))
# except Exception as e:
#     print(e)
import collections
def sum(values):
    if not isinstance(values, collections.Iterable):
        raise TypeError('Values must be iterable')
    total = 0
    for v in values:
        if not isinstance(v, (int, float)):
            raise TypeError('Values must be numeric')
        total += v
    return total

sum(5)