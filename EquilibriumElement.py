def find_equilibrium_element(input_list):
    
    left_product = [1] * len(input_list)
    right_product = [1] * len(input_list)

    for index in range(1, len(input_list)):
        left_product[index] = left_product[index-1] * input_list[index - 1]
    
    for index in range(len(input_list) - 2, -1, -1):
        right_product[index] = right_product[index + 1] * input_list[index + 1]

    print(left_product, right_product)

    for index in range(len(input_list)):
        if left_product[index] == right_product[index]:
            return index
    
    return -1


if __name__ == "__main__":
    print(find_equilibrium_element([-24, 1, 6, 1, -4, 1, 1]))
