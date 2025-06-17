# Write a program to print even numbers from 1 to 100 using for loop.

# take input range from 1 to 100
for num in range(1, 101):

    # when number divided by two gives remainder as zero it is even
    if num % 2 == 0:
        print(num)