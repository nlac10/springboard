# user_input = input("Please enter product info: ")

def unique_products(str):

    # reads in file and returns list via .split()
    # before making list, make sure to remove whitespaces
    # lower case
    # what about punctuations? ## should learn how to do error handling
    with open(str,"r") as file:
        text = file.read()
        products = text.lower().strip().split("\n")
        # return products
        # >>> outputs:
        # ['ball 5 2', 'box 10 5', 'ball 10 3.5', 'ball 5 2', '']

        # return products
        # >>> output:
        # ball 5 2
        # box 10 5
        # ball 10 3.5
        # ball 5 2

    # make each item in list a list
    prod_list = [items.split() for items in products]
    # return prod_list
    # >>> outputs:
    # [['ball', '5', '2'],
    # ['box', '10', '5'],
    # ['ball', '10', '3.5'], ['ball', '5', '2']]

    # cast while you're making each a tuple!
    prod_details = []
    for item in prod_list:
        tup_specs = (item[0], int(item[1]), float(item[2]))
        prod_details.append(tup_specs )
        # >>> TypeError: list indices must be integers or slices, not list
        # for specs in items:
        # return specs
        # return prod_list[items]
    #         tuple = (str÷(items[0]), int(items[1]), float(items[2]))
    #         # >>> TypeError: 'str' object is not callable
    #         prod_details.append(tuple)
    #
    # return prod_details
    # >>> outputs:
    # [('ball', 5, 2.0), ('box', 10, 5.0), ('ball', 10, 3.5), ('ball', 5, 2.0)]

    # you CANNOT change anything about a tuple once it's set
    # WRONG ... you can do what Charles did... see above
    # prod_list = [tuple(items.split()) for items in products]
    # return prod_list
    # >>> outputs:
    # [('ball', '5', '2'), ('box', '10', '5'),
    # ('ball', '10', '3.5'), ('ball', '5', '2')]

    # for specs in prod_list[specs]:
        # return type(specs)
        # prod_list[specs][1] = int(prod_list[specs][1])
        # prod_list[specs][2] = float(prod_list[specs][2])

    # return prod_list[0][0]
    # >>> output:
    # "ball"

    return len(set(prod_details))

print(unique_products("product_dupes.txt"))
