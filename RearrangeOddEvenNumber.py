def rearrange_odd_even_number(input_list):
    even_index = 0
    odd_index = 1

    for i in range(len(input_list)):

        if i % 2 == 0 and odd_index < len(input_list):

            while input_list[i] % 2 == 0 and odd_index < len(input_list):

                if input_list[odd_index] % 2 != 0:
                    temp_var = input_list[odd_index]
                    input_list[odd_index] = input_list[i]
                    input_list[i] = temp_var


                else:
                    odd_index = odd_index + 2

        elif i % 2 != 0 and even_index < len(input_list):
            while input_list[i] % 2 != 0 and even_index<len(input_list):
                if input_list[even_index] % 2 == 0:
                    temp_var = input_list[even_index]
                    input_list[even_index] = input_list[i]
                    input_list[i] = temp_var

                else:
                    even_index = even_index + 2

    print (input_list)


if __name__ == "__main__":
    input_list = [1,3,5,7,2,4,6,8]
    rearrange_odd_even_number(input_list)
