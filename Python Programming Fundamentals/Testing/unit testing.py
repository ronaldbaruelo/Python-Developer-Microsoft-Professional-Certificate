# Function to be tested
def contains_five(my_list):
    return 5 in my_list

# Pytest test function
def test_contains_five():
    assert contains_five([1, 2, 3, 4, 5]) == True
    assert contains_five([10, 20, 30]) == False
    assert contains_five([]) == False
    assert contains_five([5]) == True
    assert contains_five([0, -5, 5, 100]) == True
