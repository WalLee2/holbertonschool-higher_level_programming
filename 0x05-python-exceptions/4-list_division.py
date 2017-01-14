#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Function that divides each element in two different lists
    """
    div_list = []
    tracker = 0
    for i in range(0, list_length):
        try:
            num = my_list_1[i] / my_list_2[i]
        except(ZeroDivisionError):
            print ("division by 0")
            tracker = 1
        except(IndexError):
            print ("out of range")
            tracker = 1
        except(TypeError):
            print ("wrong type")
            tracker = 1
        finally:
            if tracker == 1:
                tracker = 0
                div_list.append(0)
            else:
                div_list.append(num)
    return (div_list)
