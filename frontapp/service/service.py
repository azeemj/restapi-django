import os
import requests


def get_droplets(invent_id=0):

    if invent_id == 0:
        url = "http://localhost:8000/api/inventory/"
    else:
        url = "http://localhost:8000/api/inventory/"+str(invent_id)+"/"

    r = requests.get(url)

    data = r.json()
    print("r", data)
    # droplet_list = []
    # for i in range(len(droplets['droplets'])):
    #     droplet_list.append(droplets['droplets'][i])
    return data
