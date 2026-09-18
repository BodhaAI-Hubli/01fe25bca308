#Read the two numbers from the user
a=int(intput("Enter first number: "))
b=int(intput("Enter second number: "))

#Display values before swapping
print("Before Swapping: ")
print("First number:",a )
print("Second number:",b)

#Swapp the values
a,b = b,a

#Display values after swapping
print("After Swapping: ")
print("First number: ",a)
print("Second number: ",b)