from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pdb
import re
import os
import hashlib
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
pageIds = [55226, 55428, 55430, 55432, 55435, 55439, 55442, 55444, 55447, 55449, 55453, 55458]
for pageId in pageIds:
    site = 'file:///Users/satya/work/transition/digital.lib.umd.edu/transition/poem%3Fpid=umd:'+str(pageId)+'.html'
    directory = os.getcwd() #Relative to script location
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get(site)
    source_url_img = "../webfiles/public-common/images/digital/55226/thumb_%s/umd-bdef:image/getImage/"
    source_url_thumb = "../webfiles/public-common/images/digital/55226/thumb_%s/umd-bdef:image/getThumbnail?maxHeight=&maxWidth="
    path = directory+"/"+str(pageId)+"/"
    try:
        os.mkdir(path, 0o755)
    except OSError:
        print ("Creation of the directory %s failed" % path)

    def download_image(source_url, dest_dir, name="test"): 
        image_name = name ##hashlib.md5(source_url.encode()).hexdigest()
        image_name = image_name + ".jpg"
        with open(os.path.join(dest_dir, image_name), 'wb') as f:
            image_data = requests.get(source_url).content
            f.write(image_data)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    img_tags = soup.find_all('img')
    urlLists = []
    for img in img_tags:
        lis = re.findall(r'umd\:(.+?)_transition', img.get('onclick', ""))
        if len(lis)>0:
            urlLists.append(lis[0])

    for url in urlLists:
        try:
            print url
            download_image(source_url_img%url,path,"image_"+url)
            download_image(source_url_thumb%url,path,"thumb_"+url)
        
        except Exception as e:
            print url, "error fetching...", str(e)
    driver.quit()
