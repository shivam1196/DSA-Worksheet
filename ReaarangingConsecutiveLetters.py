def rearrange_consecutive_letters(input_list):
    for i in range(len(input_list)):
        input_list[i] = ord(input_list[i])

    sorted_list = merger_sort(input_list)
    unique_element_number = total_unique_element(sorted_list)

    swap_spot_lists = find_swap_spots(input_list)

    unique_frequency_list = frequency_counter(sorted_list)

    unique_element_list = unique_elements_list(sorted_list)

    if unique_element_number - len(swap_spot_lists) != 3:
        if unique_element_number == 3 and len(swap_spot_lists) >= 1:
            return special_case_handling(swap_spot_lists,unique_frequency_list,unique_element_list,input_list)

        else:
            rearranged_list = rearrange_characters(unique_element_list, unique_frequency_list)
            return rearranged_list



    else:
        return -1


def merger_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid_element = len(input_list) // 2

    left = input_list[:mid_element]

    right = input_list[mid_element:]

    left = merger_sort(left)

    right = merger_sort(right)

    sorted_list = merge_sorted_list(left, right)

    return sorted_list


def merge_sorted_list(left, right):
    merged_list = []

    left_index = 0

    right_index = 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] > right[right_index]:
            merged_list.append(right[right_index])
            right_index += 1

        else:
            merged_list.append(left[left_index])
            left_index += 1

    merged_list += left[left_index:]

    merged_list += right[right_index:]

    return merged_list


def total_unique_element(input_list):
    unique_count = 1

    for i in range(1, len(input_list), 1):
        if input_list[i] != input_list[i - 1]:
            unique_count += 1

    return unique_count


def special_case_handling(swap_spot_list, frequency_list, unique_element_list, input_list):
    final_result = ""

    final_result = final_result + chr(input_list[swap_spot_list[0]+1]) * frequency_list[
        chr(input_list[swap_spot_list[0]+1])]

    unique_element_list.remove(chr(input_list[swap_spot_list[0]+1]))

    final_result = unique_element_list[0] * frequency_list[unique_element_list[0]] + final_result + unique_element_list[
        1] * frequency_list[unique_element_list[1]]

    return final_result


def find_swap_spots(input_list):
    swap_spots_list = []

    for i in range(0, len(input_list) - 1, 1):
        if input_list[i + 1] - input_list[i] > 1:
            swap_spots_list.append(i)

    return swap_spots_list


def rearrange_characters(unique_element_list, frequency_list):
    final_result = ""

    for i in range(1, len(unique_element_list), 2):
        final_result = final_result + unique_element_list[i] * frequency_list[unique_element_list[i]]

    for j in range(0, len(unique_element_list), 2):
        final_result = final_result + unique_element_list[j] * frequency_list[unique_element_list[j]]

    return final_result


def frequency_counter(input_list):
    unique_number_count = 0
    frequency_list = {}
    frequency_list[chr(input_list[0])] = 1

    for i in range(1, len(input_list), 1):
        if (input_list[i] != input_list[i - 1]):
            unique_number_count += 1
            frequency_list[chr(input_list[i])] = 1
        else:
            frequency_list[chr(input_list[i])] = frequency_list.get(chr(input_list[i])) + 1

    return frequency_list


def unique_elements_list(sorted_list):
    unique_elements_list = []
    unique_elements_list.append(chr(sorted_list[0]))
    for i in range(1, len(sorted_list)):
        if (sorted_list[i] != sorted_list[i - 1]):
            unique_elements_list.append(chr(sorted_list[i]))

    return unique_elements_list


def convert_ascii_to_character(input_list):
    for i in range(len(input_list)):
        input_list[i] = chr(input_list[i])

    return input_list


if __name__ == "__main__":
    print rearrange_consecutive_letters(["a", "d", "d", "b", "b"])
