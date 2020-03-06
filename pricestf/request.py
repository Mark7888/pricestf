import requests

def request(id, quality=6, au="", ks=""):
    url = "https://api.prices.tf/items/" + str(id) + ";" + str(quality) + au + ks + "?src=bptf"
    r = requests.get(url)
    return(r.json())
