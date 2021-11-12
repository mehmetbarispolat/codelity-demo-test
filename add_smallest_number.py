'''Add smallest positive number to given array.
'''
import copy
import timeit


def add_smallest_number(number_list: list) -> list:
    '''Add smallest positive number to array by using sorting.

    Args:
        number_list(list): given number of list

    Return:
        list: Added number of list
    '''
    smallest_number = 1
    copy_number_list = copy.deepcopy(number_list)
    copy_number_list.sort()
    for number in copy_number_list:
        if number > 0 and number == smallest_number:
            smallest_number = number + 1

    copy_number_list.append(smallest_number)
    return copy_number_list

def add_smallest_number_without_sort(number_list: list) -> list:
    '''Add smallest positive number to array without sorting.

    Args:
        number_list(list): given number of list

    Return:
        list: Added number of list
    '''
    smallest_number = 1
    copy_number_list = copy.deepcopy(number_list)
    for _ in range(len(copy_number_list)):
        for number in copy_number_list:
            if number > 0 and number == smallest_number:
                smallest_number = number + 1
                break

    copy_number_list.append(smallest_number)
    return copy_number_list

def main():
    numbers_1 = [1,6,5,3,1,2]
    numbers_2 = [-2,-3]
    numbers_3 = [-1,0,3,1]

    for number_list in [numbers_1, numbers_2, numbers_3]:
        result_with_sort_start_time = timeit.default_timer()
        result_with_sort = add_smallest_number(number_list)
        result_with_sort_end_time = timeit.default_timer()

        result_without_sort_start_time = timeit.default_timer()
        result_without_sort = add_smallest_number_without_sort(number_list)
        result_without_sort_end_time = timeit.default_timer()

        print(f"Result with Sort: {result_with_sort}. completed in {result_with_sort_end_time - result_with_sort_start_time} seconds ")
        print(f"Result without Sort: {result_without_sort}. completed in {result_without_sort_end_time - result_without_sort_start_time} seconds ")

if __name__ == '__main__':
    main()
