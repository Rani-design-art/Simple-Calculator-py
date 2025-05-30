print('---SIMPLE CALCULATOR---')
print('1 - Add')
print('2 - Substract')
print('3 - Multiple')
print('4 - Divide')
operation = int(input('Choose an operation: '))

if(operation in [1,2,3,4]):
    num1 = int(input('Insert first number : '))
    num2 = int(input('Insert second number: '))
    if operation == 1:
        result=num1+num2
    elif operation == 2:
        result=num1-num2
    elif operation == 3:
        result=num1*num2
    elif operation == 4:
        result=num1/num2     
else:
    print('Invalid operation or numbers')

print('The result is:', result)


