#Add a variable
digit = int(input("Enter a number: "))
#Add a if-else statement
if (digit == 1) :
    a = int(input("Enter the length of the side of the square: "))
    print("The area of the square is: ", a*a)
#Add a elif statement
elif (digit == 2) :
    b = int(input("Enter the length of the side of the rectangle: "))
    c = int(input("Enter the width of the rectangle: "))
    print("The area of the rectangle is: ", b*c)
#Add a else statement
else :
    print("Invalid choice")