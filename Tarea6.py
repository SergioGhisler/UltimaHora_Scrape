import requests
import csv
from bs4 import BeautifulSoup as bs

url = requests.get("https://www.ultimahora.es/tu-ciudad/madrid.html")
soup = bs(url.content, 'html.parser')

filename = "resultado.csv"
csv_writer = csv.writer(open(filename, 'w'))

data = []
data.append("Titulo")
data.append("Comentarios")
data.append("Imagenes")
if data:
    print("Inserting headers : {}".format(','.join(data)))
    csv_writer.writerow(data)
    data=[]

for article in soup.findAll('article', attrs=lambda value: value and value.startswith("normal")):

    #Titulos
    data.append(article.find('h3').string)

    #Comentarios
    comments = article.findAll('div', class_="enlaces")
    if comments == []:
        aux = "No tiene comentarios"
    else:
        aux = comments[0].getText()
        if aux == 'Comenta':
            aux = 'No tiene comentarios'
    data.append(aux)


    #Imagenes
    imagenes = article.findAll('figure',class_='img')
    if imagenes ==[]:
        aux= "No tiene imagen"
    else:
        aux = imagenes[0].find('img').get('src')
    data.append(aux)

    if data:
        print("Inserting data: {}".format(','.join(data)))
        csv_writer.writerow(data)
        data=[]
