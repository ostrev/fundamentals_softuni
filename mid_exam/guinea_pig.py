food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())

for day in range(1, 31):
    if food >= 0.3:
        food -= 0.3
    else:
        print("Merry must go to the pet store!")
        exit()

    if day % 2 == 0:
        if hay >= food * 0.05:
            hay -= food * 0.05
        else:
            print("Merry must go to the pet store!")
            exit()

    if day % 3 == 0:
        if cover >= weight/3:
            cover -= weight/3
        else:
            print("Merry must go to the pet store!")
            exit()
print(f"Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.")


