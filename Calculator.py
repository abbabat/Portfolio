print("$# Welcome to the calculator $#")


def preliminaire(x,y):
    order = input("please chose ur action: x , + , - , / , or //: ")
    number = ''
    if order== 'x':
        s = x * y
        number +=str(s)
    elif order == '+':
        s = x + y
        number +=str(s)
    elif order == '/':
        s = x/y
        number +=str(s)
    elif order == '//':
        s = x // y
        number +=str(s)
    

    return int(number)


def calculate(x,y):
    s = int(preliminaire(x,y))
    print(s)

    continu = input("Do you want to prossess to further calculation with the obained number? y or n: ")

    if continu == 'y':
        n = int(input("please enter a new number: "))
        return calculate(s , n)

    else: 
        return "Thank you for using the claculator"
    
print(calculate(4, 5))



