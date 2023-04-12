""" def func():
    num = 1
    a = int(input("Enter number: "))
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        for i in range(1, a+1):
            num = num*i
        print(num)

func() """


# def fab (a):
    
#     if a == 0:
#         return 0
#     elif a == 1:
#         return 1
#     else:
#         return fab(a-1)*fab(a-2)

# print(fab(4))


a = input("Enter string: ")
b = a[::-1]
if b == a:
    print("palindrome")
else:
    print("Not")
    


        



    
    
