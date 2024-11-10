import http.client
from bs4 import BeautifulSoup
import os
import requests
from urllib.parse import urljoin


host = "rokot.ibst.psu"
path = "/anatoly/"

connection = http.client.HTTPConnection(host)

try:
    
    connection.request("GET", path)

    
    response = connection.getresponse()

    
    if response.status != 200:
        print(f"Ошибка загрузки страницы: {response.status} {response.reason}")
        exit()
      
    content = response.read().decode('utf-8')

    soup = BeautifulSoup(content, 'html.parser')

  
    img_tags = soup.find_all('img')

    os.makedirs('images', exist_ok=True)

    for img in img_tags:
        img_url = urljoin(f"http://{host}", img.get('src'))
        try:
            img_data = requests.get(img_url).content
            img_name = os.path.join('images', os.path.basename(img_url))
            with open(img_name, 'wb') as f:
                f.write(img_data)
            print(f"Сохранено изображение: {img_name}")
        except Exception as e:
            print(f"Не удалось загрузить {img_url}: {e}")

finally:
    connection.close()
