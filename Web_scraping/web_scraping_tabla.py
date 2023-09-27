import bs4 as bs #-------------> libreria 
import requests #-------------> libreria 
import pandas as pd #-------------> libreria 
from tqdm import tqdm
#def olympic_game ():

response = requests.get ('https://es.wikipedia.org/wiki/Anexo:Medallas_ol%C3%ADmpicas')
    
#response = requests.get(web)
#print(response.text)
content = response.text
soup = bs.BeautifulSoup(content, 'lxml')

table = soup.find ('table', {'class' : 'wikitable'})

Disciplinas = []
Años = []
Medallas = []
Deportistas = []

for medal in tqdm (table.findAll('tr')[1:]):
    Disciplina = medal.findAll('td')[2].text #---------> indice de la informacion que quiero sacar de la pagina
    Año = medal.findAll('td')[3].text #---------> indice de la informacion que quiero sacar de la pagina
    Medalla = medal.findAll('td')[8].text #---------> indice de la informacion que quiero sacar de la pagina
    Deportista = medal.findAll('td')[9].text #---------> indice de la informacion que quiero sacar de la pagina

    Disciplinas.append(Disciplina)
    Años.append(Año)
    Medallas.append(Medalla)
    Deportistas.append(Deportista)
    
                   




