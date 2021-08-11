original = int(input('Please enter the number: '))
print("Original:   ", original)

reversed = 0
sum_digits = 0

while original > 0:
    last_digit = original % 10
    reversed = reversed*10 + last_digit
    sum_digits += last_digit
    original = int(original/10)

print("Reversed:   ", reversed)
print("Sum digits: ", sum_digits)
