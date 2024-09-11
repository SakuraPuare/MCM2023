import datetime
import pathlib
import pickle
import time
from urllib.parse import urlencode
import httpx
import tqdm.asyncio
from PIL import Image
import asyncio

url = 'https://wvs.earthdata.nasa.gov/api/v1/snapshot'
param = {
    'REQUEST': 'GetSnapshot',
    'TIME': '2010-01-01T00:00:00',
    'BBOX': '42.2577,-112.1233,44.5019,-109.8791',
    'CRS': 'EPSG:4326',
    'LAYERS': 'MODIS_Combined_L4_FPAR_4Day,MODIS_Combined_L4_FPAR_8Day',
    'WRAP': 'none,none',
    'FORMAT': 'image/png',
    'WIDTH': '4000',
    'HEIGHT': '4000',
    'ts': int(time.time()*1000)
}
download_path = pathlib.Path('download/light')
download_path.mkdir(parents=True, exist_ok=True)

httpx_cookies = httpx.Cookies()

with open('cookies.pkl', 'rb') as f:
    cookies = pickle.load(f)
    for i in cookies:
        httpx_cookies.set(i['name'], i['value'],
                          domain=i['domain'], path=i['path'])


sem = asyncio.Semaphore(32)


async def run(i, sem):
    if (download_path / f'{i.strftime("%Y%m%d")}.png').exists():
        return
    try:
        async with sem:
            async with httpx.AsyncClient(follow_redirects=True, timeout=60, verify=False) as client:
                param['TIME'] = i.strftime('%Y-%m-%dT00:00:00Z')
                r = await client.get(url + '?' + urlencode(param), cookies=httpx_cookies)
                with open(download_path / f'{i.strftime("%Y%m%d")}.png', 'wb') as f:
                    f.write(r.content)
                time.sleep(1)
        await asyncio.sleep(0.5)
    except:
        print(i)
        await run(i, sem)


async def main():
    time_now = datetime.datetime(year=2010, month=1, day=1)
    time_end = datetime.datetime(year=2020, month=1, day=1)
    task_list = []
    while time_now <= time_end:
        task_list.append(asyncio.create_task(run(time_now, sem=sem)))
        time_now += datetime.timedelta(days=25)

    for task in tqdm.asyncio.tqdm.as_completed(task_list):
        await task


if __name__ == '__main__':
    asyncio.run(main())
#     resp = httpx.get('https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&TIME=2011-08-03T00:00:00Z&BBOX=42.2577,-112.1233,44.5019,-109.8791&CRS=EPSG:4326&LAYERS=MODIS_Aqua_CorrectedReflectance_TrueColor,MODIS_Aqua_L3_EVI_Monthly&WRAP=day,none&FORMAT=image/png&WIDTH=8171&HEIGHT=8171&ts=1676690342588',cookies=httpx_cookies,timeout=60)
#     pass
# Image.frombytes(resp.content)
