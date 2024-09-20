# Agrim Kasaju (101280101)
# Austin Graham (101236825)
# Andrew Giles (101271100)
# Cross Rego (101256755)

from T053_M1_load_data import *
from T053_M2_sort_plot import *
import numpy as np
from scipy.optimize import fminbound, fsolve


def curve_fit(student_dictionary, attribute: str, num: int) -> list:
    """
    This function takes an input list of students, finds the g_avg for the total list for each level of the attribute selected, then outputs the equation of the best fit as a list of coefficientsents. 

    Preconditions, input list needs to be from The student_list funtion from T053_m2_student_list as it puts the students in order based on the selected attrubue level.


    >>>curve_fit(student_list(load_data('student-mat.csv', 'Age')),"Age",2)
       [-0.12017857142857201, 4.060297619047645, -23.142202380952657]

    >>>curve_fit(student_list(load_data('student-mat.csv', 'Failures')),"Failures",5)
       [-0.012821999832509746, 0.07693199899505894, 0.21395800184239047, -2.6580680010049376, 11.359999999999998]

    >>>curve_fit(student_list(load_data('student-mat.csv', 'Health')),"Health",3)
       [-0.027500000000000076, 0.4667857142857155, -2.2657142857142882, 13.708000000000004]
    """
    g_avge_dict = {}
    key = list((student_dictionary[0]).keys())[-1]
    G_Avg = list((student_dictionary[0]).keys())[-2]
    m = []

    x = 0
    y = 0
    n = 0

    while x in range(len(student_dictionary)):

        g_avge_dict[list((student_dictionary[x]).values())[-1]] = []

        x += 1

    x = 0

    key_of_g_avg_dict = list(g_avge_dict.keys())

    while y in range(len(key_of_g_avg_dict)):

        while x in range(len(student_dictionary)):
            if (student_dictionary[x])[key] is key_of_g_avg_dict[y]:
                m.append((student_dictionary[x])[G_Avg])
                x += 1
            else:
                n = x
                x = 395
                g_avge_dict[key_of_g_avg_dict[y]] = m
                m = []

        y += 1
        x = n

    m = []
    while x in range(len(student_dictionary)):
        if (student_dictionary[x])[key] is key_of_g_avg_dict[-1]:
            m.append((student_dictionary[x])[G_Avg])
            x += 1
        else:
            x += 1
    g_avge_dict[key_of_g_avg_dict[-1]] = m

    y = 0
    while y in range(len(key_of_g_avg_dict)):
        t = (sum(g_avge_dict[key_of_g_avg_dict[y]]))
        d = len(list(g_avge_dict[key_of_g_avg_dict[y]]))
        g_avge_dict[key_of_g_avg_dict[y]] = round(t / d, 2)

        y += 1

    g = g_avge_dict

    y = list(g.values())
    c = len(g.keys())

    if (num) <= (len(y)):
        a = list(g.keys())[0]
        b = list(g.keys())[-1]
        x = np.linspace(a, b, c)
        z = np.polyfit(x, y, num)

    else:
        x = list(g.keys())
        z = np.polyfit(x, y, c)

    return tuple(map(tuple, (z, x)))


file = ''
while file != 'stored_cmd.txt':
    file = input(
        'Please enter the name of the file where your commands are stored: ')
infile = open(file, "r")
dic = []
for line in infile:
    file_cmd = line.split(';')
    for i in file_cmd:
        dic.append(i.strip('\n').strip(' '))
infile.close()


def get_command():
    """Return promp to input the file name and command.

    Precondition: needs to be one of the keys and attributes

    >>>get_command()
    The available commands are:
     1. L; load Data
     2. S; Sort Data
          'School' 'Age' 'StudyTime' 'Failures' 'Health'
          'Absences' 'G1' 'G2' 'G3' 'G_Avg'
     3. H; Histogram
          'School' 'Age' 'StudyTime' 'Failures' 'Health'
          'Absences'
     4. W; Worst _____ for Grades
          'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
     5. B; Best _____ for Grades
          'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
     6. Q; Quit
    Please enter the name of the file where your commands are stored: 
    """

    string = """The available commands are:
    1. L; load Data
    2. S; Sort Data
         'School' 'Age' 'StudyTime' 'Failures' 'Health'
         'Absences' 'G1' 'G2' 'G3' 'G_Avg'
    3. H; Histogram
         'School' 'Age' 'StudyTime' 'Failures' 'Health'
         'Absences'
    4. W; Worst _____ for Grades
         'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
    5. B; Best _____ for Grades
         'Age' 'StudyTime' 'Failures' 'Health' 'Absences'
    6. Q; Quit"""
    print(string)

    command = dic
    print(command)

    cmd = input('Please type your command: ')
    while (cmd not in dic):
        cmd = input('Please type a valid command: ')
    return (cmd, command)


def execute_command(file_input):
    """Return the loaded, sorted, histogram, min and max of the attributes from
    the txt file.

    Precondition: must be one of the keys and attribute

    >>>Please type your command: L
    {1: [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 
    6, 'G1': 6, 'G2': 5, 'G3': 6},...}]}
    >>>Please type a valid command: S
    [{'School': 'GP', 'Age': 17, 'StudyTime': 2, 'Failures': 0, 'Absences': 6, 
    'G1': 6, 'G2': 5, 'G3': 6, 'Health': 1},...}]
    """
    cmd, command = file_input
    loaded = load_data(command[1], command[3])
    if cmd == 'L':
        loaded = load_data(command[1], command[3])
        print(loaded)
    elif cmd == 'S':
        print(sort_students_selection(loaded, command[3]))
    elif cmd == 'H':
        print(histogram(loaded, command[5]))
    elif cmd == 'W':
        return minimum(student_list(load_data('student-mat.csv', command[7])), command[9])
    elif cmd == 'B':
        return maximum(student_list(load_data('student-mat.csv', command[11])), command[9])


def minimum(dictionary: dict, attribute: str) -> tuple:
    """Return worst attribute for grade.

    Preconditions: has to be one of the attributes

    >>>Please type your command: W
    The worst grade for attribute Age is 22 years old
    """
    coeff_interval = curve_fit(dictionary, attribute, 2)
    for i in coeff_interval:
        interval = coeff_interval[1]
        coeff = coeff_interval[0]
    for i in interval:
        mini = int(interval[0])
        maxi = int(interval[len(interval) - 1])
    poly = np.array(list(coeff))
    x = np.linspace(mini, maxi, maxi)

    x_e = np.linspace(mini, maxi, 100)
    y_e = np.polyval(poly, x_e)

    def x_minus(x):
        return np.polyval(poly, x)

    x_min = fminbound(x_minus, mini, maxi)
    print('The worst grade for attribute Age is {} years old.'.format(round(x_min)))


def maximum(dictionary: dict, attribute: str) -> tuple:
    """Return best attribute for grade.

    Preconditions: has to be one of the attributes

    Please type your command: B
    The best grade for attribute Age is 15 years old.
    """
    coeff_interval = curve_fit(dictionary, attribute, 2)
    for i in coeff_interval:
        interval = coeff_interval[1]
        coeff = coeff_interval[0]
    for i in interval:
        mini = int(interval[0])
        maxi = int(interval[len(interval) - 1])
    poly = np.array(list(coeff))
    x = np.linspace(mini, maxi, maxi)

    x_e = np.linspace(mini, maxi, 100)
    y_e = np.polyval(poly, x_e)

    def x_minus(x):
        return -np.polyval(poly, x)

    y_min = fminbound(x_minus, mini, maxi)
    print('The best grade for attribute Age is {} years old.'.format(round(y_min)))


end = ''
while end != 'Q' and end != 'q':
    x = get_command()
    execute_command(x)
    end = input('Enter Q to quit or anything to continue: ')
print('This is end, have good day ツ')
