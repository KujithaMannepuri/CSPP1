''' functions and objects 3'''
#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]
def square(lst):
    ''' functions and objects 3'''
    return lst*lst
def apply_to_each(lst, _):
    ''' functions and objects 3'''
    return list(map(square, lst))
def main():
    ''' functions and objects 3'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()
