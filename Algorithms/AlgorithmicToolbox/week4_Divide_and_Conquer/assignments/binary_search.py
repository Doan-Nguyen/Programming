def binary_search(input_arr, input_numb):
    min_idx = 0
    max_idx = len(input_arr) - 1
    while(min_idx <= max_idx):
        mid_idx = int((max_idx + min_idx)/2)
        if (input_arr[mid_idx] == input_numb):
            return mid_idx
        elif (input_arr[mid_idx] > input_numb):
            max_idx = mid_idx - 1
        else:
            min_idx = mid_idx + 1
    return "Not found"


def boolean_binary_search(input_arr, input_numb):
    min_idx = 0
    max_idx = len(input_arr) - 1
    while(min_idx <= max_idx):
        mid_idx = int((max_idx + min_idx)/2)
        if (input_arr[mid_idx] == input_numb):
            return mid_idx
        elif (input_arr[mid_idx] > input_numb):
            max_idx = mid_idx - 1
        else:
            min_idx = mid_idx + 1
    return 0


def majority_element(input_arr):
    len_haft = int(len(input_arr)/2)
    for i in range(len(input_arr)):
        


if __name__ == "__main__":
    input_arr = [1, 3, 7, 8, 9, 12, 15]
    input_numb = 9
    tmp = binary_search(input_arr, input_numb)
    print(tmp)