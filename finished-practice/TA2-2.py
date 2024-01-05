nums = input()

nums_list = nums.split(" ")

i = 0

while i < len(nums_list):
    # print(int(nums_list[i]) + 1)
    nums_list[i] = str(int(nums_list[i]) + 1)
    i += 1

print(' '.join(nums_list))
