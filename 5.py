import http.client
from bs4 import BeautifulSoup
import os
import requests
from urllib.parse import urljoin, urlparse


host = "rokot.ibst.psu"
path = "/anatoly/"


os.makedirs('images', exist_ok=True)


visited_urls = set()

def download_images_from_page(url):
    if url in visited_urls:
        return
    visited_urls.add(url)

    
    parsed_url = urlparse(url)
    host = parsed_url.netloc
    path = parsed_url.path

    
    connection = http.client.HTTPConnection(host)

    try:
        connection.request("GET", path)

        
        response = connection.getresponse()

        
        if response.status != 200:
            print(f"Ошибка загрузки страницы: {response.status} {response.reason}")
            return

      
        content = response.read().decode('utf-8')

        
        soup = BeautifulSoup(content, 'html.parser')

        
        img_tags = soup.find_all('img')
        for img in img_tags:
            img_url = urljoin(url, img.get('src'))
            try:
                img_data = requests.get(img_url).content
                img_name = os.path.join('images', os.path.basename(img_url))
                with open(img_name, 'wb') as f:
                    f.write(img_data)
                print(f"Сохранено изображение: {img_name}")
            except Exception as e:
                print(f"Не удалось загрузить {img_url}: {e}")

        
        link_tags = soup.find_all('a')
        for link in link_tags:
            link_url = urljoin(url, link.get('href'))
            if link_url.startswith(f"http://{host}") and link_url not in visited_urls:
                download_images_from_page(link_url)

    finally:
        connection.close()

start_url = f"http://{host}{path}"
download_images_from_page(start_url)
