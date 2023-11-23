import time
start_time = time.time()  # 记录开始时间
import math
import random
import matplotlib.pyplot as plt
import sys
from numba import jit

file_path = r"D:\programming\research-parking\停车数据-出入时间戳拼接&时长.txt"  # 替换为实际文件路径
with open(file_path, 'r') as file:
    content = file.read()

numbers_list = content.split()
numbers = [int(num) for num in numbers_list]
during_hours=[]
for i in range(2, len(numbers), 3):
    hour=0 if numbers[i] <= 15 else ( 1 if numbers[i] <= 60 else math.ceil(numbers[i] / 30) / 2 )
    during_hours.append(hour)

# @jit(nopython=True,fastmath=True,nogil=True)
def original_fee(halfhour):
    hour=math.ceil(halfhour)
    days = math.floor(hour / 24)
    today_limit = 80 * (1 + days)
    today_hour = hour - 24 * days
    today_nolimit = 10 * today_hour + 80 * days
    fee = min(today_limit, today_nolimit)
    return fee

# @jit(nopython=True,fastmath=True,nogil=True)
def new_fee_short(halfhour):
    hour=halfhour
    # tmp[0]+=1
    days = math.floor(hour / 24)
    today_limit = 112 * (1 + days)
    today_hour = hour - 24 * days
    today_nolimit = 14 * today_hour + 112 * days
    fee = min(today_limit, today_nolimit)
    return fee

# @jit(nopython=True,fastmath=True,nogil=True)
def new_fee_med(halfhour):
    hour=math.ceil(halfhour)
    # tmp[1]+=1
    days = math.floor(hour / 24)
    today_limit = 88 * (1 + days)
    today_hour = hour - 24 * days
    today_nolimit = 11 * today_hour + 88 * days 
    fee = min(today_limit, today_nolimit)
    return fee

# @jit(nopython=True,fastmath=True,nogil=True)
def new_fee_long(halfhour):
    hour=math.ceil(halfhour)
    # tmp[2]+=1
    days = math.floor(hour / 24)
    today_limit = 80 * (1 + days)
    today_hour = hour - 24 * days
    today_nolimit = 10 * today_hour + 80 * days
    fee = min(today_limit, today_nolimit)
    return fee

#@jit(nopython=True,fastmath=True,nogil=True)
def calc_fee():
    new=0

    for i in during_hours:
        # original += original_fee(i)
        rd_num=random.random()
        if i <= 1:
            if 0.7 >= rd_num:
                new += new_fee_short(i)
            elif  0.9>= rd_num:
                new += new_fee_med(i)
            else:
                new += new_fee_long(i)
        elif i<=4:
            if 0.8 >= rd_num:
                new += new_fee_med(i)
            elif 0.9 >= rd_num:
                new += new_fee_short(i)
            else:
                new += new_fee_long(i)
        else:
            if 0.7 >= rd_num:
                new += new_fee_long(i)
            elif 0.8 >= rd_num:
                new += new_fee_short(i)
            else:
                new += new_fee_med(i)
    return new

original=773900
all_percentage=[]
times=10000
for i in range(times):
    current_fee:float = calc_fee()
    current_percentage:float = ( current_fee / original - 1 ) *100
    all_percentage.append(current_percentage)
    print(f"{current_fee}\t{current_percentage:.2f}")
avg = sum(all_percentage) / len(all_percentage)
max_value = max(all_percentage)
min_value = min(all_percentage)
printcontent=f"\n\nAvg: {avg:.2f}%\nMax: {max_value:.2f}%\nMin: {min_value:.2f}%"
sys.stdout.write(printcontent)
end_time = time.time()  # 记录结束时间
elapsed_time = end_time - start_time
print("\n\n",f"程序运行时间：{elapsed_time} 秒")
plt.ylim((10,13))
plt.xlim((0, times))
plt.scatter(list(range(times)),all_percentage,s=3)
plt.axhline(y=avg, color='y', linestyle='--', label=f'Avg: {avg:.2f}%')
plt.axhline(y=max_value, color='r', linestyle='--', label=f'Max: {max_value:.2f}%')
plt.axhline(y=min_value, color='g', linestyle='--', label=f'Min: {min_value:.2f}%')
plt.legend()
plt.show()

# print(tmp)