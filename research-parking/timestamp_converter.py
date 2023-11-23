def convert(input):
    return (input//10000-1)*1440+input%10000

input_file_path = r"D:\programming\research-parking\停车数据-出入时间戳拼接&时长.txt"  # 替换为实际文件路径
output_file_path = r"D:\programming\research-parking\停车数据-出入时间戳&时长.txt"  # 替换为实际文件路径
with open(input_file_path, 'r') as input_file:
    input_content = input_file.read()
numbers_list = input_content.split()
numbers = [int(num) for num in numbers_list]

output_list=[]
for i in range(0, len(numbers), 3):
    start_num = numbers[i]
    end_num = numbers[i + 1]
    diff = numbers[i + 2]
    
    output_list.append(convert(start_num))
    output_list.append(convert(end_num))
    output_list.append(diff)

with open(output_file_path, 'w') as output_file:
    for i in range(0, len(output_list), 3):
        line = " ".join(map(str, output_list[i:i+3]))  # 将每三个数字组合成一行
        output_file.write(line + '\n')
