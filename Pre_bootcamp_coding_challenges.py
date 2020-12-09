# Mukovhe Lugisani


# Task 1
# Values of x and y

x = 0
y = 1

# Printing the values of x and y
print("The value of x is " + str(x))
print("The value of y is " + str(y))

# Updating the values of x and y
x = x + 3
y = y + 3

# Printing new values of x and y
print("The value of x is " + str(x))
print("The value of y is " + str(y))


# Task 2
# DODMAS RULE

x = 1 + 1 * 2
print("Multiplication comes before addition, so 1 * 2 gives us 2, then 2 + 1 gives us " + str(x))

y = (1 + 1) * 2
print("Brackets comes before multiplication, so (1 + 1) gives us 2, then 2 * 2 gives us " + str(y))

z = 1 + ( 1 * 2 )
print("Brackets comes before addition, so (1 * 2) gives us 2, then 1 + 2 gives us " + str(z))

a =  1 + 1 * 2 / 2
print("Division comes first, multiplication 2nd and addition last,  so 2/2 gives us 1, 1 * 1 gives us 1, then 1 + 1 gives us " + str(a))

b =  (1 + 1 * 2 ) /  2
print("Brackets comes before division, so (1 + 1 * 2) gives us 3, then 3 / 2 gives us " + str(b))


# Task 3
# Write a function that takes 2 numbers as input. If either of the numbers is 65, OR if the sum of the numbers is 65 then return true. Otherwise return false.

def number_65 (a, b):
    if ((a == 65) | (b == 65)) | (a + b == 65):
        return True
    else:
        return False
    
print(number_65(65,48))
print(number_65(60,4))
print(number_65(55,10))


# Task 4
# Write a function that takes 2 numbers as input. If either of the numbers is 3 AND the sum of the numbers contains a 3 then return true. Otherwise return false


def number_3(x, y):
    
    a = 0
    test = ['3'] # we use this variable to check if the sum containns 3
    
    sum_of_x_and_y = list(str(x + y)) # to compute the sum and break in into pieces, i.e. 33 becomes ['3','3']
    
    for test in sum_of_x_and_y:
        a += 1
    
        if (a >= 1) & ((x == 3) | (y == 3)):
            return True #return true if the sum contains at least one 3 and either of the numbers(x or y) is 3
        
        else:
            return False

# Example  
print(number_3(3,30))
print(number_3(9,4))
print(number_3(10,3))


# Task 5
# Write a function that takes in three numbers. These numbers represent the lengths of the sides of a triangle. The function should return the area of a triangle.

def triagle_area (p1, p2, p3):
    s = (p1 + p2 + p3)/2
    area = (s*(s-p1)*(s-p2)*(s-p3))**(1/2)
    return area

# Example
a = 3
b = 4
c = 3

# Assuming that the measurements are given in meters
print("The area of a triangle with three sides of length " + str(a) + "m, " + str(b) + "m, and " + str(c) + "m is " + str(triagle_area(a,b,c)) + " square meters.")


# Task 6
# White a function that takes in three numbers and returns the maximum number. Do this without using any builtin methods. Write your own logic from scratch.

def maximum (a, b, c):
    value = 0
    
    if (a > b) & (a > c):
        value = a
        return value
    elif (b > a) & (b > c):
        value = b
        return value
    else:
        value = c
        return value

# Example
a, b, c = 2, 8, 6

print("The maximum of " + str(a) + ", " + str(b) + ", and " + str(c) + " is "+ str(maximum(a, b, c)))


# Bonus: How can you change the code so it can take in any number of numbers?

def advaced_maximum (*args):
    maximum_value = 0
    numbers = list(args)
    
    for i in numbers:
        if i > maximum_value:
            maximum_value = i
    return maximum_value

# Example
a, b, c, d, e = 26, 18, 79, 20, 43

print("The maximum of " + str(a) + ", " + str(b) + ", "+ str(c) + ", " + str(d) + ", and " + str(e) + " is "+ str(advaced_maximum(a, b, c, d, e)))


# Task 7
# Write a function that takes in a number representing the temperature in Celsius and returns the temperature in Fahrenheit. Write another function that does the opposite (Fereignheit to Celsius)

def temparature_in_Fereignheit (Celsius):
    Fereignheit = (Celsius * 9/5) + 32
    return Fereignheit

def temparature_in_Celsius (Fereignheit):
    Celsius = (Fereignheit - 32) * 5/9
    return Celsius

# Example
temp_in_celsius = 39
temp_in_fereignheit = 102.2
#Change values to find other temparatures

print(str(temp_in_celsius) + " degree celsius is equal to " + str(temparature_in_Fereignheit(temp_in_celsius)) + " fereignheit.")
print(str(temp_in_fereignheit) + " fereignheit is equal to " + str(temparature_in_Celsius(temp_in_fereignheit)) + " degree celsius.")


# Task 8
# Make a function to convert any number into hours and minutes. (For example, 71 will become 1 hour, 11 minutes; 133 will become 2 hours, 13 minutes.)


def time (x):
    if x < 0:
        print("Enter a positive number")
    
    elif (x == 0) | (x == 1):
        print(str(x) + " minute")
        
    elif (x > 1) & (x < 60):
        print(str(x) + " minutes")
        
    elif x >= 60:
        h = int(x/60) # this gives us the number of hours
        m = x % 60 # the remainder of x gives us number of minutes
        
        if (h < 2) & (m < 2):
            print(str(h) + " hour, " + str(m) + " minute")
        
        elif (h < 2) & (m >= 2):
            print(str(h) + " hour, " + str(m) + " minutes")
        
        elif (h >= 2) & (m >= 2):
            print(str(h) + " hours, " + str(m) + " minutes")
        
        else:
            print(str(h) + " hours, " + str(m) + " minute")
        
# Example
time(1)
time(2)
time(60)
time(61)
time(63)
time(121)
time(350)


# Task 9
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.

i = 3
a = 5

sum_of_multiples_of_3 = 0
sum_of_multiples_of_5 = 0
sum_of_common_numbers = 0

multiples_of_3 = []
multiples_of_5 = []

# multiples of 3 below 1000.
while i < 1000:
    multiples_of_3 += [i]
    sum_of_multiples_of_3 += i
    i += 3

# multiples of 5 below 1000.
while a < 1000:
    multiples_of_5 += [a]
    sum_of_multiples_of_5 += a
    a += 5

# multiples of 3 and 5 below 1000 that are equal.
for i in multiples_of_3:
    if i in multiples_of_5:
        sum_of_common_numbers += i 

sum_of_multiples = sum_of_multiples_of_3 + sum_of_multiples_of_5 - sum_of_common_numbers  # we don't want to count common multiples of 3 and 5 twice     
print(sum_of_multiples)


# Task 10
# Write a function that takes in a string and then prints out all the vowels in the string. Make sure it can deal with capital letters and small letters.

vowels = ['A','a','E','e','I','i','O','o','U','u']

def vowel (x):
    values = []
    
    for i in x:
        if i in vowels:
            values += [i]
            
    print('Vowels: ')
    for i in range(len(values)):
        print(values[i], end = " ")
            
vowel('Orange')


# Task 11
# Make a function that takes two strings as input, and outputs the common characters/letters that they share. (For example, Input: ‘house’, ‘computers’ . Output: ‘Common letters: o, u, e, s’)

def common_characters(x, y):
    letters = []
    
    for i in x:
        if i in y:
            letters += [i]
            
    print('Common letters: ')
    for i in range(len(letters)):
        print(letters[i], end = " ")
        
# Example
common_characters('alice', 'david')
