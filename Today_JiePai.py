# coding:utf-8
'''
任务2：学习requests库: http://2.python-requests.org/zh_CN/latest/user/quickstart.html
产出：今日头条官网搜索“街拍”，爬取图片并保存图片到本地
author：oxl
time：2019.10.10
'''
import requests
from bs4 import BeautifulSoup
import json
import os
from io import BytesIO
from PIL import Image
import time
from hashlib import md5

def get_page(offset):
    url = "https://www.toutiao.com/api/search/content/"

    querystring = {"aid": "24", "app_name": "web_search", "offset": offset, "format": "json",
                   "keyword": "街拍", "autoload": "true", "count": "20", "en_qc": "1", "cur_tab": "1",
                   "from": "search_tab", "pd": "synthesis", "timestamp": "1570521477001"}

    headers = {
        'cookie': "tt_webid=6741269396470269444; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6741269396470269444; csrftoken=723996e61cbfbadb5c828bc1dcdaa5db; __tasessionId=7bd21rcwk1570521463757; s_v_web_id=9bf5fd5f27699910b0c34b5c66d6a968",
        'referer': "https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        'x-requested-with': "XMLHttpRequest",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "76701d95-5a6e-4915-9c70-c12af44bafce,c4ff69a8-02f0-4174-a052-ed256d6066e6",
        'Host': "www.toutiao.com",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    page = json.loads(response.text)
    page_data = page['data']
    # print(page_data)
    image_url_list = []
    for item in page_data:
        # print(type(item))
        try:
            image_li = item['image_list']
            image_url_list.append(image_li)

        except KeyError:
            pass

    return image_url_list

# image_url_list = get_page(offset)

def save_image_jiepai(image_url_list):
    file_path = "./jiepai_pics"
    if os.path.exists(file_path) == False:
        os.makedirs(file_path)

    for num, pics in enumerate(image_url_list):
        for index, pic in enumerate(pics):
            if pic:
                html = requests.get(pic.get('url'))
                file_name= md5(html.content).hexdigest()
                img_name = file_name +".png"
                image = Image.open(BytesIO(html.content))
                image.save(file_path+"/"+img_name)
                print("第{}组第{}张图片下载完成".format(num+1, index+1))
                time.sleep(0.1)


if __name__ == '__main__':
    num = eval(input("请输入总共抓取图片的页数:"))
    offsets = [20 * i for i in range(num)]
    for index, offset in enumerate(offsets):
        image_url_list = get_page(str(offset))
        save_image_jiepai(image_url_list)
        print('第{}轮抓取完成'.format(index + 1))