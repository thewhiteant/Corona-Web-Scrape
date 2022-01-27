from bs4 import BeautifulSoup as soup
import requests
import readchar
page = requests.get("https://www.worldometers.info/coronavirus").text

loadpage = soup(page,'lxml')

total = loadpage.find_all("div", class_="maincounter-number")
tn = []
for i in total:
    total_number = i.find("span")
    tn.append(total_number.text)

print("\033[1;35;40m                        Welcome Whiteant Corona Meter")
print("\033[0;30;40m _________________________________________________________________________")
print(f"\033[0;33;40m World Total Corona Case : {tn[0]}")
print(f"\033[0;31;40m Total Deaths Of World : {tn[1]}")
print(f"\033[0;32;40m Total Recovered : {tn[2]}")


total_data = []

tab = loadpage.find("table")
all_country = loadpage.find_all("a", class_="mt_a")
all_row = tab.find_all("tr")


table = loadpage.find("table")
tr = table.find_all("tr", {"style": ""})
fbd = table.find_all("a", class_="mt_a")

sc = input("Country Name: ")


x = 0
for co in fbd:
    x += 1
    ctex = co.text
    if ctex.upper()  == sc.upper()  :

        data = tr[x+1].find_all("td")
        name = data[1].text
        tc = data[2].text.replace(",","")
        nc = data[3].text.replace("+","")
        td = data[4].text.replace(",", "")
        ajm = data[5].text.replace("+", "")
        tre = data[6].text.replace(",", "")
        ac = data[8].text
        print("\033[1;30;40m ----------------------")
        print(f"\033[1;35;40m {name} Corona Report ")
        print(f"\033[1;33;40m Total Case: {tc}")
        print(f"\033[3;36;40m New Case: {nc}")
        print(f"\033[5;34;40m Total Deaths : {td}")
        print(f"\033[1;31;40m Today Deaths: {ajm}")
        print(f"\033[0;32;40m Total Recovered : {tre}")
        print(f"\033[1;33;40m Active Case: {ac}")


print("\033[1;37;40m Press Any Key To Exit")
k = readchar.readchar()

