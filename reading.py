num =input("enter the number: ")
for num in range (1, 10, 1):
    number= int(input("enter the number: "))

    if number % 2 !=0:
        print("it's an odd number")
    if number % 2 ==0:
        print("it's an even number")
    if number >1000:
        print("this number is greater than 1000")
    if number <= 1000:
        print("number is less than 1000")
    if number >=5 and number <=12:
        print("number is inbetween 5 and 12")


