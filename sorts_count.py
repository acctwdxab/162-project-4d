# Dan Wu
# 1/26/2021
# 4d - Write a bubble sort that counts the number of comparisons and the number of exchanges made while sorting a list and
# returns a tuple of the two values (comparisons first, exchanges second). Do the same for insertion sort.
# Name these functions bubble_count and insertion_count. Your functions should only count comparisons between the values that are being sorted.


def bubble_count(a_list):
    """
    Function that bubble sorts the number of comparisons and exchanges
    and returns a tuple of the two values
    """
    comparisons = 0
    exchanges = 0


    for i in range(len(a_list)):
        for j in range(len(a_list) - i - 1):

            comparisons += 1

            if a_list[j] > a_list[j + 1]:
                # swap elements
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                exchanges += 1

    return comparisons, exchanges


def insertion_count(a_list) :
    """
    Function that bubble sorts the number of comparisons and exchanges
    and returns a tuple of the two values
    """
    comparisons = 0
    exchanges = 0
    for i in range ( 1 , len ( a_list ) ) :
        key = a_list[i]
        j = i - 1
        comparisons += 1
        while j >= 0 and key < a_list[j] :

            a_list[j + 1] = a_list[j]
            j -= 1
            exchanges += 1
        a_list[j + 1] = key
    return comparisons , exchanges

print ( insertion_count ( list ( range ( 10 , 0 , -1 ) ) ) )