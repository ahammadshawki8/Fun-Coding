
num1=input("enter a number: ")
num2=input("enter another number: ")
def division(num1,num2):
    import sys
    try:
        answer= float(num1)/float(num2)
        print("the answer of the division is "+str(answer))
    except ZeroDivisionError:
        print("somthing went wrong. You are trying to divide the first value by zero")
    except ValueError:
        print("something went wrong. please insert a number, not a letter or symble")
    except:
        error=sys.exc_info()[0]
        print("something went wrong. couldn\'t perform the action.")
        print(error)
division(num1,num2)