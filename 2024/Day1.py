from collections import Counter

list1 = []
list2 = []
with open("Day1.txt", "r") as file:
    for line in file:
        first, second = line.split()
        list1.append(int(first))
        list2.append(int(second))
copy1 = list1.copy()
copy2 = list2.copy()
copy1.sort()
copy2.sort()
print(sum([abs(copy1[i] - copy2[i]) for i in range(len(list1))]))

cnt = Counter(list2)
print(sum([list1[i] * cnt[list1[i]] if list1[i] in cnt else 0 for i in range(len(list1))]))