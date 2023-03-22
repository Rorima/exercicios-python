"""
Materials used to learn:

https://www.w3schools.com/python/python_json.asp
https://www.youtube.com/watch?v=9N6a-VLBa2I&t=5s&ab_channel=CoreySchafer

"""

import json

"""
todo_list = {
    "items": [
        {'name': 'chosen_name', 'checked': False},
        {'name': 'chosen_name', 'checked': False},
        {'name': 'chosen_name', 'checked': False},
        {'name': 'chosen_name', 'checked': False},
        {'name': 'chosen_name', 'checked': False},
        {'name': 'chosen_name', 'checked': False},
        {'name': 'chosen_name', 'checked': False},
        {'name': 'chosen_name', 'checked': False}
    ]
}
"""

# with open('test_list.json', 'w') as f:
#     json.dump(todo_list, f, indent=2)

todo_list = dict()

with open('test_list.json', 'r') as f:
    todo_list = json.load(f)

# for item in todo_list['items']:
#     print(item['name'], item['checked'])

print(todo_list['items'][0]['checked'])
print(type(todo_list['items'][0]['checked']))