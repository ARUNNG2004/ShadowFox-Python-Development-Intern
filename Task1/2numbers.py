
# 1 Function to format a string
print("--------------------task-1----------------------------")
def format_string(num, char):
    return "{:{}^10}".format(num, char)

result = format_string(145, 'o')
print(result)  # "ooo145oooo"

# The representation used here centers the number 145 in a field of width 10,
# padded by the character 'o'.
print("------------------------------------------------")
# 2  area of the pond and total water
print("---------------------task-2---------------------------")
radius = 84
pi = 3.14
area = pi * (radius ** 2)  # Circle Area = π r^2
print(f"Area of the pond: {area}")  # 22155.76

# Bonus:   total amount of water without any decimal point
water_per_square_meter = 1.4
total_water = int(area * water_per_square_meter) #  Total amount of water
print(f"Total amount of water: {total_water} liters")  # 31017 liters

print("------------------------------------------------")
# 3 Calculate speed in meters per second
print("------------------------task-3------------------------")
distance =490 # in meters
time_minutes = 7   
time_seconds = time_minutes * 60  # convert minutes to seconds

speed = int(distance / time_seconds)  # Speed = Distance / Time
print(f"Speed: {speed} meters per second")  # 1 meter per second
print("------------------------------------------------")
