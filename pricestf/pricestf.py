from json import load
from os import path
import requests

itemidsfile = path.join(path.dirname(path.abspath(__file__)), 'itemids.json')
with open(itemidsfile) as json_file:
    itemids = load(json_file)

def request(id, quality=6, au="", ks=""):
    url = "https://api.prices.tf/items/" + str(id) + ";" + str(quality) + au + ks + "?src=bptf"
    r = requests.get(url)
    return(r.json())

def get_price(name, quality="", australium=False, killstreak=0, error_message=True):
    price = {}
    au = ""
    ks = ""
    qua = 6

    if australium:
        au = ";australium"

    if killstreak > 0 and killstreak <= 3:
        ks = ";kt-" + str(killstreak)

    if quality == "Normal":
        qua = 0
    elif quality == "Genuine":
        qua = 1
    elif quality == "Vintage":
        qua = 3
    elif quality == "rarity3":
        qua = 4
    elif quality == "Unusual":
        qua = 5
    elif quality == "Unique":
        qua = 6
    elif quality == "Community":
        qua = 7
    elif quality == "Valve":
        qua = 8
    elif quality == "Self-Made":
        qua = 9
    elif quality == "Customized":
        qua = 10
    elif quality == "Strange":
        qua = 11
    elif quality == "Completed":
        qua = 12
    elif quality == "Haunted":
        qua = 13
    elif quality == "Collector's":
        qua = 14
    elif quality == "Decorated Weapon":
        qua = 15

    try:
        id = itemids[name]
    except:
        if error_message:
            print("NameError: No item named " + name)
        return(4)

    myrequest = request(id, quality=qua, au=au, ks=ks)

    if myrequest['success'] == False:
        if error_message:
            print("Something went wrong: '" + myrequest["message"] + "'")

        if myrequest["message"] == "Rate limit exceeded, try again later":
            return(1)
        elif  myrequest["message"] == "Item is not priced":
            return(2)
        elif myrequest["message"] == "No prices for given source":
            return(3)
        else:
            return(0)
    else:
        price['name'] = myrequest['name']
        price['buy_price'] = myrequest['buy']
        price['sell_price'] = myrequest['sell']
        return(price)
