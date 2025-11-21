#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        val = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                print("wrong type")
            else:
                try:
                    val = a / b
                except ZeroDivisionError:
                    print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            res.append(val)
    return res
