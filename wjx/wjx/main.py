from concurrent.futures.thread import ThreadPoolExecutor
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import fun
import short_answer
import random
import proxy_util


chrome_options = Options()
# 设置无头浏览器
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--incognito')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 滑块防止检测
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

driver_path = r'C:\Program Files\Google\Chrome\Application\chromedriver'
# driver_path = ''
head = '(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))'
proxy_list = [
    "117.159.10.124:9002",
    "218.57.210.186:9002",
    "111.59.4.88:9002",
    "140.249.88.105:80",
    "117.146.231.40:9002",
    "82.79.29.12:8182",
    "82.79.29.12:8182",
    "187.189.79.169:999",
    "102.212.130.117:8080",
    "91.189.177.186:3128",
    "112.25.18.114:80",
    "120.236.88.83:9002",
    "195.245.76.45:3128",
    "39.164.45.197:8060",
    "60.188.5.234:80",
    "188.82.97.82:80",
    "200.61.16.80:8080",
    "47.91.45.235:8000",
    "88.201.217.203:80",
    "141.95.241.100:80",
    "47.96.70.163:8888",
    "112.54.47.55:9091",
    "200.106.184.10:999",
    "120.82.174.128:9091",
    "42.63.65.38:80",
    "185.15.172.212:3128",
    "59.110.139.131:3128",
    "58.221.40.175:80",
    "120.202.128.112:9002",
    "120.202.128.112:9002",
    "135.181.154.225:80",
    "123.30.154.171:7777",
    "121.194.10.77:80",
    "45.163.199.227:8083",
    "117.54.114.35:80",
    "103.152.112.234:80",
    "60.188.5.214:80",
    "60.188.5.168:80",
    "60.188.5.136:80",
    "221.153.92.39:80",
    "47.100.91.57:8080",
    "47.100.91.57:8080",
    "221.194.149.8:80",
    "94.158.53.145:3128",
    "39.100.120.200:7890",
    "82.69.16.184:80",
    "221.130.192.237:80",
    "221.130.193.28:80",
    "84.248.46.187:80",
    "154.85.58.149:80",
    "193.239.56.84:8081",
    "203.19.38.114:1080",
    "35.240.156.235:8080",
    "61.130.9.38:443",
    "203.89.126.250:80",
    "50.62.183.223:80",
    "139.159.176.147:8090",
    "123.3.141.167:80",
    "209.97.173.78:4444",
    "162.223.94.164:80",
    "111.8.226.107:9091",
    "60.188.5.148:80",
    "8.209.114.72:3129",
    "60.214.128.150:9091",
    "47.113.224.182:9999",
    "148.76.97.250:80",
    "101.200.187.233:3333",
    "94.140.242.221:8080",
    "61.158.175.38:9002",
    "142.93.223.219:8080",
    "115.144.16.101:10471",
    "121.194.10.72:80",
    "121.37.205.253:10001",
    "111.40.124.221:9091",
    "154.118.228.212:80",
    "111.40.116.212:9091",
    "190.113.40.41:999",
    "38.156.238.94:999",
    "154.118.228.212:80",
    "211.97.2.196:9002",
    "8.219.97.248:80",
    "116.205.229.85:80",
    "51.15.242.202:8888",
    "218.13.24.130:9002",
    "120.46.215.52:8080",
    "51.15.242.202:8888",
    "112.250.110.172:9091",
    "221.130.193.35:80",
    "140.249.88.107:80",
    "45.174.92.200:999",
    "192.99.208.0:8050",
    "36.6.144.78:8089",
    "221.130.193.27:80",
    "58.221.40.178:80",
    "200.185.55.121:9090",
    "115.144.102.39:10080",
    "109.194.22.61:8080",
    "101.251.204.174:8080",
    "117.158.146.215:9091",
    "95.56.254.139:3128"
]

# 每个问题选项的数量（-1表示该题为简答题）（若为矩阵题则每道题分多个不同角度，此处填写一个角度下的选项数量即可）
option_nums = [41]  # 18
# 0表示单选，1表示多选
# 新增：2表示度量题，3表示矩阵单选题
multiple_choice = [1]


def solve(cnt: int):

    # 设置代理
    PROXY = proxy_util.random_proxy(proxy_list)  # 随机用一个代理
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",
    }

    driver = webdriver.Chrome(options=chrome_options)
    # 设置最大连接时间，超时抛出异常
    driver.set_page_load_timeout(10)

    # 设置浏览器定位
    (longitude, latitude) = fun.random_position()
    # print(longitude, latitude)
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", {
        "latitude": latitude,
        "longitude": longitude,
        "accuracy": 100
    })
    # 将webdriver属性置为undefined
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                        {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })

    # 打开问卷星网址
    driver.get('https://tp.wjx.top/vm/tnVOP7j.aspx')

    # driver.maximize_window()
    # 每个问题的选项
    q_num = len(option_nums)

    for i in range(0, q_num):
        # 第i+1题目的选项数
        num = option_nums[i]
        if num == -1:
            # 简答题
            text_input = driver.find_element(By.XPATH, f'//*[@id="div{i+1}"]/div[1]/div/label/span')
            text_input.clear()
            text = short_answer.get_short_answer(i+1)
            text_input.send_keys(text)

        elif multiple_choice[i] == 0:
            # 单选题
            q_option = fun.random_option(num)
            q_select = driver.find_element(By.XPATH, f'//*[@id="div{i+1}"]/div[2]/div[{q_option}]')
            q_select.click()
        
        elif multiple_choice[i] == 1:
            # 多选题
            q_selects = []
            while len(q_selects) <= 6:
                q_selects.append(random.randint(1,41))
                q_selects=list(set(q_selects))
            if 0.7 >= random.random():
                q_selects.append(23)
            q_selects=list(set(q_selects))
            q_selects.sort()
            print(q_selects)
            for j in q_selects:
                q_select = driver.find_element(By.XPATH, f'//*[@id="div{i+1}"]/div[3]/div[{j}]')
                q_select.click()
                time.sleep(random.random()*2+1)
        
        elif multiple_choice[i] == 2:
            # 度量题（新增）
            q_option = fun.random_multi_select(num)
            q_select = driver.find_element(By.XPATH, f'//*[@id="div{i+1}"]/div[2]/div[1]/ul[1]/li[{q_option}]')
            q_select.click()

        elif multiple_choice[i] == 3:
            # 矩阵单项题（新增，此处以正反两个角度为例）。
            # 矩阵第一个角度
            q_option1 = fun.random_option(num)+1
            q_select1 = driver.find_element(By.XPATH, f'//*[@id="div{i+1}"]/div[2]/table[1]/tbody[1]/tr[3]/td[{q_option1}]')
            q_select1.click()
            # 矩阵第二个角度
            q_option2 = fun.random_option(num)+1
            q_select2 = driver.find_element(By.XPATH, f'//*[@id="div{i+1}"]/div[2]/table[1]/tbody[1]/tr[5]/td[{q_option2}]')
            q_select2.click()

    submit_button = driver.find_element(By.XPATH, '//*[@id="ctlNext"]')
    submit_button.click()
    time.sleep(0.2)
    # 点按验证（旧，现在已不可用）
    # confirm = driver.find_element(By.XPATH, '//*[@id="alert_box"]/div[2]/div[2]/button')
    # confirm.click()
    # validation = driver.find_element(By.XPATH, '//*[@id="rectMask"]')
    # validation.click()
    # time.sleep(2.5)

    # 点按验证（新）
    # confirm = driver.find_element(By.XPATH, '//*[@id="layui-layer1"]/div[3]/a')
    # confirm.click()
    try:
        validation = driver.find_element(By.XPATH, '//*[@id="SM_BTN_WRAPPER_1"]')
        validation.click()
        time.sleep(2.5)
    except selenium.common.exceptions.NoSuchElementException:
        pass


    # res = driver.find_element(By.XPATH, '//*[@id="SM_TXT_1"]')

    # 滑块验证
    try:
        slider = driver.find_element(By.XPATH, '//*[@id="nc_1__scale_text"]/span')

        print('[' + eval(head) + f']: ', slider.text, cnt)
        if str(slider.text).startswith("请按住滑块"):
            width = slider.size.get('width')
            ActionChains(driver).drag_and_drop_by_offset(slider, width, 0).perform()

    except selenium.common.exceptions.NoSuchElementException:
        pass

    time.sleep(1)
    # print('[' + eval(head) + f']: ', res.text, cnt)
    driver.close()


if __name__ == '__main__':
    for i in range(1000000):
        try:
            solve(i)
            time.sleep(random.randint(15,60))
        except Exception as e:
            print(e)
            time.sleep(random.randint(120,300))

        # current_time = int(time.time())
        # gap = current_time - last_time
        # # 8分钟更新一次代理
        # if gap >= 480:
        #     proxy_list = proxy_util.update_proxy()
        #     print('[' + eval(head) + ']: 更新代理列表')
        #     last_time = current_time

