std_heights = input("Enter height of each student: ").split()

for each_std_height in range(0, len(std_heights)):
    std_heights[each_std_height] = int(std_heights[each_std_height])
print(std_heights)

count = 0
sum_of_heights = 0

for n in std_heights:
    sum_of_heights += n
    count += 1

average_height = round(sum_of_heights / count)

print(f"Students average height is {average_height}")
