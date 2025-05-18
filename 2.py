# task_1 : Check if number is odd or even
user_no = int(input("Enter a number:"))

x = user_no % 2

if x == 0:
    print(user_no, "is an even number")
else:
    print(user_no, "is an odd number")


#task_2 : Sum of integers from 1 to 50 using a loop
total = 0
for i in range(1,51):
    total += i

print("The sum of numbers from 1 to 50 is:", total)