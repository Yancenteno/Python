num1 = 42 #int, variable declaration, numbers
num2 = 2.3 #float, variable declaration, numbers
boolean = True #Boolean
string = 'Hello World' #string, variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalapeños', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}#Dictionaries
fruit = ('blueberry', 'strawberry', 'banana')#tuples
print(type(fruit))#tuple
print(pizza_toppings[1])#access value from list
pizza_toppings.append('Mushrooms')#add value
print(person['name'])#access value from dictionary
person['name'] = 'George'#change value from dictionary 
person['eye_color'] = 'blue'#adds value from dictionary
print(fruit[2])#access value from tuple
print(person)

if num1 > 45:#num1 is less than
    print("It's greater")#will not print
else:#will run this line instead
    print("It's lower")#will print

if len(string) < 5:#gets the "length of the "string", string is equal to 11
    print("It's a short word!")#will skip
elif len(string) > 15:#11 is less than 15
    print("It's a long word!")#will skip
else:#activates after nothing else is not accepted
    print("Just right!")#prints

for x in range(5):#gets the number range starting from 0 and ending at 4
    print(x)# prints 0,1,2,3,4
for x in range(2,5):#gets the number range starting from 2 and ending at 4
    print(x)# prints 2,3,4
for x in range(2,10,3):#starts the range from 2 and adds 3 until its less than 10
    print(x)#prints 2, 5, 8
x = 0
while(x < 5):#while loop, loop continues while x is less than 5
    print(x)#prints 0,1,2,3,4
    x += 1#adds on to x and runs loop again

pizza_toppings.pop()#deletes the last value of the list
pizza_toppings.pop(1)#deletes the (1) value of the list

print(person)#prints the full dictionary
person.pop('eye_color')#removes 'eye_color' from dictionary
print(person)#prints {'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

for topping in pizza_toppings:
    if topping == 'Pepperoni':#boolean
        continue #continue stops the boolean above
    print('After 1st if statement')# prints 'After 1st if statement''After 1st if statement''After 1st if statement'
    if topping == 'Olives':#boolean
        break#for loop keeps running until toppings == Olives and stops the whole loop


def print_hello_ten_times():#parameter
    for num in range(10):#argument
        print('Hello')#return

print_hello_ten_times()#calls function

def print_hello_x_times(x):#parameter
    for num in range(x):#argument
        print('Hello')#return

print_hello_x_times(4)#calls function

def print_hello_x_or_ten_times(x = 10):#parameter
    for num in range(x):#argument
        print('Hello')#return

print_hello_x_or_ten_times()#calls function
print_hello_x_or_ten_times(4)#calls function


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)