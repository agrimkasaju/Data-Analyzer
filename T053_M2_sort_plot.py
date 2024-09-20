# Agrim Kasaju (101280101)
# Austin Graham (101236825)
# Andrew Giles (101271100)
# Cross Rego (101256755)

import T053_M1_load_data
import numpy as np
import matplotlib.pyplot as plt


def student_list(dictionary: dict) -> list:
    """Return the data from the load data file including the G_avg informaiton added. Then turn in into a list. 

    >>>student_list(add_average(load_data('student-mat.csv', 'School')))
    [{'Age': 18, 'StudyTime': 6.0, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1':
    5, 'G2': 6, 'G3': 6, 'G_Avg': 5.67, 'School': 'GP'},
    {'Age': 17, 'StudyTime': 4.7, 'Failures': 0, 'Health': 3, 'Absences': 4, 'G1':
    5, 'G2': 5, 'G3': 6, 'G_Avg': 5.33, 'School': 'GP'},
    ...].
    """
    result = []
    for i in dictionary:
        for j in dictionary[i]:
            if "School" not in j:
                j.update({'School': i})
                result.append(j)
            if "Age" not in j:
                j.update({'Age': i})
                result.append(j)
            if "Health" not in j:
                j.update({'Health': i})
                result.append(j)
            if "Failures" not in j:
                j.update({'Failures': i})
                result.append(j)
    return result


def sort_students_bubble(dictionary: list, string: str) -> list:
    """Return the dictionaries in ascending order depending on the key you 
    want to order it from.

    Preconditions: has to be one of the attributes with in the keys in the dictionary.

    >>>sort_students_bubble(add_average(load_data('student-mat.csv', 'School')), 'Age')
    [{'Age': 15, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6, 'G_Avg': 5.666666666666667, 'School': 'GP'},... {'Age': 22, 'StudyTime': 1, 'Failures': 0, 'Health': 5, 'Absences': 5, 'G1': 8, 'G2': 9, 'G3': 9, 'G_Avg': 8.666666666666666, 'School': 'MS'}]
    >>>sort_students_bubble(add_average(load_data('student-mat.csv', 'Age')), 'School')
    [{'School': 'BD', 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10, 'G_Avg': 8.333333333333334, 'Age': 15},... {'School': 'MS', 'StudyTime': 1, 'Failures': 3, 'Health': 1, 'Absences': 16, 'G1': 6, 'G2': 8, 'G3': 8, 'G_Avg': 7.333333333333333, 'Age': 22}]
    """

    lst = student_list(dictionary)
    swap = True
    while swap:
        swap = False
        for i in range(len(lst) - 1):
            if lst[i].get(string) > lst[i + 1].get(string):
                lst[i][string], lst[i + 1][string] = lst[i
                                                         + 1][string], lst[i][string]
                swap = True
    return lst


def sort_students_selection(dictionary: list, attribute: str) -> list:
    """
    The purpose of this code is to print out a set of information decided by how
    you would like it to be printed out.

    Parameter: must be one of the attributes with in the keys in the dictionary.

    sort_students_selection((student_age_dictionary("student-mat.csv")), "School")

    sort_students_selection((student_age_dictionary("student-mat.csv")), "Age")

    sort_students_selection((student_age_dictionary("student-mat.csv")), "StudyTime")
    """

    selection = student_list(dictionary)
    for i in range(len(selection)):
        min_index = i

        for j in range(i + 1, len(selection)):
            if selection[j][attribute] < selection[min_index][attribute]:
                min_index = j
        selection[i], selection[min_index] = selection[min_index], selection[i]
    return selection


def curve_fit(student_dictonary, attribute: str, num: int) -> list:
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
    key = list((student_dictonary[0]).keys())[-1]
    G_Avg = list((student_dictonary[0]).keys())[-2]
    m = []

    x = 0
    y = 0
    n = 0

    while x in range(len(student_dictonary)):

        g_avge_dict[list((student_dictonary[x]).values())[-1]] = []

        x += 1

    x = 0

    key_of_g_avg_dict = list(g_avge_dict.keys())

    while y in range(len(key_of_g_avg_dict)):

        while x in range(len(student_dictonary)):
            if (student_dictonary[x])[key] is key_of_g_avg_dict[y]:
                m.append((student_dictonary[x])[G_Avg])
                x += 1
            else:
                n = x
                x = 395
                g_avge_dict[key_of_g_avg_dict[y]] = m
                m = []

        y += 1
        x = n

    m = []
    while x in range(len(student_dictonary)):
        if (student_dictonary[x])[key] is key_of_g_avg_dict[-1]:
            m.append((student_dictonary[x])[G_Avg])
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


def histogram(dictionary: list, string: str) -> None:
    """Return none, makes a histogram of the number of students in each level of attribute within each key
    in the dictionary.

    Precondition: must be one of the attributes within the keys in the dictionary

    >>>histogram(T053_M1_load_data.add_average(T053_M1_load_data.load_data('student-mat.csv', 'School')), 'Age')
    None
    """

    fig1 = plt.figure()
    plt.title("Histogram")

    dic_lst = student_list(dictionary)
    key = []
    key_index = {}
    for i in dic_lst:
        val = [i.get(string)]
        key += val
    for i in key:
        if not (i in key_index):
            key_index.update({i: 0})

        new_val = {i: (key_index.get(i) + 1)}
        key_index.update(new_val)
    key_index.keys()

    plt.bar(list(key_index.keys()), list(key_index.values()), width=1.0)
    plt.xlabel(string)
    plt.ylabel('number of students')
    plt.show()


if __name__ == '__main__':
    student_list(T053_M1_load_data.add_average(
        T053_M1_load_data.load_data('student-mat.csv', 'School')))

    sort_students_bubble(T053_M1_load_data.add_average(
        T053_M1_load_data.load_data('student-mat.csv', 'School')), 'Age')

    sort_students_selection(T053_M1_load_data.add_average(
        T053_M1_load_data.load_data('student-mat.csv', 'School')), 'Health')

    curve_fit(student_list(T053_M1_load_data.load_data(
        'student-mat.csv', 'Age')), "Age", 2)

    histogram(T053_M1_load_data.add_average(
        T053_M1_load_data.load_data('student-mat.csv', 'School')), 'Age')

