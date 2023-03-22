import json

todo_list = {
    "items": [
        
    ]
}

#todo_list["items"].append({"name": "test", "checked": False})

with open('list.json', 'w') as f:
    json.dump(todo_list, f, indent=2)
