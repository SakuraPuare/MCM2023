import datetime
import itertools
import multiprocessing
import random
import time

import keyboard
import numpy
import psutil
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By

start = datetime.datetime(year=2013, month=1, day=1)
end = datetime.datetime(year=2023, month=1, day=1)


def startandstop(pid):
    if psutil.Process(pid).status() == 'stopped':
        # 则唤醒
        print('唤醒')
        psutil.Process(pid).resume()
    # 如果pid在运行
    elif psutil.Process(pid).status() == 'running':
        # 则挂起
        print('挂起')
        psutil.Process(pid).suspend()


# 降水


def run():
    global start
    driver = webdriver.Chrome()
    driver.get(
        'https://worldview.earthdata.nasa.gov/?v=-111.05317125297746%2C35.136652539062496%2C-109.17780504203996%2C36.022150585937496&z=2&ics=true&ici=3&icd=31&l=Reference_Labels_15m%2CReference_Features_15m%2CCoastlines_15m%2CMODIS_Terra_L4_LAI_8Day%2CMODIS_Aqua_L4_LAI_8Day%2CMODIS_Combined_L4_LAI_8Day%2CMODIS_Combined_L4_LAI_4Day%2CVIIRS_NOAA20_CorrectedReflectance_TrueColor%2CVIIRS_SNPP_CorrectedReflectance_TrueColor%28hidden%29%2CMODIS_Aqua_CorrectedReflectance_TrueColor%28hidden%29%2CMODIS_Terra_CorrectedReflectance_TrueColor%28hidden%29&lg=true&s=-70.1708%2C47.2884&t=2013-01-01-T13%3A42%3A32Z')
    # 窗口最大化
    driver.maximize_window()
    pass
    pyautogui.moveTo(1280, 720)
    pyautogui.click()
    data = None
    while start < end:
        data_list = []
        delta = 100
        x = delta
        # x = random.randint(int(delta // 4), delta // 3)
        for i in itertools.product(range(1280 - delta, 1280 + delta + 2, x), range(720 - delta, 720 + delta + 2, x)):
            pyautogui.moveTo(*i, duration=0)
            # 设置driver为焦点
            driver.switch_to.window(driver.window_handles[0])
            try:
                while not data or not [i.text for i in data if i.text]:
                    data = driver.find_elements(By.CLASS_NAME, 'wv-running-label')
                    pyautogui.move(1, 1, duration=0)
                for v in driver.find_elements(By.CLASS_NAME, 'wv-running-label'):
                    v = v.text
                    if '<' in v:
                        continue
                    elif '–' in v:
                        v = v[:-6]
                        v = v.split(' – ')[0]
                    else:
                        # v = v[1:-1]
                        continue
                        # v = 40
                    print(v)
                    if v:
                        data_list.append(float(v))
            except Exception as e:
                print(e)
                keyboard.press_and_release('right')
                start += datetime.timedelta(days=31)
                time.sleep(2)
                continue
        keyboard.press_and_release('right')
        start += datetime.timedelta(days=31)
        if len(data_list) == 0:
            continue
        print(numpy.average(data_list))
        # time.sleep(0.05)
        ans = (numpy.average(data_list))
        with open('data.csv', 'a') as f:
            f.write(f'{start.strftime("%y/%m/%d")},{ans}\n')
        pass


if __name__ == '__main__':
    with open('data.csv', 'w') as f:
        f.write('date,value\n')
    p = multiprocessing.Process(target=run)
    p.start()
    pid = p.pid
    keyboard.add_hotkey('F8', startandstop, args=(pid,))
    p.join()
