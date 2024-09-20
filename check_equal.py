# Agrim Kasaju (101280101)
# Austin Graham (101236825)
# Andrew Giles (101271100)
# Cross Rego (101256755)

def check_equal(expected: list, actual: list) -> bool:
    """Return true if the expected value is equal to the actual value.

    >>>check_equal({'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 
    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'Age': 18, 'StudyTime': 2, 
    'Failures': 0, 'Health': 3, 'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6})
    True

    >>>check_equal({'Age': 18, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 
    'Absences': 6, 'G1': 5, 'G2': 6, 'G3': 6}, {'School': 'GP', 'StudyTime': 2, 
    'Failures': 3, 'Health': 3, 'Absences': 10, 'G1': 7, 'G2': 8, 'G3': 10})
    False
    """

    if expected == actual:
        return True
    else:
        return False


if __name__ == '__main__':
    import T053_M1_load_data
    print('Test 1:')  # check the keys in the dictionary are correct.
    T053_M1_load_data.check_keys()
    print('')
    print('Test 2:')  # check the size of the list for each keys are correct.
    T053_M1_load_data.size_of_list()
    print('')
    print('Test 3:')  # check the format for each keys are correct.
    T053_M1_load_data.test_format()
    print('')
    # check that there are correct number of students in each keys, if G_Avg is added, and if G_Avg is calculated properly.
    print('Test 4:')
    T053_M1_load_data.test_average()
