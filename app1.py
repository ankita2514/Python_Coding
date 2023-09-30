from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99
            }
        ]
    }
]


@app.get("/store")
def get_store():
    return {"stores": stores}


@app.post("/store")
def create_store():
    request_data=request.get_json()
    new_store={"name":request_data["name"], "items":[]}
    stores.append(new_store)
    return new_store,201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data=request.get_json()
    for store in stores:
        if store["name"]==name:
            new_item={"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"Store not found"},404


@app.get("/store/<string:name>")
def get_storeInfo(name):
    for store in stores:
        if store["name"]==name:
            return store,201
    return {"message":"Store name not found"},404


@app.get("/store/<string:name>/items")
def get_storeItems(name):
    for store in stores:
        if store["name"] == name:
            return {"items" : store["items"]}, 201
    return {"message" : "Store name not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)