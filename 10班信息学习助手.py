#!/usr/bin/python
print("欢迎来到十班信息——学习助手")
print(":)")
jiange="====================================="
i=1
while i==1:
    print("开启什么应用？")
    print("1:计算原子电子排布与基础信息")
    print("2:模拟单恒星单行星时行星轨道")
    print("3:娱乐")
    yy0=int(input("(输入数字)开启："))
    print(jiange)
    if yy0==2:
        #=单行星轨道模拟2.0=
        print("欢迎模拟行星轨道！")
        print("使用场景：单恒星，单行星")
        print(":)")
        print("-")
        import math
        i20=1
        zuobiao2=1
        juli2=1
        sudu2=1
        shijian2=1
        zuobiao12=4
        juli12=4
        sudu12=4
        shijian12=4
        while i20==1:
            print("1:计算")
            print("2:设置")
            print("3:返回")
            xiayibu2=int(input("下一步是:"))
            print(jiange)
            if xiayibu2==1:
                print("恒星坐标恒为(0,0)，输出坐标为质点(行星)相对于恒星的坐标")
                print("输入方法为形如a*10^b的科学计数法")
                print("先输入a，后输入b")
                print("恒星质量的a不能为零")
                M12=input("恒星质量(kg)的a：")
                M22=input("恒星质量(kg)的b：")
                M2=float(M12)*10**int(M22)
                print("x,y方向坐标不可全为0")
                x12=input("质点x方向的初始坐标(m)的a：")
                x22=input("质点x方向的初始坐标(m)的b：")
                x2=float(x12)*10**int(x22)
                y12=input("质点y方向的初始坐标(m)的a：")
                y22=input("质点y方向的初始坐标(m)的b：")
                y2=float(y12)*10**int(y22)
                print("质点初速度不能为0(但可以很小)")
                Vx12=input("质点x方向初速度(m/s)的a：")
                Vx22=input("质点x方向初速度(m/s)的b：")
                Vx2=float(Vx12)*10**int(Vx22)
                Vy12=input("质点y方向初速度(m/s)的a：")
                Vy22=input("质点y方向初速度(m/s)的b：")
                Vy2=float(Vy12)*10**int(Vy22)
                print("每经过一段路程步长计算一次坐标")
                ds12=float(input("路程步长(m)的a："))
                ds22=float(input("路程步长(m)的b："))
                ds2=float(ds12)*10**int(ds22)
                G2=6.67*10**-11
                i2=1
                print("在“ok--”后输入1来计算下一次坐标")
                print("在“ok—”后输入0来结束这系列运算")
                while i2>=1:
                    Wait2=int(input("ok--"))
                    if Wait2!=0:
                        R2=math.sqrt(x2**2+y2**2)
                        a2=G2*M2/(R2**2)
                        ax2=-a2*x2/R2
                        ay2=-a2*y2/R2
                        v2=math.sqrt(Vx2**2+Vy2**2)
                        t2=(-v2+math.sqrt(v2**2+2*a2*ds2))/a2
                        Vx2=Vx2+t2*ax2
                        Vy2=Vy2+t2*ay2
                        x2=x2+ds2*Vx2/v2
                        y2=y2+ds2*Vy2/v2
                        print("第"+str(i2)+"次计算")
                        if shijian2==1:
                            print("经过"+str(round(t2,shijian12))+"秒后")
                        if zuobiao2==1:
                            print("坐标变为"+"("+str(round(x2,zuobiao12))+","+str(round(y2,zuobiao12))+")")
                        i2=i2+1
                        if juli2==1:
                            print("距离中心恒星"+str(round(R2,juli12))+"m")
                        if sudu2==1:
                            print("行星速度为"+str(round(v2,sudu12))+"m/s")
                        if shijian2==2 and zuobiao2==2 and juli2==2 and sudu2==2:
                            print("提示:所有功能已被关闭！")
                    if int(Wait2)==0:
                        i2=0
            if xiayibu2==2:
                print("1:开启")
                print("2:关闭")
                zuobiao2=int(input("显示坐标？"))
                juli2=int(input("显示与恒星距离？"))
                shijian2=int(input("显示间隔时间？"))
                sudu2=int(input("显示行星速度？"))
                print("现在设置输出结果保留小数位数")
                print("输入保留的位数")
                zuobiao12=int(input("坐标输出保留位数？"))
                juli12=int(input("距离输出保留位数？"))
                shijian12=int(input("时间输出保留位数？"))
                sudu12=int(input("速度输出保留位数？"))
                print("设置完毕！")
                print(jiange)
            if xiayibu2==3:
                i20=0
    if yy0==1:
        print("欢迎计算电子排布！")
        print("开发者：腿")
        print(":)")
        print("-")
        paibu1=1
        fangshe1=1
        zhouqi1=1
        zu1=1
        Zu1=["0","碱金属元素原子","碱土金属元素原子","硼族元素原子","碳族元素原子","氮族元素原子","氧族元素原子","卤族元素原子","稀有气体元素原子"]
        i1=1
        while i1==1:
            s1=0
            print("1:计算")
            print("2:设置")
            print("3:返回")
            s1=int(input("下一步是:"))
            print(jiange)
            z1=0
            if s1==1:
                X1=float(input("质子数为："))
                x1=int(X1)
                if 0<=x1<=118:
                    K1=int(0.5*(abs(x1)-abs(x1-2)+2))
                    L1=int(0.5*(abs(x1-2)-abs(x1-10)+8))
                    M1=int(0.5*(abs(x1-10)-abs(x1-18)+abs(x1-20)-abs(x1-30)+18))
                    N1=int(0.5*(abs(x1-18)-abs(x1-20)+abs(x1-30)-abs(x1-36)+abs(x1-38)-abs(x1-48)+abs(x1-56)-abs(x1-70)+32))
                    O1=int(0.5*(abs(x1-36)-abs(x1-38)+abs(x1-48)-abs(x1-54)+abs(x1-70)-abs(x1-80)+abs(x1-88)-abs(x1-102)+32))
                    P1=int(0.5*(abs(x1-54)-abs(x1-56)+abs(x1-80)-abs(x1-86)+abs(x1-102)-abs(x1-112)+18))
                    Q1=int(0.5*(abs(x1-86)-abs(x1-88)+abs(x1-112)-abs(x1-118)+8))
                    PaiBu1=str(x1)+"="+str(K1)+")"+str(L1)+")"+str(M1)+")"+str(N1)+")"+str(O1)+")"+str(P1)+")"+str(Q1)+")"
                    if paibu1==1:
                        print(PaiBu1)
                    #=====================================
                    if fangshe1==1:    
                        if 1<=x1<=83 and x1!=43:
                            print("存在非放射性的稳定同位素")
                        elif 83<=x1<=118 or x1==43:
                            print("无稳定同位素，常见同位素呈放射性")
                    #=====================================
                    if 1<=x1<=2:
                        z1=1
                    elif 3<=x1<=10:
                        z1=2
                    elif 11<=x1<=18:
                        z1=3
                    elif 19<=x1<=36:
                        z1=4
                    elif 37<=x1<=54:
                        z1=5
                    elif 55<=x1<=86:
                        z1=6
                    elif 87<=x1<=118:
                        z1=7
                    if zhouqi1==1:
                        print("第"+str(z1)+"周期")     
                #===========================
                    if zu1==1:    
                        if 57<=x1<=71:
                            print("镧系元素原子")
                        elif 89<=x1<=103:
                            print("锕系元素原子")
                        elif x1==1:
                            print("氢原子")
                        elif x1==4:
                            print("其他元素原子")
                        elif x1==12:
                            print("其他元素原子")
                        elif x1==2:
                            print("稀有气体元素原子")
                        elif 20<x1<30 or 38<x1<48 or 56<x1<80 or 88<x1<112:
                            print("过渡金属元素原子")
                        elif x1==30 or x1==48 or x1==80 or x1==112:
                            print("锌族元素原子")
                        elif Q1!=0:
                            print(str(Zu1[Q1]))
                        elif P1!=0:
                            print(str(Zu1[P1]))
                        elif O1!=0:
                            print(str(Zu1[O1]))
                        elif N1!=0:
                            print(str(Zu1[N1]))
                        elif M1!=0:
                            print(str(Zu1[M1]))
                        elif L1!=0:
                            print(str(Zu1[L1]))
                        elif K1!=0:
                            print(str(Zu1[K1]))
                    #=====================================
                elif x1==119:
                    print("嘿？这是鐄！")
                elif x1>119:
                    print("质子数过大")
                else:
                    print("error")
                if paibu1==2 and fangshe1==2 and zhouqi1==2 and zu1==2:
                    print("提示：所有功能已被关闭")
            if s1==2:
                print("1:开启")
                print("2:关闭")
                paibu1=int(input("显示电子排布？"))
                fangshe1=int(input("显示放射性？"))
                zu1=int(input("显示族？"))
                zhouqi1=int(input("显示周期？"))
                print("设置完毕！")
            print(jiange)
            if s1==3:
                i1=0
    if yy0==3:
        import random
        ren3=["郭郭","阿燕","蚱蜢","大师","平平","黄文","蒋天浩","体育甲"]
        didian3=["在控江","在家里","在天上","在厕所","趴在地上","倒立着","看着阿燕","在食堂"]
        zuo3=["跳原木","唱歌","卷同学","倒立","打乒乓球","制备Hw","狂啸","画十班美学","摔跤"]
        i3=1
        while i3==1:
            ren31=ren3[random.randint(0,7)]
            didian31=didian3[random.randint(0,7)]
            zuo31=zuo3[random.randint(0,8)]
            print(ren31+didian31+zuo31)
            print("1:继续")
            print("2:结束")
            i3=int(input("下一步？"))
            print(jiange)
