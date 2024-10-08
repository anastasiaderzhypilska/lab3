## Лабораторна робота з дисципліни "Алгоритми та структури даних"

## Виконала: Держипільська Анастасія Андріївна (ІР-14)
## Лабораторна робота №3 (Варіант 6)
## Task №1

def likes(names):
    count = 0
    for _ in names: 
        count += 1
    if count == 0:
        return "no one likes this"
    if count == 1:
        return names[0] + " likes this"
    if count == 2:
        return names[0] + " and " + names[1] + " like this"
    if count == 3:
        return names[0] + ", " + names[1] + " and " + names[2] + " like this"
    if count > 3:
        others = count - 2
        return names[0] + ", " + names[1] + " and " + str(others) + " others like this"

print(likes([]))  
print(likes(["Peter"]))  
print(likes(["Jacob", "Alex"]))  
print(likes(["Max", "John", "Mark"]))  
print(likes(["Alex", "Jacob", "Mark", "Max"]))  