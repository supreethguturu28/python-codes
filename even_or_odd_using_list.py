# res = [{'even':[2,4,6,8], 'odd':[1,3,5,7]}]

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
even_list = []
odd_list = []


def even_odd_function(num_list_in):
    for x in num_list_in:
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)

    rand_dict = {'Even': even_list, 'Odd': odd_list}

    return rand_dict


print("\nThe Dictionary is:", even_odd_function(num_list))
