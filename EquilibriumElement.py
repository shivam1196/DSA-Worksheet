def find_equilibrium_element(input_list):
    start_index = 0

    end_index = len(input_list) - 1

    left_product = 1
    right_product = 1

    while start_index <= end_index:

        if left_product <= right_product:
            left_product = left_product * input_list[start_index]
            start_index = start_index + 1
        if left_product == right_product and start_index == end_index:
            return start_index

        if right_product <= left_product:
            right_product = right_product * input_list[end_index]
            end_index = end_index - 1
        if left_product == right_product and start_index == end_index:
            return end_index

    return -1


if __name__ == "__main__":
    print find_equilibrium_element([6, 6, 1, 2, 2, 3, 3])
