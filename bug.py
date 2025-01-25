def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
result = calculate_average(my_list)
print(f"Average: {result}")  #Output: Average: 0

my_list = [10,20,30]
result = calculate_average(my_list)
print(f"Average: {result}") #Output: Average: 20.0

my_list = [10, 20, 'a']
result = calculate_average(my_list) #This will throw an error