#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    finallist = []
    for t in range(list_length):
        try:
            numa = float(my_list_1[t]) if t < len(my_list_1) else 0
            numb = float(my_list_2[t]) if t < len(my_list_2) else 0
            result = num1 / num2
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except (ValueError, TypeError):
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            finallist.append(result)

    return finallist
