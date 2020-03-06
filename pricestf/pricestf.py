from request import request
from json import load

with open('itemids.json') as json_file:
    itemids = load(json_file)

def get_price(name, quality="", australium=False, killstreak=0):
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
        print("NameError: No item named " + name)
        return(None)

    myrequest = request(id, quality=qua, au=au, ks=ks)

    if myrequest['success'] == False:
        print("Something went wrong: '" + myrequest["message"] + "'")
        return(None)
    else:
        price['name'] = myrequest['name']
        price['buy_price'] = myrequest['buy']
        price['sell_price'] = myrequest['sell']
        return(price)
