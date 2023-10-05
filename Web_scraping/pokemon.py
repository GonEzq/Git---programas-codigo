from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://pokemondb.net/pokedex/all"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")
# print(soup)

rows = soup.find("table", attrs={"id": "pokedex"}).find("tbody").find_all("tr")
# print(rows[0].find_all("td")[1].get_text())
# print(rows[0].find_all("td")[2].get_text())
names = []
types = []
total = []
hp = []
attack = []
defense = []
sp_atk = []
sp_def = []
speed = []

for row in rows:
    names.append(row.find_all("td")[1].get_text())
    types.append(row.find_all("td")[2].get_text())
    total.append(row.find_all("td")[3].get_text())
    hp.append(row.find_all("td")[4].get_text())
    attack.append(row.find_all("td")[5].get_text())
    defense.append(row.find_all("td")[6].get_text())
    sp_atk.append(row.find_all("td")[7].get_text())
    sp_def.append(row.find_all("td")[8].get_text())
    speed .append(row.find_all("td")[9].get_text())

# print(speed)
df = pd.DataFrame({"Names": names, "Types": types, "Total": total,
                   "Hp": hp, "Attacks": attack, "Defense": defense,
                   "Sp_atk": sp_atk, "Sp_def": sp_def, "Speed": speed})
# print(df)

df.to_csv("Pokemones.csv")
