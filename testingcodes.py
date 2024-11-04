class ArithmeticOp:
    def sum(self):
        x = 20
        y = 30
        return x + y

    def mul(self):
        a = 20
        b = 5
        return a * b

    def sub(self):
        p = 100
        q = 50
        return p - q

    def div(self):
        a = 100
        b = 5
        if b != 0:
            return a / b
        else:
            return "Division by zero is not allowed."

    def mod(self):
        a = 100
        b = 30
        return a % b

    def even_odd(self, num):
        return "Even" if num % 2 == 0 else "Odd"

    def pos_negative(self, num):
        return "Positive" if num >= 0 else "Negative"

    def fact(self, n):
        if n < 0:
            return "Factorial not defined for negative numbers."
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result

    def perimeter_circle(self, radius):
        from math import pi
        return 2 * pi * radius

    def interest_calc(self, principal, rate, time):
        return (principal * rate * time) / 100

    def celsius_to_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def bmi_calc(self, weight, height):
        if height <= 0:
            return "Height must be greater than zero."
        bmi = weight / (height ** 2)
        return bmi

    def speed_calc(self, distance, time):
        if time <= 0:
            return "Time must be greater than zero."
        return distance / time

    def discount_calc(self, original_price, discount_percentage):
        return original_price - (original_price * discount_percentage / 100)


class StringHandling:
    def prime_no(self, num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def mobile_no_validation(self, mobile_number):
        if len(mobile_number) == 10 and mobile_number.isdigit():
            return True
        else:
            return False


# Example usage
arithmetic = ArithmeticOp()
print(arithmetic.sum())
print(arithmetic.mul())
print(arithmetic.sub())
print(arithmetic.div())
print(arithmetic.mod())
print(arithmetic.even_odd(4))
print(arithmetic.pos_negative(-5))
print(arithmetic.fact(5))
print(arithmetic.perimeter_circle(5))
print(arithmetic.interest_calc(1000, 5, 2))
print(arithmetic.celsius_to_fahrenheit(0))
print(arithmetic.bmi_calc(70, 1.75))
print(arithmetic.speed_calc(100, 2))
print(arithmetic.discount_calc(200, 20))

string_handling = StringHandling()
print(string_handling.prime_no(11))
print(string_handling.mobile_no_validation("1234567890"))