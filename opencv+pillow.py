# 导入必要的库
import cv2
from PIL import Image, ImageDraw
import numpy as np

# 用Pillow库中的Image.open()打开一张图片
img_pil = Image.open("cdu.jpg")

# 将img_pil对象转换成numpy数组
np_img = np.array(img_pil)
# 将RGB颜色顺序转换成BGR顺序
cv2_img  = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)

# 创建一个人脸检测器(xml文件包含了训练过的模型参数)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# 调用函数检测所有人脸
# 该函数返回的是一个包含检测到所有人脸的列表，每个元素是一个包含(x, y, w, h)四个整数的元组，分别表示人脸矩形框左上角的坐标和矩形的宽度和高度
faces = face_cascade.detectMultiScale(cv2_img, scaleFactor=1.1, minNeighbors=5, minSize=(1, 1))

# 生成一个可用于画图的对象
draw = ImageDraw.Draw(img_pil)

# 遍历所有检测到的人脸矩形框，并且画框
for (x, y, w, h) in faces:
    draw.rectangle((x, y, x+w, y+h), outline=(255, 0, 0))
    print(x,y,w,h)

# 显示标记好的图片
img_pil.show()
