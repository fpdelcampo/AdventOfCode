safe1 = 0
with open("Day2.txt", "r") as file:
    for line in file:
        nums = [int(number) for number in line.split()]
        unsafe1 = False
        inc = nums[1] > nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) > 3 or abs(nums[i] - nums[i - 1]) < 1:
                unsafe1 = True
                break
            if inc and nums[i - 1] > nums[i] or not inc and nums[i - 1] < nums[i]:
                unsafe1 = True
                break
        if not unsafe1:
            safe1 += 1
print(safe1)

safe2 = 0
with open("Day2.txt", "r") as file:
    for line in file:
        nums = [int(number) for number in line.split()]
        inc = nums[1] > nums[0]
        unsafe2 = False
        for i in range(1, len(nums)):
            if abs(nums[i] - nums[i - 1]) > 3 or abs(nums[i] - nums[i - 1]) < 1:
                unsafe2 = True
                break
            if inc and nums[i - 1] > nums[i] or not inc and nums[i - 1] < nums[i]:
                unsafe2 = True
                break
        if unsafe2:
            for i in range(len(nums)):
                safe_with_removal = True
                removal = []
                for j in range(len(nums)):
                    if i != j:
                        removal.append(nums[j])
                inc = removal[1] > removal[0]
                for k in range(1, len(removal)):
                    if abs(removal[k] - removal[k - 1]) > 3 or abs(removal[k] - removal[k - 1]) < 1:
                        safe_with_removal = False
                        break
                    if inc and removal[k - 1] > removal[k] or not inc and removal[k - 1] < removal[k]:
                        safe_with_removal = False
                        break
                if safe_with_removal:
                    safe2 += 1
                    break
        else:
            safe2 += 1
print(safe2)