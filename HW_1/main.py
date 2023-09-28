import sort_1
import sort_2

def main():
    numbers_1 = [ 2,4,6,7,8,0,2,1,6,3,9]
    print(numbers_1)
    numbers_1 = sort_1.sort_list_imperative(numbers_1)
    print("императивный " + numbers_1)
    
    numbers_2 = [ 2,4,6,7,8,0,2,1,6,3,9]
    numbers_2 = sort_2.sort_list_declarative(numbers_2)
    print("декларативный" + numbers_2)
    