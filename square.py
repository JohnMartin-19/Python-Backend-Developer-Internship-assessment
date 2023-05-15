def test_function(array):
    arr_to_be_returned = []
    for num in array:
        arr_to_be_returned.append(num*num)

    return arr_to_be_returned
    

print(test_function([3,4,5]))