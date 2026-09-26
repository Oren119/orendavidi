def say_goodbye(name):
    print("Goodbye,", name + "!")

def area_of_circle(radius):
    area = 3.14 * radius ** 2
    print (area)

def subtract(num1, num2):
    minus = num1 - num2
    return minus

def multiply(num1, num2):
    product = num1 * num2
    return product

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero."
    else:
        quotient = num1 / num2
    return quotient

temperature = [72, 75, 79, 80, 68, 74, 77]
def what_should_i_wear(temperature):
    if max(temperature):
        return "It's hot outside, wear shorts and a t-shirt."
    if min(temperature):
        return "It's cold outside, wear long pants and a jacket."
    return (min,max)

def day_of_week(int):
    if int == 6 or int == 7:
        return True
    else:
        return False

def fuel_efficiency(miles, gallons):
    fuel_efficient = miles/gallons
    return fuel_efficient

def encrypt(int):
    last_digit = int % 10
    remaining = int // 10
    return last_digit * (10 ** len(str(remaining))) + remaining

def power_function(x,y):
    result = 1
    for i in range(y):
        result = result*x
    return result

def find_minimum(int):
    min = int[0]
    for i in range(len(int)):
        if int[i] < min:
            min = int[i]
    return min
def find_maximum(int):
    max = int[0]
    for i in range(len(int)):
        if int[i] > max:
            max = int[i]
    return max

def minimum(int):
    min = int[0]
    i=1
    while i<len(int):
        if int[i]<min:
            min=int[i]
        i+=1
    return min
def maximum(int):
    max = int[0]
    i = 1
    while i < len(int):
        if int[i] > max:
            max = int[i]
        i += 1
    return max

def calc_sum(int):
    total=0
    while int > 0:
        total+= int %10
        int//=10
    return total

num1 = 3
num2 = 8
result = subtract(num1, num2) #num2 minus num1
print(f"The result of Subtract (4.1) with num1 = 3 and num2 = 8 is -5.")