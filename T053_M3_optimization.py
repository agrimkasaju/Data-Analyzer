# Agrim Kasaju (101280101)
# Austin Graham (101236825)
# Andrew Giles (101271100)
# Cross Rego (101256755)
import T053_M1_load_data as ld
import T053_M2_sort_plot as sp
import numpy as np
from scipy.optimize import fminbound, fsolve


def minimum(dictionary: dict, attribute: str) -> tuple:
    """Return worst attribute for grade.

    Preconditions: has to be one of the attributes

    >>>minimum(sp.student_list(ld.load_data('student-mat.csv', 'Age')), "Age")
    (21.99999391225472, 8.168754632119963)
    >>>minimum(sp.student_list(ld.load_data('student-mat.csv', 'Health')), "Health")
    (3.5095465393794756, 9.845722724173207)
    """
    coeff_interval = sp.curve_fit(dictionary, attribute, 2)
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
    y_min = np.polyval(poly, x_min)
    return (x_min, y_min)


def maximum(dictionary: dict, attribute: str) -> tuple:
    """Return best attribute for grade.

    Preconditions: has to be one of the attributes

    >>>maximum(sp.student_list(ld.load_data('student-mat.csv', 'Age')), "Age")
    (15.00000608774528, 10.931249827149568)
    >>>maximum(sp.student_list(ld.load_data('student-mat.csv', 'Health')), "Health")
    (1.000005628673589, 11.7305629735091)
    """
    coeff_interval = sp.curve_fit(dictionary, attribute, 2)
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

    x_min = fminbound(x_minus, mini, maxi)
    y_min = np.polyval(poly, x_min)
    return (x_min, y_min)


if __name__ == '__main__':
    minimum(sp.student_list(ld.load_data('student-mat.csv', 'Age')), "Age")
    minimum(sp.student_list(ld.load_data(
        'student-mat.csv', 'Health')), "Health")
    maximum(sp.student_list(ld.load_data('student-mat.csv', 'Age')), "Age")
    maximum(sp.student_list(ld.load_data(
        'student-mat.csv', 'Health')), "Health")
