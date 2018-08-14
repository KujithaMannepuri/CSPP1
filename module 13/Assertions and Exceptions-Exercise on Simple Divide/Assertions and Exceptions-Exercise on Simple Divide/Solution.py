'''fancy divide'''
#define the simple_divide function here
def simple_divide(item, denom):
    '''fancy divide'''
    # start a try-except block
    try:
        return item / denom
    except ZeroDivisionError:
        return 0
def fancy_divide(list_of_numbers, index):
    '''fancy divide'''
    denom = list_of_numbers[index]
    return [simple_divide(item, denom) for item in list_of_numbers]
def main():
    '''fancy divide'''
    data = input()
    num1 = data.split()
    lst1 = []
    for j in num1:
        lst1.append(float(j))
    s_1 = input()
    index = int(s_1)
    print(fancy_divide(lst1, index))
if __name__ == "__main__":
    main()
