from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import httpx
import pathlib
import pickle
from concurrent.futures import ThreadPoolExecutor

driver = webdriver.Chrome()
driver.get('https://urs.earthdata.nasa.gov/home')

driver.implicitly_wait(10)
driver.find_element(By.ID,'username').send_keys(account)
driver.find_element(By.ID,'password').send_keys(passwd)
driver.find_element(By.CLASS_NAME,'eui-btn--green').click()

while driver.current_url == 'https://urs.earthdata.nasa.gov/home':
    time.sleep(1)

cookies = driver.get_cookies()
httpx_cookies = httpx.Cookies()
for i in cookies:
    httpx_cookies.set(i['name'], i['value'], domain=i['domain'], path=i['path'])

with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

driver.quit()

download_list = []
with open('download.txt', 'r') as f:
    for i in f.readlines():
        download_list.append(i.strip())


pool = ThreadPoolExecutor(16)


def run(url):
    if pathlib.Path('download')/url.split('/')[-1].exists():
        return
    with httpx.Client(cookies=httpx_cookies,follow_redirects=True) as client:
        r = client.get(url)
        with open(pathlib.Path('download')/url.split('/')[-1], 'wb') as f:
            f.write(r.content)


for i in download_list:
    # pool.submit(run, i)
    run(i)
    