# Agrim Kasaju (101280101)
# Austin Graham (101236825)
# Andrew Giles (101271100)
# Cross Rego (101256755)
"""
This is a text ui that allows a user to define how they would like to see data displayed. 


"""
from T053_M1_load_data import *
from T053_M2_sort_plot import *
import numpy as np
from scipy.optimize import fminbound, fsolve
b = 1
load1 = ["L", "l"]
sort1 = ["S", "s"]
histogram1 = ["H", "h"]
worst1 = ["W", "w"]
best1 = ["B", "b"]
quit1 = ["Q", "q"]
loaded = 0


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

    >>>Please type your command: B
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


while b in range(10):
    input_prompt = input("The available commands are: \n 1. L)oad Data \n 2. S)ort Data"
                         "\n     'School' 'Age' 'StudyTime' 'Failures' 'Health'"
                         "\n     'Absences ' 'G1 ' 'G2' 'G3' 'G_Avg'" "\n 3. H)istogram" "\n     'School' 'Age' 'StudyTime' 'Failures' 'Health' 'Absences'" "\n 4. W)orst _____ for Grades""\n      'Age' 'StudyTime' 'Failures' 'Health' 'Absences'""\n 5. B)est _____ for Grades\n"
                         "     'Age' 'StudyTime' 'Failures' 'Health' 'Absences'" "\n 6. Q)uit" "\n Please type your command: \n")

    if input_prompt in load1:
        input_filename = input("Please enter the name of the file: \n")
        if len(input_filename) > 0:
            input_attribute = input(
                "Please enter the attribute to use as key: \n")
            x = add_average(load_data(input_filename, input_attribute))
            print("Data loaded:")
            print(x)
            b = 1
            loaded = 1
    if input_prompt in quit1:
        print("Program terminated")
        b = 1222
    elif loaded == 0:
        print("File not loaded. Please, load a file first.")

    if input_prompt in sort1:
        input_attrubite = input("Please enter the attribute you want to use for sorting:\n"
                                "'School' 'Age' 'StudyTime' 'Failures' 'Health' \n 'Absences' 'G1' 'G2' 'G3' 'G_Avg'\n")

        sorted_list = sort_students_bubble(add_average(
            load_data(input_filename, input_attribute)), input_attribute)
        input_check = input(
            "Data Sorted. Do you want to display the data? \n(y or n):")
        if input_check == "y":
            print(sorted_list)
            move_on = input("press enter to move on:\n")
            b = 1
        elif input_check == "n":
            b = 1

    elif input_prompt in histogram1:
        input_attrubite = input("Please enter the attribute you want to use for sorting:\n"
                                "'School' 'StudyTime' 'Absences' 'Age' 'Failures' 'Health' \n")
        histogram(load_data(input_filename, input_attribute), input_attribute)
        b = 1
        move_on = input("press enter to move on:\n")
    elif input_prompt in worst1:
        input_attrubite = input("Please enter the attribute you want to use for sorting:\n"
                                "'School' 'Age' 'Failures' 'Health' \n")
        minimum(student_list(load_data('student-mat.csv',
                input_attrubite)), input_attrubite)
        move_on = input("press enter to move on:\n")
        b = 1
    elif input_prompt in best1:

        input_attrubite = input("Please enter the attribute you want to use for sorting:\n"
                                "'School' 'Age' 'Failures' 'Health' \n")
        maximum(student_list(load_data('student-mat.csv',
                input_attrubite)), input_attrubite)
        move_on = input("press enter to move on:\n")
        b = 1
