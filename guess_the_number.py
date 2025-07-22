def search_number(list_numbers, number):
    low = 0
    high = len(list_numbers) - 1 

    while low <= high:
        mid = (low + high) / 2
        attempt = list_numbers[mid]

        if attempt == number:
            return mid
        if attempt > number:
            high = mid - 1 
        else:
            low = mid + 1
    return None

low_range = int(input("The lowest value on the list is ? "))
high_range = int(input("The highest value on the list is ? ")) + 1

list_numbers = [i for i in range(low_range,high_range)]
print(list_numbers)