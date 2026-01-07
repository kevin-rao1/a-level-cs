def bubble_sort(unsorted_list):
    noofswaps = 0
    for i in unsorted_list:
        for j in range(i):
            try:
                if unsorted_list[j] > unsorted_list[j+1]:
                    smaller_value = unsorted_list[j+1]
                    unsorted_list[j+1] = unsorted_list[j]
                    unsorted_list[j] = smaller_value
                    noofswaps +=1
            except IndexError:
                break
    print(f"noofswaps = {noofswaps}")
    return unsorted_list # now sorted

numbers = [6,4,9,2,0]
print(numbers, bubble_sort(numbers))