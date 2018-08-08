''' functions and objects 2'''
#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def inc(lst):
    ''' functions and objects 2'''
    return lst+1
def apply_to_each(lst, _):
    ''' functions and objects 2'''
    return list(map(inc, lst))
def main():
    ''' functions and objects 2'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
