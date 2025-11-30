import random
from datetime import date, timedelta, datetime


class Register_for_uni:

    def __init__(self):
        self.w1 = []
        self.display_menu()

    def display_menu(self):
        while True:
            print()
            # function that displays menu
            print(f'You may select one of the following:\n'
                  f'                1) Add student\n'
                  f'                2) Search student\n'
                  f'                3) Search course\n'
                  f'                4) Add course completion\n'
                  f"                5) Show student's record\n"
                  f'                0) Exit\n'
                  f'What is your selection?')
            s1 = input()  # user enters his selection
            if s1 == '1':
                self.add_student()
            elif s1 == '2':
                self.search_student()
            elif s1 == '3':
                self.search_course()
            elif s1 == '4':
                self.add_course_completion()
            elif s1 == '5':
                self.show_students_record()
            elif s1 == '0':
                break
            else:
                # if smth else was entered by the user
                print('Please enter a number between 0 and 5')

    def add_student(self):
        # function that adds student to the student.txt

        q1 = {
            1: 'Enter the first name of the student:',
            2: 'Enter the last name of the student:',
            3: 'Enter the middle name (just press enter and '
               'leave it black if no middle name) of the student:',
            4: "Select student's major:\n"
               '                CE: Computational Engineering\n'
               '                EE: Electrical Engineering\n'
               '                ET: Energy Technology\n'
               '                ME: Mechanical Engineering\n'
               '                SE: Software Engineering\n'
               'What is your selection?'
        }  # all questions that should be asked from user

        w1 = [self.generating_student_id()]  # list where the results of questions will be stored
        # initially contain randomly created ID for future student

        count = 1  # number of current question
        while count <= len(q1):
            r = input(q1[count] + '\n')
            check = self.check_of_input_student(r, count)
            if check == 1:
                w1.append(r)
                count += 1
            elif check == 0:
                print(f'Names should contain only letters and '
                      f'start with capital letter.')
            else:
                print(f'Please enter the exact abbreviation of the major')

        w1.insert(4, w1[2].lower() + '.' + w1[1].lower() + '@lut.fi')  # adding students email

        today = date.today()
        year_today = datetime.strftime(today, "%Y")  # adding current year
        w1.insert(5, year_today)

        f1 = open('students.txt', 'a')
        result = ''
        for i in w1: result = result + ',' + i
        f1.write(result[1::] + '\n')  # writing the resulted data to the student.txt
        # result[1::] starts with the 1st element, because string "result" starts with ,
        f1.close()
        print(f'Student added successfully!')

    def search_student(self):
        while True:
            r = input('Give at least 3 charecters of the '
                      'students first, middle or last name:\n').lower()

            if (len(r) < 3) or (not r.isalpha()):
                print('Error!!!\n'
                      'Please check that at least three characters were entered correctly.\n')  # checking if correct input was given

            else:
                f1 = open('students.txt').readlines()
                matching_is_printed = False  # False if "Matching students:" is not printed yet / True if "Matching
                # students:" has been already printed

                found_matching = False  # False if nothing was printed / True if matching was find

                for i in f1:
                    student_info = i.split(',')

                    if (r in student_info[1].lower()) or (r in student_info[2].lower()) or (r in student_info[3].lower()):
                        found_matching = True

                        if matching_is_printed == False:
                            print('Matching students:')
                            matching_is_printed = True

                        print(f'ID: {student_info[0]}, {student_info[1]}, '
                              f'{student_info[2]} {student_info[3]}')

                if not found_matching:
                    print('No matching students.')
                    break
                break

    def search_course(self):
        while True:
            r = input('Give at least 3 characters of the '
                      'course or the teacher:\n').lower()

            if (len(r) < 3) or (not r.isalpha()):
                print('Error!!!\n'
                      'Please check that at least three characters were entered correctly.\n')  # checking if correct input was given
            else:
                f1 = open('courses.txt').readlines()
                course_found = False

                for i in f1:
                    course_info = i.strip().split(',')

                    for x in range(1, len(course_info)):  # loop starts with 1 because it doesn't search the matches in course ID
                        if x != 2:   # also doesn't search the matches among credits
                            if r in course_info[x].lower():
                                course_found = True                     # checking for the matching course

                                result = ''
                                for i in course_info[3::]:
                                    result = result + ', ' + i

                                print(f'ID: {course_info[0]}, Name: {course_info[1]}, '
                                      f'Teacher (s): {result[2::]}')

                if course_found == False:
                    print('No matching courses.')  # if no courses were found
                else:
                    break

    def add_course_completion(self, match=False):
        q1 = {
            1: 'Give the course ID:',
            2: 'Give the student ID:',
            3: 'Give the grade:',
            4: 'Enter a date (YYYY-MM-DD)'
        }  # all questions that should be asked from user

        w1 = []  # list where the results of questions will be stored

        count = 1  # number of current question

        while count <= len(q1):

            r = input(q1[count] + '\n')    # current question that should be asked
            check = self.check_of_input_course(r, count)
            match = False
            if check == 1:

                if count == 4:
                    w1.insert(2, r)   # date should added not in the last, but on the 2nd position of the list
                else:
                    w1.append(r)
                count += 1
            elif check == 2:
                match = True
                break

        if match == False:
            self.retaking_course(w1)   # checking if the course was taken earlier


    def show_students_record(self):
        q1 = {
            1: 'Student ID:',
            2: 'Name:',
            3: 'Starting year:',
            4: 'Major:',
            5: 'Email:'
        }
        q2 = [
            ['Course ID:', ''],
            ['Name:', ''],
            ['Credits:', ''],
            ['Date:', ''],
            ['Teacher (s):', ''],
            ['grade:', 0]
        ]
        list_of_majors = [
            ('CE', 'Computational Engineering'),
            ('EE', 'Electrical Engineering'),
            ('ET', 'Energy Technology'),
            ('ME', 'Mechanical Engineering'),
            ('SE', 'Software Engineering')
        ]

        r = input('Give the student ID:\n')
        print()
        f1 = open('students.txt').readlines()
        found_student = False
        student_ID = ''

        for i in f1:
            if r == i[:5]:
                found_student = True
                student_info = i.strip().split(',')
                student_ID = student_info[0]
                print(f'{q1[1]} {student_info[0]}')
                print(f'{q1[2]} {student_info[1]}, '
                      f'{student_info[2]} {student_info[3]}')
                print(f'{q1[3]} {student_info[5]}')

                for x in range(4):
                    if student_info[6] == list_of_majors[x][0]:
                        print(f'{q1[4]} {list_of_majors[x][1]}')
                        break

                print(f'{q1[5]} {student_info[4]}')
                break

        if found_student == False:
            print('Student not found. Try again.')
            return

        try:
            print('\nPassed courses:\n')

            w1 = open('passed.txt').readlines()
            f1 = []
            for i in w1:
                f1.append(i.strip().split(','))

            def sort(item):
                return datetime.strptime(item[2], "%Y-%m-%d")

            f1.sort(key=sort)

            f2 = open('courses.txt').readlines()
            total_credits = 0
            grade = 0
            kol_of_courses = 0

            for passed_info in f1:
                if passed_info[1] == student_ID:

                    teacher = []
                    grade += int(passed_info[-1])
                    kol_of_courses += 1

                    for x in f2:
                        course_info = x.strip().split(',')
                        if course_info[0] == passed_info[0]:
                            q2[1][1] = course_info[1]
                            q2[2][1] = course_info[2]
                            total_credits += int(course_info[2])
                            teacher = course_info[3::]
                            break

                    q2[0][1] = passed_info[0]
                    q2[3][1] = passed_info[2]

                    result = ''
                    for i in teacher: result = result + ', ' + i

                    print(f'{q2[0][0]} {q2[0][1]}, {q2[1][0]} {q2[1][1]}, '
                          f'{q2[2][0]} {q2[2][1]}\n{q2[3][0]} {q2[3][1]}, '
                          f'{q2[4][0]} {result[2::]}, {q2[5][0]} {passed_info[-1]}\n')
            print(f'Total credits: {total_credits}, average grade: {round(grade / kol_of_courses, 2)}')

        except:
            print("None of them are found.\n")

    def generating_student_id(self):
        # function that generates student's ID
        f = open('students.txt').readlines()
        uniqueness_check = True
        while True:
            number = str(random.randint(10000, 99999))  # for 5-digit id
            for i in f:
                if i[:5] == number:
                    uniqueness_check = False
            if uniqueness_check:
                return number

    def check_of_input_course(self, r, count):
        if count == 1:
            f1 = open('courses.txt').readlines()
            for i in f1:
                if r == i[:5]:
                    return 1
            print('Invalid course ID')
            return 0
        elif count == 2:
            f1 = open('students.txt').readlines()
            for i in f1:
                if r.lower() == i[:5]:
                    return 1
            print('Student not found. Try again.')
            return 0
        elif count == 3:
            if r.isdigit():
                if 0 < int(r) < 6:
                    return 1
                print('Grade is not a correct grade.')
                return 0
        elif count == 4:
            try:
                user_date = datetime.strptime(r, "%Y-%m-%d").date()
                today = date.today()
                thirty_days_ago = today - timedelta(days=30)
                if user_date < thirty_days_ago:
                    print('Input date is older than 30 days. Contact "opinto"')
                    return 2
                elif user_date > today:
                    print('Input date is later than today. Try again!')
                    return 0
                print('Input date is valid.')
                return 1

            except ValueError:
                print('Invalid date format. Use YYYY-MM-DD. Try again!')

    def check_of_input_student(self, r, count):
        # function that checks if the user's inputted data for adding student was correct
        list_of_majors = ['CE', 'EE', 'ET', 'ME', 'SE']
        if count == 3 and len(r) == 0:
            return 1
        if count == 4:
            if r not in list_of_majors:
                return 2
        if r.isalpha() and r[0].isupper():
            return 1
        return 0

    def retaking_course(self, w1):

        w2 = []
        new_data = True
        early_date = False
        f = open('passed.txt').readlines()

        for i in f:
            line = i.strip().split(',')

            if w1[0] == line[0] and w1[1] == line[1] and early_date == False:

                if int(w1[3]) > int(line[3]) and early_date == False:
                    # checking if the student got better grade
                    new_data = False

                    if w1[2] >= line[2]:  # checking if the retaken course has latter date
                        line[2], line[3] = w1[2], w1[3]
                        # list(line) changes its values to the more late date and better grade

                        result = ''
                        for x in line: result = result + ',' + x

                        w2.append((result[1::] + '\n'))

                    else:
                        print(f'However the same course, but taken later has been found! '
                              f'The date of last attempt - {line[2]}!')
                        w2.append(i)
                        early_date = True

                        # s1 = input(f'Press ENTER to return to the main lobby / '
                        #            f'Write anything else to try one more time')
                        # if s1 == '':
                        #     return
                        # else:
                        #     self.add_course_completion(True)
                else:
                    new_data = False
                    w2.append(i)

            else:
                w2.append(i)

        if new_data == True:
            result = ''
            for i in w1: result = result + ',' + i
            w2.append((result[1::] + '\n'))

        f1 = open('passed.txt', 'w')
        for i in w2:
            f1.write(i)
        f1.close()
        if early_date == False:
            print('Record added!')


if __name__ == "__main__":
    Register_for_uni()



# instead of this algorithm:
# result = ''
# for i in w1: result = result + ',' + i
# everywhere could be used:
# ','.join(w1)     but Code Grade marks it as untaught structure.


