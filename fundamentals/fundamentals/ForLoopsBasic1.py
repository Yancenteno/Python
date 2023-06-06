for integers in range(0,151):
    print(integers)


m = 5
while m<=1000:
    print(m)
    m = m*5


for int in range(1,101):
    if int % 10 == 0:
        print("Coding Dojo")
    elif int % 5 == 0:
        print("Coding")
    else:
        print(int)


sum=0
for odd in range(1,500000,2):
    sum += odd
print(sum)


for even in range(2018,0,-4):
    print(even)
    


lowNum = 2
highNum = 9
multi = 3
for flexible in range(lowNum, highNum+1):
    if flexible % multi == 0:
        print(flexible)

