# Agrim Kasaju (101280101)
# Austin Graham (101236825)
# Andrew Giles (101271100)
# Cross Rego (101256755)

import string
from typing import List
import check_equal


def student_school_dictionary(file: str) -> dict:
    """Return the dictionary of the keys of the schools with the list of items
    of dictionaries of the age, studytime, failures, health, absences, and grades
    in the student-mat.csv file.

    Preconditon: must be the csv file given.

    >>>student_school_dictionary('student-mat.csv')
    {'GP': [{'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,
     'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}...],
     'MB': [{'Age': 16, 'StudyTime': 2, 'Failures': 0, 'Health': 3,
     'Absences': 12, 'G1': 5, 'G2': 5, 'G3': 5}...],
     'CF': [{'Age': 16, 'StudyTime': 2, 'Failures': 1, 'Health': 5,
     'Absences': 4, 'G1': 10, 'G2': 12, 'G3': 12}...],...}
    """

    infile = open(file, "r")
    school_dict = {}
    keys = ['GP', 'MB', 'CF', 'BD', 'MS']
    for i in keys:
        school_dict[i] = []

    l = infile.readline()
    for line in infile:
        school_list = line.split(',')
        for i in school_list:
            a_dict = {'Age': int(school_list[1]), 'StudyTime': int(school_list[2]), 'Failures': int(school_list[3]),
                      'Health': int(school_list[4]), 'Absences': int(school_list[5]), 'G1': int(school_list[6]), 'G2': int(school_list[7]), 'G3': int(school_list[8])}
        school_dict[school_list[0]].append(a_dict)

    infile.close()
    return school_dict


def student_age_dictionary(filename: str) -> dict:
    """Return the students infomation grouped using age.

    Preconditon: must be the csv file given.

    >>> student_age_dictionary("student-mat.csv")
        {15: [{'School': 'GP', 'StudyTime': '2', 'Failures': '3', 'Health': '3',
        'Absences': '10', 'G1': '7', 'G2': '8', 'G3': '10\n'},...
        {16: [{'School': 'GP', 'StudyTime': '2', 'Failures': '0', 'Health': '5',
        'Absences': '4', 'G1': '6', 'G2': '10', 'G3': '10\n'},...
        {22: [{'School': 'BD', 'StudyTime': '1', 'Failures': '3', 'Health': '1',
        'Absences': '16', 'G1': '6', 'G2': '8', 'G3': '8\n'}...]...}
    """
    age_dict = {}
    keys = [15, 16, 17, 18, 19, 20, 21, 22]
    for i in keys:
        age_dict[i] = []

    infile = open(filename, "r")

    l = infile.readline()
    for line in infile:
        age_list = line.split(',')
        a_dict = {'School': age_list[0], 'StudyTime': int(age_list[2]), 'Failures': int(age_list[3]),
                  'Health': int(age_list[4]), 'Absences': int(age_list[5]), 'G1': int(age_list[6]), 'G2': int(age_list[7]), 'G3': int(age_list[8])}
        age_dict[int(age_list[1])].append(a_dict)

    infile.close()
    return age_dict


def student_health_dictionary(file: str) -> dict:
    """Return the dictionary of student health with iteams with a list of
    school, age, studytime, failures, absence, and grades dictionary.

    Preconditon: must be the csv file given.

    >>>student_health_dictionary("student-mat.csv")
    {1: [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0,
    'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6}, {'School': 'GP', 'Age': 15,
    'StudyTime': 2, 'Failures': 0, 'Absences': 0, 'G1': 16, 'G2': 18,
    'G3': 19}...]...]...}
    """

    health_dict = {}
    keys = [1, 2, 3, 4, 5]
    for i in keys:
        health_dict[i] = []

    infile = open(file, "r")

    l = infile.readline()
    for line in infile:
        health_list = line.split(',')
        dictionary = {'School': health_list[0], 'Age': int(health_list[1]), 'StudyTime': int(health_list[2]), 'Failures': int(
            health_list[3]), 'Absences': int(health_list[5]), 'G1': int(health_list[6]), 'G2': int(health_list[7]), 'G3': int(health_list[8])}
        health_dict[int(health_list[4])].append(dictionary)

    infile.close()
    return health_dict


def student_failures_dictionary(filename: str) -> dict:
    """The program prints out all the students that had a certain number of
    failures, ranging from 0 to 10 fails. It will print out the number of
    failures first, then all the students information with that number of fails.

    Precondition: File used is "student-mat.csv"

    >>>student_failure_dictionary('student-mat.csv')
    {0: [{'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,
     'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}...],
     1: [{'School': 'GP', 'Age': 16, 'StudyTime': 2, 'Health': 3,
     'Absences': 25, 'G1': 7, 'G2': 10, 'G3': 11}...],
     2: [{'School': 'GP', 'Age': 16, 'StudyTime': 1, 'Health': 5,
     'Absences': 14, 'G1': 6, 'G2': 9, 'G3': 8}...]...}
    """
    fail_dict = {}
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in keys:
        fail_dict[i] = []

    infile = open(filename, "r")

    l = infile.readline()
    for line in infile:
        failure_list = line.split(',')
        a_dict = {'School': failure_list[0], 'Age': int(failure_list[1]), 'StudyTime': int(failure_list[2]),
                  'Health': int(failure_list[4]), 'Absences': int(failure_list[5]), 'G1': int(failure_list[6]), 'G2': int(failure_list[7]), 'G3': int(failure_list[8])}
        fail_dict[int(failure_list[3])].append(a_dict)

    infile.close()
    return fail_dict


def load_data(filename: str, key: str) -> dict:
    """Return the dictionary of the file with the given key 'School', 'Age',
    'Health', 'Failures', else print invalid key.

    Preconditon: must be the csv file given.

    >>>load_data('student-mat.csv', 'Age')
    {15: [{'School': 'GP', 'StudyTime': 2, 'Failures': 3, 'Health': 3,
    'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10}...]...}
    >>>load_data('student-mat.csv', 'School')
    {'GP': [{'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,
    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}...]...}
    """

    if key == 'School':
        return student_school_dictionary(filename)
    elif key == 'Age':
        return student_age_dictionary(filename)
    elif key == 'Health':
        return student_health_dictionary(filename)
    elif key == 'Failures':
        return student_failures_dictionary(filename)
    else:
        print("Invalid Key")
        return {}


def add_average(dictionary: dict) -> dict:
    """Returns the average of grades: 'G1', 'G2', 'G3' of dictionaries of
    load_data with any of the keys: 'School', 'Age', 'Health', 'Failures'.

    >>>add_average(load_data('student-mat.csv', 'School'))
    {'GP': [{'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3,
    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.666666666666667}...]
    ...}
    >>>add_average(load_data('student-mat.csv', 'Failures'))
    {0: [{'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3,
    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.666666666666667}...]
    ...}
    >>>add_average(load_data('student-mat.csv', 'Age'))
    {15: [{'School': 'GP', 'StudyTime': 2, 'Failures': 3, 'Health': 3,
    'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.333333333333334}...]
    ...}
    """

    for i in dictionary:
        for i in dictionary[i]:
            average = (i.get('G1') + i.get('G2')
                       + i.get('G3')) / 3
            i.setdefault('G_Avg', average)
    return dictionary


student_school_dictionary('student-mat.csv')
student_age_dictionary('student-mat.csv')
student_health_dictionary('student-mat.csv')
student_failures_dictionary('student-mat.csv')

load_data('student-mat.csv', 'School')
load_data('student-mat.csv', 'Age')
load_data('student-mat.csv', 'Health')
load_data('student-mat.csv', 'Failures')

add_average(load_data('student-mat.csv', 'School'))
add_average(load_data('student-mat.csv', 'Age'))
add_average(load_data('student-mat.csv', 'Health'))
add_average(load_data('student-mat.csv', 'Failures'))


def check_keys() -> None:
    """Check to see wheather the keys of the dictionaries are correct.

    Precondition: Must call the data file 'student-mat.csv'.

    >>> check_keys('student-mat.csv')
    Test Passed: 4
    Test Failed: 0
    """
    expected = {'School': ['GP', 'MB', 'CF', 'BD', 'MS'], 'Age':
                [15, 16, 17, 18, 19, 20, 21, 22], 'Health': [1, 2, 3, 4, 5], "Failures": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

    List = ['School', 'Age', 'Health', 'Failures']
    check_passed = 0
    check_failed = 0
    for keys in List:
        dictionary = load_data('student-mat.csv', keys)
        actual = list(dictionary.keys())
        check = check_equal.check_equal(expected[keys], actual)
        if check == True:
            check_passed += 1
        if check == False:
            check_failed += 1

    print("Test Passed:", check_passed)
    print("Test Failed:", check_failed)


def size_of_list() -> None:
    """Checks the size of the list for each keys in the dictionary.

    Precondition: has to be one of the keys compared.

    >>>size_of_list()
    pass
    pass
    pass
    pass
    """
    total_dict = [student_school_dictionary, student_age_dictionary,
                  student_health_dictionary, student_failures_dictionary]

    for i in range(len(total_dict)):
        a = (total_dict[i]("student-mat.csv"))
        if (sum([len(x) for x in a.values()])) == 395:
            print('pass')
        else:
            print("fail")


def test_format() -> None:
    """Checks if the formate of the data is correct for each of the keys:
    'School', 'Age', 'Health', 'Failures'.

    Precondition: Has to be one of the keys.

    >>>test_format()
    Test Passed: 4
    Test Failed: 0
    """
    expected = {'School': {'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6},
                'Age': {'School': 'GP', 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10},
                'Health': {'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 'G1': 6, 'G2': 5, 'G3': 6},
                'Failures': {'School': 'GP', 'Age': 18, 'StudyTime': 2, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}}

    count_pass = 0
    count_fail = 0

    dictionary = load_data('student-mat.csv', 'School')
    dictionary2 = load_data('student-mat.csv', 'Age')
    dictionary3 = load_data('student-mat.csv', 'Health')
    dictionary4 = load_data('student-mat.csv', 'Failures')

    for i in dictionary:
        val = dictionary['GP']
    for j in range(len(val)):
        get_val = val[0]

    check = check_equal.check_equal(expected['School'], get_val)
    if check == True:
        count_pass += 1
    else:
        count_fail += 1

    for i in dictionary2:
        val = dictionary2[15]
    for j in range(len(val)):
        get_val = val[0]

    check = check_equal.check_equal(expected['Age'], get_val)
    if check == True:
        count_pass += 1
    else:
        count_fail += 1

    for i in dictionary3:
        val = dictionary3[1]
    for j in range(len(val)):
        get_val = val[0]

    check = check_equal.check_equal(expected['Health'], get_val)
    if check == True:
        count_pass += 1
    else:
        count_fail += 1

    for i in dictionary4:
        val = dictionary4[0]

    for j in range(len(val)):
        get_val = val[0]

    check = check_equal.check_equal(expected['Failures'], get_val)
    if check == True:
        count_pass += 1
    else:
        count_fail += 1
    print("Test Passed:", count_pass)
    print("Test Failed:", count_fail)


def test_average():
    """
    The code tests if there is the right amount of students, if they all have a
    G_Avg function, and if the G_Avg function works properly.

    Precondition: Must be used with the student-mav.csv file. Tests will fail
    if another file is used.

    >>>test_average()
    School: number of student passed
    G_Avg added Passed: 395
    G_Avg added Failed: 0
    G_Avg calculated Passed
    """

    keys = ['School', 'Age', 'Health', 'Failures']
    for i in keys:
        dictionary = add_average(load_data('student-mat.csv', i))
        count = 0
        for j in dictionary:
            for k in dictionary[j]:
                count += 1
        check = check_equal.check_equal(395, count)
        if check == True:
            print((i + ":"), "number of student passed")
        else:
            print(i, "number student failed")

        count_avg = 0
        count_failed = 0
        for i in dictionary:
            for j in dictionary[i]:
                lst = list(j)
                for k in range(len(lst)):
                    check = check_equal.check_equal('G_Avg', lst[8])
                if check == True:
                    count_avg += 1
                else:
                    count_failed += 1

        print('G_Avg added Passed:', count_avg)
        print('G_Avg added Failed:', count_failed)

        lst = []
        for i in dictionary:
            for j in dictionary[i]:
                lst.append(str(round(j.get('G_Avg'), 2)))

        for h in range(len(lst)):
            check = check_equal.check_equal(
                '5.67', lst[0]) or check_equal.check_equal('8.33', lst[0])
        if check == True:
            print("G_Avg calculated Passed")
            print('')
        else:
            print("G_Avg calculated Failed")
