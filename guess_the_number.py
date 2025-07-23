import random

def search_number(list_numbers, number):
    low = 0
    high = len(list_numbers) - 1 
    steps = 0

    while low <= high:
        steps += 1 
        mid = int((low + high) / 2)
        attempt = list_numbers[mid]

        if attempt == number:
            return mid, steps
        if attempt > number:
            high = mid - 1 
        else:
            low = mid + 1
    return None, steps

low_range = int(input("The lowest value on the list is ? "))
high_range = int(input("The highest value on the list is ? ")) + 1
list_numbers = [i for i in range(low_range,high_range)]

random_number = random.randint(low_range,high_range)
result, num_steps = search_number(list_numbers,random_number)

print(f"The secret number is: {random_number}")
print(f"The result is: {result+1} in {num_steps} steps")
