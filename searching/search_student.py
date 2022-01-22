import collections
import bisect


Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def comp_gpa(student):
    return -student.grade_point_average, student.name

def search_student(students, target_student):
    i = bisect.bisect_left([comp_gpa(student) for student in students], comp_gpa(target_student))
    return 0 <= i < len(students) and students[i] == target_student


if __name__ == '__main__':
    s1 = Student('A', 9.0)
    s2 = Student('B', 7.0)
    s3 = Student('C', 8.0)
    print(search_student([s1, s2, s3], Student('B', 7.0) ))