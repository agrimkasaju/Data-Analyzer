Team Leader Contact Information: 
Agrim Kasaju - agrimkasaju@cmail.carleton.ca

Date:
Sunday, December 11th, 2022

Software Name:
Wing 101, Python Version 3.10.7 

Description:
Taking the data from the text file 'student-mav.csv',
the function load_data uses the 'Failures', 'Age',
'Health', and 'School' dictionary codes to get all the
information from them.

The add_average function gets the average of all the
G's for each student and adds a new key called 'G_Avg'.

The test files then test each function to make sure
the data used in the functions is all correct and that
there is no wrong data being used. If the tests pass
they will print out a pass and sometimes how many times
they pass.

The student_list function uses the load_data function
and then appends what the arguemnt is. It then turns
the data into a list. 

Bubble and selection sort will sort out all of the data
using the parameters you choose in the function call. 

Curve_fit finds the G_Avg for each level of the 
attribute selected, then outputs the equation best fit
as a list of coefficientsents. Histogram function
creates a histogram of all of the attributes.

The minimum and maximum get the highest average or
lowest average of the selected attribute. 

Installation:
import matplotlib.pyplot as plt
import string
import numpy as np

Usage:
The usage for this code is to sort, get specific points
of data, averages, minimum and maximum as well as 
print out graphs of the functions.

Credits:
Agrim Kasaju - student_school_dictionary, load_data, 
add_average, test_format, sort_students_bubble,
histogram, Moduel 2

Austin Graham - sort_students_selection, test_average,
student_failures_dictionary, README file, maximum

Andrew Giles - student_age_dictionary, check_keys, 
student_list, minimum,

Cross Rego - student_health_dictionary, size_of_list,
student_list, curve_fit, histogram, Module 1

License:
Copyright (c) [2022] [Agrim Kasaju] [Austin Graham] [Andrew Giles] [Cross Rego]