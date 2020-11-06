# imports

# global vars

# functions

def print_menu():
    print('**********')
    print("Welcome - pc-calc")
    print('***************')

    print('[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divise')

    print('[5] Calculate age')

    print('[x] Exit')
    print('-' * 20)

def clear():
    print('\n\n\n\n')
    import os
    os.system ("cls")
    # HW: python clear console


# intructions
opc = ''

while(opc != 'x'): 
    clear()
    print_menu()
    opc = input("Please select an option: ")

    if(opc == '1' or opc == '2' or opc == '3' or opc == '4'):
        num1 = float(input("Please provide num1: "))
        num2 = float(input("Please provide num2: "))
        if(opc == '4' and num2 == 0):
            while(num == 0):
                print("Error, zero division not allowed")
                num2 = float(input("Please provide num2: "))

   
    if(opc == '1'):
        print(num1 + num2)
    elif(opc == '2'):
        print(num1 - num2)
    elif(opc == '3'):
        print(num1 * num2)
    elif(opc == '4'):
        print(num1 / num2)  

    input("Press Enter to continue....") 

print("Good byte!")
