# 1. Large Power:

def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False

print(large_power(10,10))     # Returns True

print(large_power(5,5))       # Returns False



# 2. Over Budget:

def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if (budget < food_bill + electricity_bill + internet_bill + rent):
        return True
    else:
        return False

print(over_budget(100, 20, 30, 10, 40))     # Returns False

print(over_budget(1000,500,500,500,500))    # Returns True



# 3. Twice As Large:

def twice_as_large(num1, num2):
    if (num1 > (2 * num2)):         # Do not need parentheses on this line. I just like them. Lol.
        return True
    else:
        return False

print(twice_as_large(10, 5))        # Returns False

print(twice_as_large(11, 5))        # Returns True



# 4. Divisible By Ten:

def divisible_by_ten(num):
    if (num % 10 == 0):
        return True
    else:
        return False

print(divisible_by_ten(100))        # Returns True

print(divisible_by_ten(99))         # Returns False



# 5. Not Sum To Ten:

def not_sum_to_ten(num1, num2):
    if (num1 + num2 != 10):
        return True
    else:
        return False

print(not_sum_to_ten(9, -1))        # Returns True

print(not_sum_to_ten(9, 1))         # Returns False

print(not_sum_to_ten(5,5))          # Returns False