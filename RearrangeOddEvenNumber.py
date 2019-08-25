def rearrange_odd_even_number(input_list):
    odd_index = 1
    even_index = 0
    answer_list = [0] * len(input_list)
    for number in input_list:
        if number % 2 == 0:
            answer_list[odd_index] = number
            odd_index += 2
        else:
            answer_list[even_index] = number
            even_index += 2

    return answer_list

if __name__ == "__main__":
    input_list = [1,3,5,7,2,4,6,8]
    print(rearrange_odd_even_number(input_list))
