from json import load
from os import path
import requests

itemidsfile = path.join(path.dirname(path.abspath(__file__)), 'itemids.json')
with open(itemidsfile) as json_file:
    itemids = load(json_file)

qualities = {
"Normal" : 0,
"Genuine" : 1,
"Vintage" : 3,
"rarity3" : 4,
"Unusual" : 5,
"Unique" : 6,
"Community" : 7,
"Valve" : 8,
"Self-Made" : 9,
"Customized" : 10,
"Strange" : 11,
"Completed" : 12,
"Haunted" : 13,
"Collector's" : 14,
"Decorated Weapon" : 15
}

def request(id, quality=6, au="", ks=""):
    url = "https://api.prices.tf/items/" + str(id) + ";" + str(quality) + au + ks + "?src=bptf"
    r = requests.get(url)
    return(r.json(), r.headers)

def ratelimit():
    data = {}
    urlrequest = request(0)
    headers = urlrequest[1]
    data["limit"] = int(headers["X-RateLimit-Limit"])
    data["remaining"] = int(headers["X-RateLimit-Remaining"])
    data["reset"] = int(headers["X-RateLimit-Reset"])

    return(data)

def get_price(name, quality="", australium=False, killstreak=0, error_message=True, ratelimit_data=False):
    data = {}
    au = ""
    ks = ""
    qua = 6

    if australium:
        au = ";australium"

    if killstreak > 0 and killstreak <= 3:
        ks = ";kt-" + str(killstreak)

    if quality in qualities:
        qua = qualities[quality]

    try:
        id = itemids[name]
    except:
        if error_message:
            raise("NameError: No item named " + name)
        return(4)

    urlrequest = request(id, quality=qua, au=au, ks=ks)

    request_content = urlrequest[0]
    headers = urlrequest[1]

    if request_content['success'] == False:
        if error_message:
            raise("Something went wrong: '" + request_content["message"] + "'")

        if request_content["message"] == "Rate limit exceeded, try again later":
            return(1)
        elif  request_content["message"] == "Item is not priced":
            return(2)
        elif request_content["message"] == "No prices for given source":
            return(3)
        else:
            return(0)
    else:
        data['name'] = request_content['name']
        data['buy_price'] = request_content['buy']
        data['sell_price'] = request_content['sell']
        if ratelimit_data:
            data["ratelimit"] = {}
            data["ratelimit"]["limit"] = int(headers["X-RateLimit-Limit"])
            data["ratelimit"]["remaining"] = int(headers["X-RateLimit-Remaining"])
            data["ratelimit"]["reset"] = int(headers["X-RateLimit-Reset"])

    return(data)
