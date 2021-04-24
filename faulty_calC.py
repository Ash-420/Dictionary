# 45*3=555 56+9=77 56/6=4

print('Enter 1st number:')
num1 = int(input())
print('Enter 2nd number:')
num2 = int(input())
print('Choose the operation\n * , + , /:')
num3 = input()

if (num1 == 45 and num2 == 3 and num3 == '*'):
    print('666')
elif (num1 == 56 and num2 == 9 and num3 == '+'):
    print('77')
elif (num1 == 56 and num2 == 6 and num3 == '/'):
    print('4')
elif (num3 == '*'):
    print(num1*num2)
elif (num3 == '+'):
    print(num1+num2)
elif (num3 == '/'):
    print(num1/num2)
else:
    print('Error!')
