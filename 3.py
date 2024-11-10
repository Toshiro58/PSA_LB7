import http.client

host = "rokot.ibst.psu"
path = "/anatoly/"

connection = http.client.HTTPConnection(host)

try:
    connection.request("GET", path)

    
    response = connection.getresponse()

    
    print(f"Статус: {response.status} {response.reason}")
    print("Заголовки:")
    for header in response.getheaders():
        print(f"{header[0]}: {header[1]}")

    
    content = response.read()
    print("nСодержимое страницы:")
    print(content.decode('utf-8'))

finally:
    connection.close()
