import requests
import json
import time

server = "http://localhost:1026/v2/entities"

# get all entities
def get_status():
    r = requests.get(server)
    # Use a breakpoint in the code line below to debug your script.
    print(r.status_code)  # Press Ctrl+F8 to toggle the breakpoint.
    print(r.headers)
    print(r.content)
    my_json = json.loads(r.content)
    print(my_json)

# Create  entity
def create():
    data = {"id": "urn:ngsi-ld:Store:004",
            "type": "Store",
            "address": {
                "type": "PostalAddress",
                "value": {
                    "streetAddress": "Bornholmer Straße 65",
                    "addressRegion": "Berlin",
                    "addressLocality": "Prenzlauer Berg",
                    "postalCode": "10439"
                },
                "metadata": {
                    "verified": {
                        "value": "true",
                        "type": "Boolean"
                    }
                }
            },
            "location": {
                "type": "geo:json",
                "value": {
                    "type": "Point",
                    "coordinates": [13.3986, 52.5547]
                 }
            },
            "name": {
                "type": "Text",
                "value": "Bösebrücke Einkauf"
            }
        }
    headers = {"Content-Type": "application/json"}
    r = requests.post(server, data=json.dumps(data), headers=headers)
    print(r.status_code)
    request_status("post", r.status_code)

# display request status message
def request_status(method, code):
    if method == "post" and code == 201:
        print("Entity has been created")


if __name__ == '__main__':
    #get_status()
    create()


