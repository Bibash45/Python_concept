### PUt and DELETE  - HTTP Verbs
### Working With API's -- Json


from flask import Flask,jsonify,request

app=Flask(__name__)




## Initial Data in my to do list
items=[
    {"id":1,"name":"Item1","description":"This is item1"},
    {"id":2,"name":"Item2","name":"This is item2"},
]

@app.route("/")
def home():
    return "Welcome To The Sample To Do List App"

## Get: Retrieve all items
@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(items)

## GET: Retrieve a specific item by Id
@app.route("/items/<int:item_id>",methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404
    else:
        return jsonify(item)
    
## Post : create a new task
@app.route("/items",methods=["POST"])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"message": "Invalid data"}), 400
    new_item = {
        "id": items[-1]['id'] + 1 if items else 1,
        "name": request.json['name'],
        "description": request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item), 201


## PUt : Update the existing item
@app.route("/items/<int:item_id>",methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id']==item_id), None)
    if item is None:
        return jsonify({"message": "Item not found"}), 404
    if not request.json:
        return jsonify({"message": "Invalid data"}), 400
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)
    
    
## DELETE: Delete an item
@app.route("/items/<int:item_id>",methods=["DELETE"])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"}), 200
    

if __name__ == '__main__':
    app.run(debug=True)

