room=["101","102","201","202","301","302","401","402","501","502"]
ys=[123,43,54,56,87,43,85,34,43,76]
i=0
sf=[]
while i<10:
    sf.append((round(ys[i]*2.27+ys[i]*0.9*2.02,2)))
    print(room[i],sf[i],"    ")
    i=i+1
