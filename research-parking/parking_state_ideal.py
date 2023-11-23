import numpy as np

def main():
    isparking_short=np.zeros((120,15840),dtype=bool)
    isparking_med=np.zeros((1000,15840),dtype=bool)
    isparking_long=np.zeros((300,15840),dtype=bool)
    lot_usage_short=[0]*120
    lot_usage_med=[0]*1000
    lot_usage_long=[0]*300
    file_path = r"D:\programming\research-parking\停车数据-出入时间戳&时长.txt" 
    with open(file_path, 'r') as file:
        content = file.read()
    parking_file = content.split()
    parking_data = [int(num) for num in parking_file]
    for i in range(0,len(parking_data),3):
        start_time=parking_data[i]
        end_time=parking_data[i+1]
        duration=parking_data[i+2]
        lot_number=0
        if duration<=60:
            lot_number=0
            while isparking_short[lot_number][start_time]==True:
                lot_number+=1
            isparking_short[lot_number][start_time:end_time+1]=True
            lot_usage_short[lot_number]+=1
        elif duration<=240:
            lot_number=0
            while isparking_med[lot_number][start_time]==True:
                lot_number+=1
            isparking_med[lot_number][start_time:end_time+1]=True
            lot_usage_med[lot_number]+=1
        else:
            lot_number=0
            while isparking_long[lot_number][start_time]==True:
                lot_number+=1
            isparking_long[lot_number][start_time:end_time+1]=True
            lot_usage_long[lot_number]+=1

    print(lot_usage_short,lot_usage_med,lot_usage_long,sep="\n\n\n\n")

main()



