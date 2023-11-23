# tian = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸"]
# di=["子","丑","寅","卯","辰","已","午","未","申","酉","戌","亥"]
# basey=2000
# basetian=6
# basedi= 4
# year=int()
# print(tian[ ( basetian + ( year - basey) ) %10 ] , sep = "" , end = "")
# print(di[ ( basedi +  ( year - basey )) %12 ] )
# a=round(3.6555,1)
# tian.insert(1145,1)
# import math as 1_a1
# print(1_a1.factorial(6))
# input("请输入年份:")

# print("请输入年份:",end="",sep="")
# input()



# height=float(input("请输入身高(m):"))    #输入身高 height
# weight=float(input("请输入体重(kg):"))   #输入体重 weight
# bmi= weight/height**2                   #根据公示计算 BMI 指数
# print("BMI=",bmi)                       #输出 BMI 指数

# temperature=38
# if temperature>=40:
#     print("高温红色预警")
# elif temperature>=37:
#     print("高温橙色预警")
# elif temperature>=35:
#     print("高温黄色预警")
# else:
#     print("请注意防暑降温")


# print("1start.")
# for i in range(1,11):  ###
#     print(i*i)
# print("1done.")


# print("2start.")
# i=1                 ###
# while i*i<=100:          ###
#     print(i*i)
#     i=i+1           ###
# print("2done.")

# # 输入两个整数
# num1 = 48
# num2 = 248

# if num1>num2:
#     num1,num2=num2,num1
# # 辗转相除法
# times=0
# while num2 != 0:
#     remainder = num1 % num2
#     num1 = num2
#     num2 = remainder
#     times=times+1

# # 输出最大公约数
# print("最大公约数是：", num1)
# print("执行次数",times)

# alst=[1,2,3,4,5]
# total=len(alst)
# i=0
# while i<total:
#     print(alst[i],"的平方是:",alst[i]*alst[i])
# i=i+1

# # alst=[1,2,3,4,5]
# # for i in alst:
# #     print(i,"的平方是:",i*i)

# import pandas as pd
# df=pd.read_csv('test.csv',encoding="ANSI")  #读取 test.csv 文件
# mydf=df.drop_duplicates(subset=['bike id','datetime'],keep='first',inplace = True)
# #去除 bike id 和 datetime 的重复数据
# print(df)

# import pandas as pd
# df = pd.read_csv('test. csv', encoding = "ANSI")    #读取 test.csv 文件
# mydf = df.dropna(axis = 0, inplace = True)          #处理缺失值,按行删除
# print(df)

# import numpy as np
# import pandas as pd
# df= pd.read_csv('test.csv', encoding ="ANSI")#读取 test.csv 文件
# count = df[(df['year_month'] >= '06-21-00') & (df['year_month']<= '06-21-23') & (df['local_name'] =='图书馆')]
# #选出日期是 6月21 日且地点是“图书馆”的数据集
# thiscount =pd.read_csv('test.csv', encoding ="ANSI")[1]['year_month'].value_counts()#按照时间进行频数统计
# print(thiscount)
# print(np.max(thiscount))#查看 6 月 21 日一天中共享单车单位时间内的最大开锁量
# print(np.sum(thiscount))#查看 6 月 21 日一天中共享单车的开锁总量

# import numpy as np
# import matplotlib.pyplot as plt
# data = np.arange(0,1.1,0.1)#在 [0,1.1)区间内,以 0.01 为间隔,创建
# plt. title('lines')
# plt. xlabel('x')
# plt. ylabel('y')
# plt. xlim((0, 1))
# plt. ylim( (0, 1))
# plt.xticks([0,0.2,0.4,0.6,0.8,1])
# plt.yticks([0,0.2,0.4,0.6,0.8,1])
# plt.plot(data, data ** 2)
# plt.plot(data, data ** 4)
# plt.legend(['y = x^2', 'y = x^4'])
# plt.show()

# import matplotlib.pyplot as plt
x= [1,2,3,4,8,25]
print(x[2])
min_x=min(x)
idx=x.index(min_x)

# plt. title('Box Plot')
# plt.boxplot(x,whis)
# plt. show()

import pandas as pd
import matplotlib. pyplot as plt
plt. rcParams['font. sans-serif' ] =  ['SimHei']#支持中文，用于正常显示中文标签
mydf = pd.read_csv('test.csv', encoding ="ANSI")#读取 test.csv 文件
plt.title('某区图书馆附近一天的共享单车流量')
plt.xlabel('小时')
plt.ylabel('总计')
ax = plt.plot(mydf['index'] , mydf['count'] , linewidth = 2)#绘制折线图
plt. xticks([0, 1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16.17, 18, 19,20, 21, 22, 23])
plt. show()

# 下行 1000Mbps
# 上行 200Mbps
# Mbps=bit per second
# MB/s=MegaByte per second

