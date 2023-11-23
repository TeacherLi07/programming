import requests
import threading

def download_image(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"文件 {filename} 下载成功")
    else:
        print(f"文件 {filename} 下载失败")

def main():
    num_threads = 5  # 设置线程数
    base_url = "http://motions.cat/gif/nhn/"

    thread_list = []

    for i in range(1, 151):
        url = f"{base_url}{str(i).zfill(4)}.gif"
        filename = f"{str(i).zfill(4)}.gif"
        thread = threading.Thread(target=download_image, args=(url, filename))
        thread_list.append(thread)

    # 启动线程
    for thread in thread_list:
        thread.start()

    # 等待所有线程完成
    for thread in thread_list:
        thread.join()

    print("所有文件下载完成")

if __name__ == "__main__":
    main()
