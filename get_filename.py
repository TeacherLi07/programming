import os

def get_filenames_without_extension(directory):
    file_names = []
    
    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # 获取文件名（不含后缀名）
            name_without_extension = os.path.splitext(filename)[0]
            file_names.append(name_without_extension)
    
    return file_names

# 指定目录路径
directory_path = r"D:\电子书"

# 获取目录中所有文件的文件名（不含后缀名）
file_names = get_filenames_without_extension(directory_path)

for name in file_names:
    print(name)