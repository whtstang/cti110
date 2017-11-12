speed = float(input('What is the speed of the vehicle in mph? ',))

print()

time = int(input('How many hours has it travled? '))

print()

print("Hour","\tDistance Traveled")

print("--------------------------")

for hour in range(1, time + 1):
    distance = speed * hour
    print(hour,"\t", distance)

            

