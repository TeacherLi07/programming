import random          # 用于产生随机数
import time            # 用于延时
from selenium.webdriver.common.by import By      #导入By包进行元素定位
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#实例化一个启动参数对象
chrome_options = Options()
 
#添加启动参数
chrome_options.add_argument(
    'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"')  # 添加请求头
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
 
# 防止被识别
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])     #设置开发者模式启动
 
chrome_options.add_experimental_option('useAutomationExtension', False)    # 关闭selenium对chrome driver的自动控制
 
browser = webdriver.Chrome(options=chrome_options)     #设置驱动程序，启动浏览器  （实现以特定参数启动）
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})       #用来执行Chrome开发这个工具命令