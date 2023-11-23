class Readbmp:
    """
    read bmp files
    图片的格式说明：https://en.wikipedia.org/wiki/BMP_file_format#Example_1
    """

    def __init__(self, pic_path) -> None:
        self.pic_path = pic_path
        self.read_color()

    def read_color(self):
        if self.pic_path.endswith(".bmp"):
            self.read_bmp()
        else:
            print("不支持的格式")

    def read_bmp(self):
        bin_datas = []
        """read file data to bin"""
        with open(self.pic_path, "rb") as f:
            while True:
                if len(bin_datas) == f.tell():
                    data = f.read(1)
                    bindata = bin(int.from_bytes(data,"little"))[2:]
                    if len(bindata) < 8:
                        bindata = (8 - len(bindata)) * "0" + bindata
                    bin_datas.append(bindata)
                else:
                    bin_datas = bin_datas[:-1]
                    break

        self.bin_pic_head = bin_datas[0:2]  # ID field
        self.bin_pic_size = bin_datas[2:6]  # Size of the BMP file 文件大小
        self.bin_pic_exe = bin_datas[6:10]  # 特定应用，默认为0
        self.bin_pic_address = bin_datas[10:14]  # 图片信息开始地址
        self.bin_pic_dib = bin_datas[14:18]  # DIB 头中的字节数
        self.bin_pic_w = bin_datas[18:22]  # 图片像素宽度
        self.bin_pic_h = bin_datas[22:26]  # 图片像素高度
        self.bin_pic_color_num = bin_datas[26:28]  # 使用颜色平面数
        self.bin_pic_color_long = bin_datas[28:30]  # 每个像素位数
        self.bin_pic_bi = bin_datas[30:34]  # BI_RGB
        self.bin_pic_big = bin_datas[34:38]  # 原始图像数据大小
        self.bin_pic_printpix = bin_datas[38:42]  # 打印分辨率
        self.bin_pic_dpi = bin_datas[42:46]  # DPI
        self.bin_pic_color_num = bin_datas[46:50]  # 调色板中颜色数量
        self.bin_pic_color_important = bin_datas[50:54]  # 重要颜色数量
        self.bin_pic_data = bin_datas[54:]  # 图片数据
        self.bin_to_pic()

    # 将二进制数据转化成十进制数据
    def bin_to_dec(self, bin_datas):
        bin_data = ""
        for i in reversed(bin_datas):
            bin_data += i
        return int(bin_data, 2)

    # 将列表转为3个一组的二维列表
    def change_data(self, data):
        data_2d = []
        x = []
        for i in data:
            x.append(int(i, 2))
            if len(x) == 3:
                data_2d.append(tuple(x))
                x = []
        return data_2d

    # 处理图片数据
    def bin_to_pic(self):
        self.pic_head = chr(int(self.bin_pic_head[0], 2)) + chr(
            int(self.bin_pic_head[1], 2)
        )
        self.pic_size = self.bin_to_dec(self.bin_pic_size)
        self.pic_exe = self.bin_to_dec(self.bin_pic_exe)
        self.pic_address = self.bin_to_dec(self.bin_pic_address)
        self.pic_dib = self.bin_to_dec(self.bin_pic_dib)
        self.pic_w = self.bin_to_dec(self.bin_pic_w)
        self.pic_h = self.bin_to_dec(self.bin_pic_h)
        self.pic_color_num = self.bin_to_dec(self.bin_pic_color_num)
        self.pic_color_long = self.bin_to_dec(self.bin_pic_color_long)
        self.pic_bi = self.bin_to_dec(self.bin_pic_bi)
        self.pic_big = self.bin_to_dec(self.bin_pic_big)
        self.pic_printpix = self.bin_to_dec(self.bin_pic_printpix)
        self.pic_dpi = self.bin_to_dec(self.bin_pic_dpi)
        self.pic_color_num = self.bin_to_dec(self.bin_pic_color_num)
        self.pic_color_important = self.bin_to_dec(self.bin_pic_color_important)
        self.pic_data = self.change_data(self.bin_pic_data)

    # 打印图片信息
    def show(self):
        print(
            """
文件ID  {} 
图像大小(Byte)  {}   
特定应用  {}   
图片信息开始地址  {}   
DIB 头中的字节数 {}   
图片像素宽度  {}   
图片像素高度  {}   
使用颜色平面数  {}   
每个像素位数  {}   
BI_RGB  {}   
原始图像数据大小(Byte) {} 
打印分辨率  {}   
DPI  {}   
调色板中颜色数量  {}   
重要颜色数量  {}   
图片数据  {} .... {} 
""".format(
                self.pic_head,
                self.pic_size,
                self.pic_exe,
                self.pic_address,
                self.pic_dib,
                self.pic_w,
                self.pic_h,
                self.pic_color_num,
                self.pic_color_long,
                self.pic_bi,
                self.pic_big,
                self.pic_printpix,
                self.pic_dpi,
                self.pic_color_num,
                self.pic_color_important,
                self.pic_data[:5],
                self.pic_data[-5:],
            )
        )

    # 判断颜色
    def color(self, color):
        b, g, r = color[0], color[1], color[2]
        if r == 0 and g == 0 and b == 0:
            return "黑色"
        elif r == 0 and g == 0 and b == 255:
            return "蓝色"
        elif r == 0 and g == 255 and b == 0:
            return "绿色"
        elif r == 255 and g == 0 and b == 0:
            return "红色"
        elif r == 255 and g == 255 and b == 255:
            return "白色"
        else:
            return "其他颜色"

    # 统计颜色
    def count_color(self):
        color_dict = {}
        for i in self.pic_data:
            if i in color_dict:
                color_dict[i] += 1
            else:
                color_dict[i] = 1
        return color_dict

    # 判断颜色的比例
    def color_percent(self):
        color_dict = self.count_color()
        color_percent_dict = {}
        for i in color_dict:
            color_percent_dict[self.color(i)] = int(
                color_dict[i] / len(self.pic_data) * 100
            )
        for i in color_percent_dict:
            print("{} 占比百分之 {}".format(i, color_percent_dict[i]))

data=Readbmp("r.bmp")
data.show()
data.color_percent()