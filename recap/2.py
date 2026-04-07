# x= int(input("Enter a number: "))
# if x<10:
#     print("x is less than 10")
# elif x==10:
#     print("x is equal to 10")
# else:    print("x is greater than 10")


def is_even(n):
    if n%2==0:
        return True
    else:
        return False
    

num = int(input("Enter a number: "))

print(is_even(num))    