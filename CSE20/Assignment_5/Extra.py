class Students:

    def __init__(self, students=[]):
        self.students = dict()
        for student in students:
            self.students[student.fetch_number()] = student

    def add_student(self, student):
        """ Add a student to the students dictionary.
            Return True if successful, else return False. """
        if student not in self.students:
            self.students[student] = student[1:]
            return True
        return False

    def add_students(self, students):
        """ Add list of students to the students dictionary. """
        for i in students:
            self.students[i] = i

    def fetch_students(self):
        """ Return the students dictionary. """
        return self.students

    def fetch_student(self, studentID):
        """ Return the student with this student number (ID). """
        for n, v in self.students.items():
            if v == studentID:
                return n

    def fetch_student_numbers(self):
        return list(self.students.keys())


class Student:

    def __init__(self, first_name='First_Name',
                 last_name='Last_Name',
                 student_number='0000'):
        self.first_name = first_name
        self.last_name = last_name
        self.student_number = student_number
        self.past_courses = []  # course numbers (IDs)
        self.current_courses = []  # course numbers (IDs)

    def fetch_name(self):
        """ Return the name of this student, (first_name, last_name). """
        return self.first_name, self.last_name

    def fetch_number(self):
        """ Return this students student number (ID). """
        return self.student_number

    def add_past_courses(self, course_IDs=None):
        """ Append this list of past course numbers (IDs)
            to the list of this student's past courses. """
        if course_IDs is None:
            course_IDs = []
        for c in course_IDs:
            self.past_courses.append(c)

    def add_current_courses(self, course_IDs=None):
        """ Append this list of current course numbers (IDs)
            to the list of this student's current courses. """
        if course_IDs is None:
            course_IDs = []
        for c in course_IDs:
            self.current_courses.append(c)

    def add_course(self, courseID):
        """ Append this course number (ID) to the list of current_courses. """
        self.current_courses.append(courseID)
        pass

    def fetch_past_courses(self):
        return self.past_courses

    def fetch_current_courses(self):
        return self.current_courses

    def drop_current_course(self, courseID):
        """ Drop this course number (ID) from the list of current_courses.
            Return True if successful, else return False. """
        if courseID in self.current_courses:
            self.current_courses.pop(courseID)
            return True
        return False

    def drop_all_current_courses(self):
        """ Empty the current_courses list. """
        self.current_courses = []

    def current_to_past_courses(self):
        """ Move all current course numbers (IDs) to the list of past_courses. """
        self.past_courses += self.current_courses
        self.drop_all_current_courses()


class Courses:

    def __init__(self, courses=None):
        if courses is None:
            courses = []
        self.courses = dict()
        # This dictionary has course numbers (IDs) for its keys.
        for course in courses:
            self.courses[course.fetch_course_number()] = course

    def add_course(self, course):
        """ Add this course to the courses dictionary.
            Return True if successful, else return False. """
        if course.fetch_course_number() in self.courses:
            return False
        else:
            self.courses.update({course.fetch_course_number(): course})
            return True

    def add_courses(self, courses):
        for c in courses:
            self.add_course(c)

    def fetch_course_numbers(self):
        """ Return a list of course numbers (IDs). """
        return list(self.courses.keys())

    def fetch_courses(self):
        """ Return the dictionary of courses. """
        return self.courses

    def fetch_course(self, courseID):
        """ Fetch the course with this course number (ID). """
        for n, v in self.courses.items():
            if n == courseID:
                return v


class Course:
    def __init__(self, course_name='CS 000',
                 course_number='0000',
                 semester='Fall',
                 year=2019,
                 enrolled_students=[]):
        ''' The enrolled_students argument is a list of student numbers (Ids) '''

        self.course_name = course_name
        self.course_number = course_number
        self.semester = semester
        self.year = year
        # This dictionary has student numbers (IDs) as keys,
        # and the student's grade as the value.
        self.enrolled_students = {student: 'NG' for student in enrolled_students}

    def fetch_course_name(self):
        """ Return this course name. """
        return self.course_name

    def fetch_course_number(self):
        """ Return this course number. """
        return self.course_number

    def fetch_enrolled_studentIDs(self):
        """ Return a list of enrolled student numbers (IDs). """
        return list(self.enrolled_students.keys())

    def fetch_enrolled_students(self):
        """ Return the dictionary of enrolled students and their grades. """
        return self.enrolled_students

    def fetch_when_offered(self):
        """ Return (semester, year) of when this course was offered. """
        return self.semester, self.year

    def enroll_student(self, studentID):
        """ Enroll a student in the course.
            Return True if successful, else return False. """
        if studentID not in self.enrolled_students:
            self.enrolled_students.update({studentID: 'NG'})
            return True
        return False

    def enroll_students(self, studentIDs):
        """ Enroll multiple students in the course.
            Return True if successful, else return False. """
        for s in studentIDs:
            if s not in self.enrolled_students:
                self.enrolled_students.update({s: 'NG'})
            else:
                return False
        return True

    def drop_student(self, studentID):
        """ Drop this student from the course.
            Return True if successful, else return False. """
        if studentID in self.enrolled_students:
            self.enrolled_students.pop(studentID)
            return True
        return False

    def submit_grade(self, studentID, grade):
        """ Enter a grade for this student. """
        self.enrolled_students.update({studentID: grade})

    def fetch_grades(self):
        """ Return the enrolled_students dictionary. """
        return self.enrolled_students

    def fetch_grade(self, studentID):
        """ Return this student’s grade. """
        return self.enrolled_students[studentID]


def roll_courses():
    """ A semester has finished, and the grades are all in. This function rolls all
       the current courses for each student from current_courses to past_courses. """
    current = Student().fetch_current_courses()
    for n in current:
        Student().fetch_past_courses().append(n)

    Student.fetch_current_course = []


def compute_gpa(studentID):
    """ Returns the GPA of the student with input student number(ID),
       rounded off to 2 decimal places. """
    return '{:.2f}'.format(Course.fetch_grade(studentID))


def compute_gpas(studentIDs):
    """ Retuns a list of the gpas of all the students on the input list. """
    stud_dict = Course.fetch_grades()
    fetch_ids = []
    fetch_gpas = []
    for i, g in stud_dict.items():
        fetch_ids.append(i)
        fetch_gpas.append(g)

    gpas_list = []
    for c in studentIDs:
        if c in fetch_ids:
            gpas_list.append(fetch_gpas[fetch_ids.index(c)])
    return gpas_list


def best_student():
    """ Returns the name of the student with the highest GPA, in the format:
       FirstName LastName  (with one space between them)  """
    stud_dict = Course.fetch_grades()
    fetch_ids = []
    fetch_gpas = []
    for i, g in stud_dict.items():
        fetch_ids.append(i)
        fetch_gpas.append(g)
    max_gpa = 0
    max_id = 0
    for m in fetch_gpas:
        if m > max_gpa:
            max_gpa = m
            max_id = fetch_ids[fetch_gpas.index(m)]
    Student.fetch_name(max_id)


def worst_student():
    """ Returns the name of the student with the lowest GPA, in the format:
       FirstName LastName   (with one space between them)  """
    stud_dict = Course.fetch_grades()
    fetch_ids = []
    fetch_gpas = []
    for i, g in stud_dict.items():
        fetch_ids.append(i)
        fetch_gpas.append(g)
    min_gpa = 0
    min_id = 0
    for m in fetch_gpas:
        if m < min_gpa:
            min_gpa = m
            min_id = fetch_ids[fetch_gpas.index(m)]
    Student.fetch_name(min_id)


def compute_mean_GPA():
    stud_dict = Course.fetch_grades()
    fetch_ids = []
    fetch_gpas = []
    # go through all students
    # to find the courses
    # go through all courses
    # find the course -> get the student -> get the grade
    for i, g in stud_dict.items():
        fetch_ids.append(i)
        fetch_gpas.append(g)
    sum_nums = 0
    for m in fetch_gpas:
        sum_nums += m
    mean = sum_nums / len(fetch_gpas)
    return '{:.2f}'.format(mean)


def compute_mean_course_GPA(courseID):
    ''' Returns the mean GPA for the grades assigned to students who took this course. '''
    course_id = Courses.fetch_course(courseID)
    stud_dict = Course.fetch_grades()
    fetch_ids = []
    pass


all_courses = Courses()
all_students = Students()

c001 = Course(course_name='CS 1', course_number='001', semester='Spring', year=2019)
c002 = Course(course_name='CS 2', course_number='002', semester='Spring', year=2019)
c003 = Course(course_name='CS 3', course_number='003', semester='Spring', year=2019)
c004 = Course(course_name='CS 4', course_number='004', semester='Spring', year=2019)
c005 = Course(course_name='CS 5', course_number='005', semester='Spring', year=2019)
all_courses.add_courses([c001, c002, c003, c004, c005])
if all_courses.fetch_course_numbers() != ['001', '002', '003', '004', '005']: print('Error adding courses')
s001 = Student('Alan', 'Turing', '001')
s002 = Student('Grace', 'Hopper', '002')
s003 = Student('Ananda', 'Dev', '003')
s004 = Student('Lao', 'Tse', '004')
s005 = Student('Ada', 'Lovelace', '005')
s006 = Student('Claude', 'Shannon', '006')
s007 = Student('Radia', 'Perlman', '007')
all_students.add_students([s001, s002, s003, s004, s005, s006, s007])
if all_students.fetch_student_numbers() != ['001', '002', '003', '004', '005', '006', '007']: print(
    'Error adding courses')
c001.enroll_students(
    [s001.fetch_number(), s002.fetch_number(), s003.fetch_number(), s004.fetch_number(), s005.fetch_number()])
c002.enroll_students([s002.fetch_number(), s004.fetch_number(), s006.fetch_number()])
c003.enroll_students([s001.fetch_number(), s003.fetch_number(), s005.fetch_number(), s007.fetch_number()])
c004.enroll_students([s004.fetch_number(), s005.fetch_number(), s006.fetch_number(), s007.fetch_number()])
c005.enroll_students([s001.fetch_number(), s004.fetch_number(), s005.fetch_number(), s007.fetch_number()])
if c001.fetch_enrolled_studentIDs() != ['001', '002', '003', '004', '005']: print('Error enrolling')
if c002.fetch_enrolled_studentIDs() != ['002', '004', '006']: print('Error enrolling')
if c003.fetch_enrolled_studentIDs() != ['001', '003', '005', '007']: print('Error enrolling')
if c004.fetch_enrolled_studentIDs() != ['004', '005', '006', '007']: print('Error enrolling')
if c005.fetch_enrolled_studentIDs() != ['001', '004', '005', '007']: print('Error enrolling')
if s001.fetch_current_courses() != ['001', '003', '005']: print('Error enrolling')
if s002.fetch_current_courses() != ['001', '002']: print('Error enrolling')
if s003.fetch_current_courses() != ['001', '003']: print('Error enrolling')
if s004.fetch_current_courses() != ['001', '002', '004', '005']: print('Error enrolling')
if s005.fetch_current_courses() != ['001', '003', '004', '005']: print('Error enrolling')
if s006.fetch_current_courses() != ['002', '004']: print('Error enrolling')
if s007.fetch_current_courses() != ['003', '004', '005']: print('Error enrolling')
if not c003.drop_student('003'):  print('Error dropping student')
if s003.fetch_current_courses() != ['001']: print('Error dropping student')
if c003.fetch_enrolled_studentIDs() != ['001', '005', '007']: print('Error dropping student')
if not c002.enroll_student('003'):  print('Error adding a student')
if s003.fetch_current_courses() != ['001', '002']: print('Error adding student')
if c002.fetch_enrolled_studentIDs() != ['002', '004', '006', '003']: print('Error adding student')
c001_studentIDs = c001.fetch_enrolled_studentIDs()
for studentID in c001_studentIDs: c001.submit_grade(studentID, 'A')
c002_studentIDs = c002.fetch_enrolled_studentIDs()
for i, studentID in enumerate(c002_studentIDs): c002.submit_grade(studentID, chr(ord('A') + i))
c003_studentIDs = c003.fetch_enrolled_studentIDs()
for i, studentID in enumerate(c003_studentIDs): c003.submit_grade(studentID, chr(ord('D') - i))
c004_studentIDs = c004.fetch_enrolled_studentIDs()
for i, studentID in enumerate(c004_studentIDs): c004.submit_grade(studentID,
                                                                  chr(ord('B'))) if i % 2 else c004.submit_grade(
    studentID, chr(ord('A')))
c005_studentIDs = c005.fetch_enrolled_studentIDs()
for i, studentID in enumerate(c005_studentIDs): c005.submit_grade(studentID, chr(ord('B') - (i % 2)))
cc = s005.fetch_current_courses()
roll_courses()
d = all_courses.fetch_courses()
if d['004'].fetch_when_offered() != ('Spring', 2019): print('Error: fetch_when_offered()')
c006 = Course(course_name='CS 1', course_number='006', semester='Fall', year=2019)
c007 = Course(course_name='CS 2', course_number='007', semester='Fall', year=2019)
c008 = Course(course_name='CS 6', course_number='008', semester='Fall', year=2019)
c009 = Course(course_name='CS 7', course_number='009', semester='Fall', year=2019)
c010 = Course(course_name='CS 8', course_number='010', semester='Fall', year=2019)
all_courses.add_courses([c006, c007, c008, c009, c010])
if all_courses.fetch_course_numbers() != ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010']: print(
    'Error adding courses')
c006.enroll_students([s001.fetch_number(), s004.fetch_number(), s006.fetch_number()])
c007.enroll_students(
    [s001.fetch_number(), s003.fetch_number(), s004.fetch_number(), s005.fetch_number(), s007.fetch_number()])
c008.enroll_students([s002.fetch_number(), s003.fetch_number(), s006.fetch_number()])
c009.enroll_students([s003.fetch_number(), s005.fetch_number(), s007.fetch_number()])
c010.enroll_students([s002.fetch_number(), s005.fetch_number()])
if c006.fetch_enrolled_studentIDs() != ['001', '004', '006']: print('Error enrolling')
if c007.fetch_enrolled_studentIDs() != ['001', '003', '004', '005', '007']: print('Error enrolling')
if c008.fetch_enrolled_studentIDs() != ['002', '003', '006']: print('Error enrolling')
if c009.fetch_enrolled_studentIDs() != ['003', '005', '007']: print('Error enrolling')
if c010.fetch_enrolled_studentIDs() != ['002', '005']: print('Error enrolling')
if s001.fetch_current_courses() != ['006', '007']: print('Error enrolling')
if s002.fetch_current_courses() != ['008', '010']: print('Error enrolling')
if s003.fetch_current_courses() != ['007', '008', '009']: print('Error enrolling')
if s004.fetch_current_courses() != ['006', '007']: print('Error enrolling')
if s005.fetch_current_courses() != ['007', '009', '010']: print('Error enrolling')
if s006.fetch_current_courses() != ['006', '008']: print('Error enrolling')
if s007.fetch_current_courses() != ['007', '009']: print('Error enrolling')
c006_studentIDs = c006.fetch_enrolled_studentIDs()
for studentID in c006_studentIDs: c006.submit_grade(studentID, 'B')
c007_studentIDs = c007.fetch_enrolled_studentIDs()
for i, studentID in enumerate(c007_studentIDs): c007.submit_grade(studentID, chr(ord('A') + (i % 3)))
c008_studentIDs = c008.fetch_enrolled_studentIDs()
for i, studentID in enumerate(c008_studentIDs): c008.submit_grade(studentID, chr(ord('D') - i % 3))
c009_studentIDs = c009.fetch_enrolled_studentIDs()
for i, studentID in enumerate(c009_studentIDs): c009.submit_grade(studentID,
                                                                  chr(ord('A'))) if i % 2 else c009.submit_grade(
    studentID, chr(ord('B')))
c010_studentIDs = c010.fetch_enrolled_studentIDs()
for i, studentID in enumerate(c010_studentIDs): c010.submit_grade(studentID, chr(ord('B') - (i % 2)))
roll_courses()
print(best_student())
print(worst_student())
print(compute_mean_GPA())
print(compute_mean_course_GPA('004'))
print(compute_mean_course_GPA('009'))
