scores_of_std = input("Enter scores of each student: ").split()

for each_score in range(0, len(scores_of_std)):
    scores_of_std[each_score] = int(scores_of_std[each_score])

print(scores_of_std)


highest_score = scores_of_std[0]
lowest_score = 0

for n in scores_of_std:
    if highest_score < n:
        highest_score = n
    elif lowest_score > n:
        lowest_score = n

print(f"Highest Score in class is --- {highest_score}")
print(f"Lowest Score in class is --- {lowest_score} ")
