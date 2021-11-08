# python program to find the largest

def great(num1,num2,num3):
    s = [num1, num2, num3]
    if (check_int_float(num1) and check_int_float(num2) and check_int_float(num3)):
        return max(s)
    elif (check_int_float(num1) and check_int_float(num2) and check_int_float(num3)):
        return max(s)
    elif (check_int_float(num1) and check_int_float(num2) and check_int_float(num3)):
        return max
    else:
        return "error"

def check_int_float(num1):
    if(type(num1)==int or type(num1)== float):
        return True
    else:
        return False


