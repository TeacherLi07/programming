with open('1.txt', 'r') as f:
    num_list = f.readline().strip().split()
    num_list = [int(num) for num in num_list]
    sum_nums = sum(num_list)
print("列表中所有整数之和为:", sum_nums)
