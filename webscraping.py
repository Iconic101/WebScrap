# this program scrapes coinmarket.com and extracts all the cryptos listed and their cost and
#also displays the best perfomring and worst performing crypto in the last 24hr

from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
html = BeautifulSoup(result, "html.parser")
cryptoContainer = html.find(class_="sc-936354b2-2 bOgFCq")



tbody = html.tbody
trs = tbody.contents



prices = {}

highest_rise = 0
highest_fall = 0
# #
def getPrices(n):
    for tr in trs[:n]:

        fixed_name=""
        fixed_price=""
        name,price = tr.contents[2:4]
        if trs.index(tr)<10:
            change = tr.contents[5].find(class_="sc-a59753b0-0").contents[-1]

        if trs.index(tr)>=10:
            fixed_name =name.find(class_="crypto-symbol").string
            fixed_price ="$" + (str(price).split(">"))[-2].split("<")[0]

        else:
            fixed_name = name.p.string

            fixed_price = price.span.string



        prices[fixed_name] = fixed_price

    print(prices)


def getChange(stat):
    changed = trs[0].contents[2].p.string
    rise_fall = 0

    for tr in trs[:10]:

        name = tr.contents[2].p.string
        change = tr.contents[5].find(class_="sc-a59753b0-0").contents[-1]
        # print(name)

        if stat.lower() in str(tr.contents[5].find(class_="sc-a59753b0-0").contents[0]).lower():
            if float(tr.contents[5].find(class_="sc-a59753b0-0").contents[-1][:-1])>rise_fall:
                rise_fall = float(tr.contents[5].find(class_="sc-a59753b0-0").contents[-1][:-1])
                changed = name

    return [changed,rise_fall]


print("Best performing: ",getChange("up")[0],":",getChange("up")[1],"% up") #down to get highest fall in last 24hr and up to get crypto with highest rise in value
print("Worst performing: ",getChange("down")[0],":",getChange("down")[1],"% down")
# print(getPrices(20))



