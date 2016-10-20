fruit = ['apples', 'pears', 'kiwis', 'cherries', 'oranges']
meals = ['breakfast', 'lunch', 'dinner']

i = 0
for f in fruit:
    meal = meals[i % len(meals)]
    print f, "for", meal
    i = i + 1
