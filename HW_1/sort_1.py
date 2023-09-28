#puzirkom
def sort_list_imperative(numbers: list):
    for i in range(len(numbers)-1, 0):
        for j in range(len(numbers)-i-1, 0):
            if numbers[j]>numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    return numbers