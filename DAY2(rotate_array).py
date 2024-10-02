def rotate_array(nums , k):
    # Create a list to store the rotated array
    rotated_array = []

    #calculate the number of steps to rotate , handling cases where k > number of array
    k = k % len(nums)

    #take the last k element of the array and add it to the new list
    for i in range(len(nums)-k, len(nums)):
     rotated_array.append(nums[i])
    #add the remaing elements of the array to a new list
    for i in range(len(nums)-k):
       rotated_array.append(nums[i])
    #return the rotated array 
    return rotated_array

# Test the function
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Original array:", nums)
print("Rotated array:", rotate_array(nums, k))