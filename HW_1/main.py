import sort_1
import sort_2

def main():
    numbers_1 = [ 1,4,6,7,8,0,2,1,6,3,9, 4]
    numbers_i = sort_1.sort_list_imperative(numbers_1)
    print("императивный ")
    print(sort_1.reverse(numbers_i))
    
    
    numbers_2 = [ 1,4,6,7,8,0,2,1,6,3,9,11]
    numbers_i2 = sort_2.sort_list_declarative(numbers_2)
    print("декларативный")
    print(numbers_i2)
    
if __name__ == '__main__':
    main()

