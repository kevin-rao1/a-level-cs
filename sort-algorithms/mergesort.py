def split_list(list):
    left_list = list[:len(list)//2]
    right_list = list[len(list)//2:]
    return left_list, right_list

def merge_lists(left_list, right_list):
    final_list = ["" for i in range(len(left_list)+len(right_list))]
    l = 0
    r = 0
    f = 0
    while not f == len(left_list) + len(right_list):
        if left_list[l] < right_list[r]:
            final_list[f] = left_list[l]
            l += 1
        else:
            final_list[f] = right_list[r]
            r += 1
        f += 1
        print(final_list)
    return final_list


list1 = [1,4,3,5,7,2,9]
print(split_list(list1))
list1 = [5, 7, 9, 11]
list2 = [2, 8, 9008]
print(merge_lists(list1, list2))