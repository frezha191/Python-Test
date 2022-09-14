
#def selection_sort(nums):
    # This value of i corresponds to how many values were sorted
#    for i in range(len(nums)):
        # We assume that the first item of the unsorted segment is the smallest
#        lowest_value_index = nums[i]
        # This loop iterates over the unsorted items
#        for j in range(i + 1, len(nums)):
#            if int(nums[j][2]) < int(nums[lowest_value_index[2]]):
#                lowest_value_index = nums[j]
        # Swap values of the lowest unsorted element with the first unsorted
        # element
#        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# Verify it works

#selection_sort(random_list_of_nums)
#print(random_list_of_nums)

from operator import itemgetter
A = [[10, 8], [90, 2], [45, 6]]
print("Sorted List A based on index 0: % s" % (sorted(A, key=itemgetter(0))))
B = random_list_of_nums = [["ssbe462", 99, "132"], ["tnu075", 54, "65"],["kyb957", 95, "113"], ["gtqg539", 54, "91"], ["rhc535", 12, "29"]]
#B = [[50, 'Yes'], [20, 'No'], [100, 'Maybe']]
print("Sorted List B based on index 2: % s" % (sorted(B, key=itemgetter(2))))



