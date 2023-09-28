#puzirkom
def sort_list_imperative(numbers: list):
    for i in range(len(numbers)-1, 0, -1):
        for j in range(0, i):
            if numbers[j]>numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
    
    return numbers

def reverse(numbers: list):
    k = len(numbers)/2
    for i in range(len(numbers) - 1, int(k)-1, -1):
        temp = numbers[len(numbers)-i]
        numbers[len(numbers)-1-i] = numbers[i] 
        numbers[i] = temp
    return numbers


numbers_2 = [ 0, 1, 1, 2, 3, 4, 8]
print(reverse(numbers_2))
print(numbers_2)