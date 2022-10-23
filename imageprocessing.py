#if statement

number = 6
if number < 6:
    print("number is smaller than 6")
elif number == 6:
    print("number is equal to 6")
else:
    print("number is bigger than 6")

#while statement

while number < 6:
    print("Number is :", number)
    number= number+1

#average 
def getNumber():
    n= int(input("How many numer will be entered : "))
    a=[]
    for i in range (0,n):
        elem= int(input("enter a number : "))
        a.append(elem)
    avg = sum(a)/n
    print("Average is :",round(avg,2))

getNumber()



    
